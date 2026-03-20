# Conference Abstract — Agent Vulnerability Triage

**Title:** LLM Agent Vulnerability Triage: An Empirical Comparison Against EPSS Using CISA KEV Ground Truth

**Target venue:** AISec Workshop (ACM CCS 2026) [HYPOTHESIZED]

**Authors:** Rex Coleman, Singularity Cybersecurity LLC

---

## Abstract (250 words)

We evaluate whether an LLM agent (Claude Haiku) can prioritize vulnerabilities more effectively than the Exploit Prediction Scoring System (EPSS), using CISA's Known Exploited Vulnerabilities catalog as ground truth. Across 100 CVEs per seed (15% KEV rate, 5 seeds), the agent achieves 92% precision@10 — outperforming CVSS ranking (82%) and random (14%), but underperforming EPSS (100%). This is an honest negative result for our primary hypothesis: LLM agents do not outperform purpose-built statistical models on data that correlates with those models' training distribution.

However, an agent+EPSS ensemble achieves 98% precision@10 with dramatically lower variance (±4% vs ±12%), suggesting the agent captures complementary signal. Enrichment ablation shows exploit database info is the highest-value data source (+6pp over CVE description alone), while vendor advisories provide no additional improvement.

We pre-registered four hypotheses under our research governance framework: H-1 (agent beats EPSS) NOT SUPPORTED, H-2 (enrichment helps) PARTIALLY SUPPORTED, H-3 (ensemble wins) NOT SUPPORTED on pre-registered metric, H-4 (temporal degradation) INCONCLUSIVE. The governance framework forced honest reporting of the negative result and prevented post-hoc reframing.

Our contribution is empirical: practitioners should use EPSS for raw ranking, but combine with LLM agents for qualitative context and ensemble stability. The agent adds reasoning and explanation that statistical models cannot provide.

**Keywords:** vulnerability management, LLM agents, EPSS, CISA KEV, triage, negative results

---

## Author Bio

**Rex Coleman** is the founder of Singularity Cybersecurity LLC, focused on AI security research. His research spans security OF AI systems and security FROM AI, with prior work in vulnerability prioritization, multi-agent security, and LLM watermark robustness. Previously at FireEye/Mandiant in data analytics and sales. MS Computer Science, Georgia Tech (ML). Securing AI from the architecture up.
