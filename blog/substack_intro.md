# Substack Introduction — Agent Vulnerability Triage

**Subject line:** Can an AI triage your vulnerabilities? We tested it against EPSS.

---

Every security team wants to know: can AI help prioritize the CVE flood? We tested Claude Haiku as a vulnerability triage agent against EPSS, CVSS, and random baselines.

The agent scores 92% precision@10. That's good — but EPSS scores 100%. The AI doesn't beat the statistical model.

The full post explains why that's actually the interesting finding, what enrichment data matters (exploit DB yes, vendor advisories no), and why the ensemble approach (agent + EPSS at 98%) might be the real answer.

**Read the full analysis →** [link]
