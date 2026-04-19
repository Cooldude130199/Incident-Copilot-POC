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
