# For: general security Discord

tested whether an LLM agent can beat EPSS at vulnerability triage. short answer: no. Claude Haiku gets 92% precision@10 but EPSS gets 100% on this data. the interesting part is the ensemble.

```
method              precision@10
EPSS                100% ± 0%
ensemble (agent+EPSS) 98% ± 4%
agent alone          92% ± 12%
CVSS                 82% ± 12%
random               14% ± 10%

enrichment ablation:
CVE description only    88%
+ exploit DB info       94%
+ vendor advisories     92%  ← adding more hurts
```

the agent's value isn't beating EPSS — it's variance reduction (±12% → ±4% in ensemble) and qualitative reasoning. it can explain WHY a vuln is dangerous, which matters when you're writing emergency patch justifications at 2am. also exploit DB is the one enrichment source worth integrating — vendor advisories are basically noise.

if you're building agent-based triage into a SOC workflow, the agent alone isn't the play. EPSS for ranking + agent for justification text is the sweet spot. and resist the temptation to throw every data source at the agent — more context actually degrades precision after exploit DB.

anyone running LLM-assisted triage in production? what enrichment sources are you feeding it?
