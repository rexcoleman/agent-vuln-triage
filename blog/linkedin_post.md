# LinkedIn Post — Agent Vulnerability Triage

I pre-registered 4 hypotheses about LLM agent vulnerability triage. Primary prediction: agent beats EPSS by 15+ percentage points.

Result: agent 92%, EPSS 100%.

NOT SUPPORTED. The agent is good but can't beat a purpose-built statistical model on its own training distribution.

But here's what's interesting: agent + EPSS ensemble hits 98% with half the variance. The agent captures complementary signal — and more importantly, it provides qualitative reasoning EPSS can't. "This CVE targets widely-deployed VPN software with a public exploit" is worth more than "0.87" when you're writing a justification for emergency patching.

The enrichment finding surprised me: exploit DB info adds 6pp. Vendor advisories? Zero additional value. The CVE description + exploit availability is the signal.

Is your team using EPSS for triage? What's the biggest gap?

#VulnerabilityManagement #AISecurity #EPSS #LLMAgents #NegativeResults

---

> First comment: "Full analysis with precision curves and enrichment ablation: [blog URL]"
