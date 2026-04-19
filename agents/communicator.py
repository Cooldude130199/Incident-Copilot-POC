from openai import OpenAI

client = OpenAI()

def draft_escalation(summary: dict) -> str:
    """
    Generate a professional escalation note using GPT-4 based on the incident summary.
    """

    prompt = f"""
    You are an IT Service Management assistant. Based on this incident summary:

    Priority counts: {summary.get("priority_summary", {})}
    Common issues (raw terms): {summary.get("common_terms", [])}
    SLA breaches: {summary.get("sla_breaches", [])}

    Your task:
    - Group raw terms into meaningful categories (e.g., Email connectivity, VPN login, Password resets, Hardware issues).
    - Ignore irrelevant or vague words (like 'not', 'detecting', 'device', 'installed', '10gr2').
    - Write a professional escalation report with:
      * A clear title
      * Categorized common issues
      * SLA breaches listed explicitly
      * Bullet points for findings
      * Actionable recommendations (which team should act and what to do)
      * Formal, recruiter-ready language with no vague terms or stopwords
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
