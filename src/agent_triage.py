"""LLM agent for CVE triage — ranks CVEs by exploitability using Claude Haiku."""
import json
import anthropic


def triage_cves(client, cves, enrichment_level="full", prompt_style="structured", seed=42):
    """Ask Claude Haiku to rank CVEs by exploitability.

    Args:
        client: Anthropic client
        cves: list of dicts with 'cve_id', 'description', optionally 'exploit_info', 'vendor_info'
        enrichment_level: 'minimal' (CVE desc only), 'exploit' (+exploit DB), 'full' (+vendor)
        prompt_style: 'minimal' or 'structured'
        seed: for reproducibility (temperature=0 for determinism)

    Returns: list of cve_ids ranked from highest to lowest priority
    """
    # Build CVE descriptions based on enrichment level
    cve_texts = []
    for cve in cves:
        text = f"- {cve['cve_id']}: {cve['description']}"
        if enrichment_level in ('exploit', 'full') and cve.get('exploit_info'):
            text += f"\n  Exploit info: {cve['exploit_info']}"
        if enrichment_level == 'full' and cve.get('vendor_info'):
            text += f"\n  Vendor advisory: {cve['vendor_info']}"
        cve_texts.append(text)

    cve_block = "\n".join(cve_texts)

    if prompt_style == "minimal":
        prompt = f"Rank these CVEs from most to least likely to be actively exploited. Return only CVE IDs, one per line, highest priority first.\n\n{cve_block}"
    else:
        prompt = f"""You are a vulnerability triage analyst. Rank the following CVEs from MOST to LEAST likely to be actively exploited in the wild.

Consider:
- Severity and attack complexity
- Whether public exploits exist
- Whether the vulnerability affects widely-deployed software
- Historical patterns of exploitation for similar vulnerability types

Return ONLY the CVE IDs, one per line, highest priority first. No explanations.

CVEs to rank:
{cve_block}"""

    resp = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}],
    )

    # Parse ranked CVE IDs from response
    text = resp.content[0].text
    ranked = []
    for line in text.strip().split("\n"):
        line = line.strip().strip("- ").strip()
        # Extract CVE ID pattern
        for word in line.split():
            if word.startswith("CVE-"):
                ranked.append(word.rstrip(",:;"))
                break

    return ranked
