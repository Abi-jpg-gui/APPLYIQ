# modules/agents/email_agent.py

def send_email(application):
    return f"""
    📧 Email Sent!

    Job Applied: {application['role']} at {application['company']}
    View Job: {application['link']}

    Status: Applied Successfully
    """