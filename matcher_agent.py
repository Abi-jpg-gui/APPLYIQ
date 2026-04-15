# modules/agents/matcher_agent.py

from modules.embedding_engine import get_embedding
from modules.matcher import calculate_match

def match_jobs(resume_text, jobs):
    results = []
    resume_vec = get_embedding(resume_text)

    for job in jobs:
        job_vec = get_embedding(job["description"])
        score = calculate_match(resume_vec, job_vec)

        job["score"] = score
        results.append(job)

    return sorted(results, key=lambda x: x["score"], reverse=True)