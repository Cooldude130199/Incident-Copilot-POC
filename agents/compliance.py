from datetime import datetime

def check_sla(incidents):
    sla_breaches = []
    for inc in incidents:
        created = datetime.strptime(inc['sys_created_on'], "%Y-%m-%d %H:%M:%S")
        age_hours = (datetime.now() - created).total_seconds() / 3600

        if inc['priority'] == "1" and age_hours > 4 and inc['state'] != "Resolved":
            sla_breaches.append(inc['number'])
        elif inc['priority'] == "2" and age_hours > 8 and inc['state'] != "Resolved":
            sla_breaches.append(inc['number'])

    return sla_breaches
