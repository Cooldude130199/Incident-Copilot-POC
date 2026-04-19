from collections import Counter
from datetime import datetime

def analyze_incidents(incidents):
    priorities = Counter([inc['priority'] for inc in incidents])

    # --- Categorization logic inline ---
    def categorize_incident(description: str) -> str:
        desc = description.lower()
        if any(word in desc for word in ["computer", "laptop", "device", "headphone", "printer"]):
            return "Hardware Issue"
        elif any(word in desc for word in ["email", "outlook", "smtp", "mailbox"]):
            return "Email/Communication Issue"
        elif any(word in desc for word in ["vpn", "connect", "network", "wifi", "unable"]):
            return "Network/Connectivity Issue"
        elif any(word in desc for word in ["password", "reset", "login", "authentication", "access"]):
            return "Access/Authentication Issue"
        elif any(word in desc for word in ["install", "installed", "setup", "oracle", "10gr2", "update"]):
            return "Installation/Software Issue"
        else:
            return "Other/Uncategorized"

    # --- Apply categorization to each incident ---
    categories = [categorize_incident(inc['short_description']) for inc in incidents]
    category_counts = Counter(categories)

    # --- SLA breach detection ---
    sla_breaches = []
    timeline_counts = Counter()
    for inc in incidents:
        created = datetime.strptime(inc['sys_created_on'], "%Y-%m-%d %H:%M:%S")
        date_str = created.date().isoformat()
        timeline_counts[date_str] += 1

        if inc['priority'] == "1":  # SLA: 4 hours for P1
            age_hours = (datetime.now() - created).total_seconds() / 3600
            if age_hours > 4 and inc['state'] != "Resolved":
                sla_breaches.append(inc['number'])

    incident_timeline = [(d, c) for d, c in sorted(timeline_counts.items())]

    return {
        "priority_summary": priorities,
        "common_terms": category_counts.most_common(),  # ✅ now categories
        "sla_breaches": sla_breaches,
        "incident_timeline": incident_timeline
    }
