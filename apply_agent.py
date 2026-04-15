# modules/agents/apply_agent.py

import datetime

def apply(job):
    return {
        "company": job["company"],
        "role": job["title"],
        "status": "Applied",
        "link": job["link"],
        "time": str(datetime.datetime.now())
    }