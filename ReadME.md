# 🚨 Incident Copilot Dashboard

AI-powered ServiceNow Incident Analysis & Escalation

---

## 📖 Overview
Incident Copilot is a Proof of Concept (POC) designed to automate incident analysis, categorization, SLA monitoring, and escalation drafting using **Agentic AI orchestration**. It integrates with ServiceNow incident data and provides recruiter-ready dashboards for managers.

---

## ✨ Features
- **Incident Ingestion**: Pulls incident data from ServiceNow.
- **Analyzer Agent**: Categorizes incidents into clear buckets:
  - Hardware Issues
  - Network/Connectivity Issues
  - Access/Authentication Issues
  - Installation/Software Issues
  - Email/Communication Issues
- **Communicator Agent**: Generates polished escalation drafts with actionable recommendations.
- **Dashboard**: Streamlit-based UI with:
  - Metrics (Total Incidents, Priority 1, SLA Breaches)
  - Bar chart of incident categories
  - Trend chart with SLA breach highlights
  - Export options (CSV/Excel)
- **Recruiter-ready Output**: Professional escalation notes with clear categories.

---

## 🛠️ Tech Stack
- **Python** (core logic)
- **Streamlit** (dashboard UI)
- **Altair** (visualizations)
- **OpenAI GPT-4** (communicator agent)
- **CrewAI orchestration** (multi-agent pipeline)
- **ServiceNow API** (incident ingestion)

---

## 📂 Project Structure

![Project Structure](https://github.com/Cooldude130199/Incident-Copilot-POC/blob/main/assets/Project%20structure.png)

---

## 🚀 How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt


3. Run the dashboard:

        streamlit run dashboard.py

4. Access the dashboard at http://localhost:8501


---


## AI POWERED INCIDENT COPILOT DEMO:


![DEMO - STREAMLIT](https://github.com/Cooldude130199/Incident-Copilot-POC/blob/main/assets/Demo%20Output.png)

---

## 📊 Example Output

Metrics

![Metrics](https://github.com/Cooldude130199/Incident-Copilot-POC/blob/main/assets/Metrics.png)

---

## ✉️ Example Escalation Draft 

**Title**: Escalation Report – April 2026

**Findings**:
- Hardware issues impacting 3 users
- Network connectivity failures recurring
- SLA breaches detected in 3 Priority 1 incidents

**Recommendations**:
- Assign Hardware team to resolve device failures
- Network team to investigate VPN/connectivity issues
- Immediate escalation of SLA breaches to Incident Manager

---

## 🚀 Next Optional Enhancements
- If you want to take this POC from “working demo” to “flagship recruiter‑ready showcase,” you could add:
- PDF export: bundle metrics, charts, and escalation draft into a single report.
- Interactive filters: filter incidents by priority, category, or date range.
- Drill‑down views: click a category bar to see the underlying incidents.
- CI/CD pipeline: containerize with Docker and deploy to Streamlit Cloud or Azure for a polished demo.

---

## 📌 Conclusion
    This POC demonstrates how Agentic AI orchestration can streamline ITSM workflows, providing managers with clear insights, polished escalation drafts, and recruiter-ready dashboards.


---

This README is recruiter‑ready: it explains the **problem solved**, the **tech stack**, the **workflow**, and shows **sample outputs**. If you want, I can also add a **screenshots section** so visuals of the dashboard appear directly in the README. Would you like me to extend it with that?