import streamlit as st
import pandas as pd
import altair as alt
from crew import run_pipeline

st.set_page_config(page_title="Incident Copilot Dashboard", layout="wide")

st.title("🚨 Incident Copilot Dashboard")
st.markdown("AI-powered ServiceNow Incident Analysis & Escalation")

# Run the CrewAI pipeline
escalation_note, summary = run_pipeline()

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Metrics")

    # Color-coded metrics
    st.markdown(f"<span style='color:blue'>Total Incidents:</span> **{summary.get('total_incidents', 0)}**", unsafe_allow_html=True)
    st.markdown(f"<span style='color:green'>Priority 1 Incidents:</span> **{summary.get('priority_summary', {}).get('1', 0)}**", unsafe_allow_html=True)
    st.markdown(f"<span style='color:red'>SLA Breaches:</span> **{len(summary.get('sla_breaches', []))}**", unsafe_allow_html=True)

    # --- Bar Chart: Incident Categories ---
    st.write("**Incident Categories (Top Issues):**")
    common_terms = summary.get("common_terms", [])
    if common_terms:
        df = pd.DataFrame(common_terms, columns=["Category", "Count"])
        chart = alt.Chart(df).mark_bar(color="steelblue").encode(
            x=alt.X("Category", sort="-y"),
            y="Count",
            tooltip=["Category", "Count"]
        ).properties(width=400, height=300)
        st.altair_chart(chart, use_container_width=True)

    # --- Trend Chart: Incidents Over Time ---
    st.write("**Incident Trend (per day/week):**")
    if "incident_timeline" in summary:
        df_timeline = pd.DataFrame(summary["incident_timeline"], columns=["Date", "Count"])

        # Add SLA breach markers
        df_timeline["Status"] = "Normal"
        for breach in summary.get("sla_breaches", []):
            # If you have incident dates per breach, mark them here
            # Example: df_timeline.loc[df_timeline["Date"] == breach_date, "Status"] = "SLA Breach"
            pass

        line_chart = alt.Chart(df_timeline).mark_line(point=True).encode(
            x="Date:T",
            y="Count:Q",
            color=alt.Color("Status", scale=alt.Scale(domain=["Normal","SLA Breach"], range=["green","red"])),
            tooltip=["Date", "Count", "Status"]
        ).properties(width=400, height=300)

        st.altair_chart(line_chart, use_container_width=True)

with col2:
    st.subheader("✉️ Escalation Draft")
    st.markdown(
        f"""
        <div style="background-color:#f8f9fa; padding:15px; border-radius:8px; border:1px solid #ddd;">
        <pre style="font-size:14px; white-space: pre-wrap;">{escalation_note}</pre>
        </div>
        """,
        unsafe_allow_html=True
    )
