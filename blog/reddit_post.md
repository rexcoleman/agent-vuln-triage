# I tested an LLM agent against EPSS for vulnerability triage — the agent scores 92% precision but can't beat a purpose-built statistical model

I built a Claude Haiku vulnerability triage agent and benchmarked it against EPSS, CVSS, and random baselines using CISA KEV as ground truth. The agent achieves 92% precision@10, meaning 9 of its top 10 ranked CVEs are actually exploited. But EPSS hits 100% on this data. The agent can't beat a purpose-built model on its own distribution. The interesting finding is the ensemble: agent + EPSS together reach 98% with dramatically lower variance (+/-4% vs +/-12%).

I tested on 100 CVEs per seed (15% KEV rate), 5 seeds, with pre-registered hypotheses. The agent's variance is the key issue — seed 3 drops to 70% precision while EPSS is stable at 100% on every seed. The ensemble compensates: even on the agent's worst seeds, EPSS pulls the ranking back up.

Key takeaways:

- **EPSS beats the LLM agent on well-structured vulnerability data** — 100% vs 92% precision@10, hypothesis "agent outperforms EPSS" is not supported
- **The ensemble is the real finding** — 98% precision with 3x lower variance than either alone
- **Exploit DB is the one enrichment source worth adding** — boosts agent precision from 88% to 94%, vendor advisories don't help beyond that
- **The agent adds qualitative value EPSS can't** — it explains WHY a vulnerability is dangerous, useful for emergency patching justifications
- **If you're choosing one tool, use EPSS** — it's free and hard to beat. If you want the best possible triage, use both

Methodology: Claude 3 Haiku agent ranking CVEs by exploitation likelihood, measured by precision@10 against CISA KEV catalog. 5 seeds, enrichment ablation (CVE-only vs exploit DB vs full), pre-registered hypotheses. ~$0.50 API cost, 3 minutes runtime.

Repo: [github.com/rexcoleman/agent-vuln-triage](https://github.com/rexcoleman/agent-vuln-triage)

Code is open source with reproduce.sh. Happy to answer questions about the methodology or how to integrate this into a triage workflow.
