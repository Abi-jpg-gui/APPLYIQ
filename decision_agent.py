# modules/agents/decision_agent.py

def decide(job):
    if job["score"] > 85:
        return "AUTO_APPLY"
    elif job["score"] > 65:
        return "REVIEW"
    else:
        return "REJECT"