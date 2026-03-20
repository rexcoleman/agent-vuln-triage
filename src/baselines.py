"""Baseline rankers for CVE triage comparison."""
import random


def rank_by_epss(cves):
    """Rank CVEs by EPSS score (highest first)."""
    return sorted(cves, key=lambda c: c.get('epss_score', 0), reverse=True)


def rank_by_cvss(cves):
    """Rank CVEs by CVSS base score (highest first)."""
    return sorted(cves, key=lambda c: c.get('cvss_score', 0), reverse=True)


def rank_random(cves, seed=42):
    """Random baseline ranking."""
    rng = random.Random(seed)
    shuffled = list(cves)
    rng.shuffle(shuffled)
    return shuffled


def rank_ensemble(agent_ranking, epss_ranking, weight_agent=0.5):
    """Weighted rank fusion of agent and EPSS rankings.

    Lower rank = higher priority. Combines by weighted average of rank positions.
    """
    all_ids = list(set(r for r in agent_ranking + epss_ranking))

    agent_rank = {cve_id: i for i, cve_id in enumerate(agent_ranking)}
    epss_rank = {cve_id: i for i, cve_id in enumerate(epss_ranking)}

    n = len(all_ids)
    scores = {}
    for cve_id in all_ids:
        a_rank = agent_rank.get(cve_id, n)
        e_rank = epss_rank.get(cve_id, n)
        scores[cve_id] = weight_agent * a_rank + (1 - weight_agent) * e_rank

    return sorted(scores.keys(), key=lambda x: scores[x])
