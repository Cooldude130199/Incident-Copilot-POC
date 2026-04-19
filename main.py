from agents.retriever import fetch_incidents
from agents.analyzer import analyze_incidents
from agents.compliance import check_sla
from agents.communicator import draft_escalation
from agents.updater import update_incident

def run_pipeline():
    incidents = fetch_incidents(limit=10)
    summary = analyze_incidents(incidents)
    sla_breaches = check_sla(incidents)
    summary["sla_breaches"] = sla_breaches
    escalation_note = draft_escalation(summary)

    print("=== Incident Analysis ===")
    print(summary)
    print("\n=== Escalation Draft ===")
    print(escalation_note)

    # Push escalation note back into ServiceNow for each SLA breach
    for inc in incidents:
        if inc["number"] in sla_breaches and "sys_id" in inc:
            status = update_incident(inc["sys_id"], escalation_note)
            print(f"Updated {inc['number']} → Status {status}")

if __name__ == "__main__":
    run_pipeline()
