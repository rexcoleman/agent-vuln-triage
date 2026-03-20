# Conference Abstract — Agent Vulnerability Triage

**Title:** LLM Agent Vulnerability Triage: An Empirical Comparison Against EPSS Using CISA KEV Ground Truth

**Target venue:** AISec Workshop (ACM CCS 2026) [HYPOTHESIZED]

**Authors:** Rex Coleman, Singularity Cybersecurity LLC

---

## Abstract (250 words)

Every security team wants to know if AI can help prioritize the CVE flood. We evaluate whether an LLM agent (Claude Haiku) can outperform the Exploit Prediction Scoring System (EPSS), using CISA's Known Exploited Vulnerabilities catalog as ground truth. This matters because EPSS is the current best practice, and LLM agents promise contextual reasoning that statistical models lack.

Across 100 CVEs per seed (15% KEV rate, 5 seeds), the agent achieves 92% precision@10 — outperforming CVSS (82%) and random (14%), but underperforming EPSS (100%). This is an honest negative result: LLM agents do not beat purpose-built statistical models. However, an agent+EPSS ensemble achieves 98% precision@10 with dramatically lower variance (plus/minus 4% vs 12%), and enrichment ablation shows exploit database info is the highest-value source (+6pp) while vendor advisories add nothing. Four pre-registered hypotheses yielded 1 not supported, 1 partially supported, 1 not supported on pre-registered metric, and 1 inconclusive.

Attendees will leave with empirical guidance on when to use EPSS alone versus an LLM ensemble, which enrichment data sources matter, and a reproducible evaluation framework for benchmarking their own triage agents.

**Keywords:** vulnerability management, LLM agents, EPSS, CISA KEV, triage, negative results

---

## Author Bio

**Rex Coleman** is the founder of Singularity Cybersecurity LLC, focused on AI security research. His research spans security OF AI systems and security FROM AI, with prior work in vulnerability prioritization, multi-agent security, and LLM watermark robustness. Previously at FireEye/Mandiant in data analytics and sales. MS Computer Science, Georgia Tech (ML). Securing AI from the architecture up.
