from crewai import Agent, Crew, Task
from agents.retriever import fetch_incidents
from agents.analyzer import analyze_incidents
from agents.compliance import check_sla
from agents.communicator import draft_escalation
from agents.updater import update_incident

# Define agents
retriever_agent = Agent(role="Incident Retriever", goal="Fetch incidents", backstory="Pulls data from ServiceNow")
analyzer_agent = Agent(role="Incident Analyzer", goal="Summarize incidents", backstory="Finds patterns and issues")
compliance_agent = Agent(role="SLA Compliance Checker", goal="Check SLA breaches", backstory="Flags SLA violations")
communicator_agent = Agent(role="Escalation Communicator", goal="Generate escalation notes", backstory="LLM-powered")
updater_agent = Agent(role="ServiceNow Updater", goal="Push escalation notes", backstory="Updates ServiceNow records")

# Define tasks
retriever_task = Task(description="Fetch incidents", agent=retriever_agent, expected_output="List of incidents")
analyzer_task = Task(description="Analyze incidents", agent=analyzer_agent, expected_output="Incident summary")
compliance_task = Task(description="Check SLA compliance", agent=compliance_agent, expected_output="List of SLA breaches")
communicator_task = Task(description="Draft escalation note", agent=communicator_agent, expected_output="Professional escalation note")
updater_task = Task(description="Update ServiceNow", agent=updater_agent, expected_output="Update status")

# Crew orchestration
incident_crew = Crew(
    agents=[retriever_agent, analyzer_agent, compliance_agent, communicator_agent, updater_agent],
    tasks=[retriever_task, analyzer_task, compliance_task, communicator_task, updater_task]
)

def run_pipeline():
    # Step 1: Fetch incidents
    incidents = fetch_incidents(limit=10)

    # Step 2: Analyze incidents
    summary = analyze_incidents(incidents)

    # Step 3: SLA compliance
    sla_breaches = check_sla(incidents)
    summary["sla_breaches"] = sla_breaches
    summary["total_incidents"] = len(incidents)

    # Step 4: Draft escalation note
    escalation_note = draft_escalation(summary)

    # Step 5: Push escalation note back into ServiceNow
    for inc in incidents:
        if inc["number"] in sla_breaches and "sys_id" in inc:
            status = update_incident(inc["sys_id"], escalation_note)
            print(f"Updated {inc['number']} → Status {status}")

    print("\n=== Escalation Draft ===")
    print(escalation_note)

    # ✅ Return both escalation note and summary
    return escalation_note, summary




if __name__ == "__main__":
    run_pipeline()
