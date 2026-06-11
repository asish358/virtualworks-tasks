import re

def analyze_email(email_text):
    risk_score = 0
    findings = []

    # Urgent keywords
    urgent_keywords = [
        "urgent", "immediately", "asap",
        "act now", "limited time", "verify now"
    ]

    # Sensitive data keywords
    sensitive_keywords = [
        "password", "otp", "bank account",
        "credit card", "debit card",
        "cvv", "pin", "ssn"
    ]

    # Threatening keywords
    threat_keywords = [
        "account suspended",
        "legal action",
        "your account will be closed",
        "security alert"
    ]

    email_lower = email_text.lower()

    # Check urgent requests
    for word in urgent_keywords:
        if word in email_lower:
            risk_score += 2
            findings.append(f"Urgent phrase detected: '{word}'")

    # Check sensitive data requests
    for word in sensitive_keywords:
        if word in email_lower:
            risk_score += 3
            findings.append(f"Sensitive information request detected: '{word}'")

    # Check threatening language
    for word in threat_keywords:
        if word in email_lower:
            risk_score += 2
            findings.append(f"Threatening phrase detected: '{word}'")

    # Detect links
    links = re.findall(r'https?://\S+|www\.\S+', email_text)

    if links:
        risk_score += len(links)
        findings.append(f"Found {len(links)} link(s):")
        for link in links:
            findings.append(f"  - {link}")

    # Risk classification
    if risk_score >= 8:
        risk_level = "HIGH RISK"
    elif risk_score >= 4:
        risk_level = "MEDIUM RISK"
    else:
        risk_level = "LOW RISK"

    return risk_level, findings


def main():
    print("=" * 50)
    print("EMAIL RISK ANALYZER")
    print("=" * 50)

    print("\nPaste the email content below:")
    email_text = input("\nEmail Content:\n")

    risk_level, findings = analyze_email(email_text)

    print("\n" + "=" * 50)
    print("ANALYSIS REPORT")
    print("=" * 50)

    print(f"Risk Level: {risk_level}")

    if findings:
        print("\nFindings:")
        for item in findings:
            print("-", item)
    else:
        print("\nNo suspicious patterns detected.")

    print("\nAnalysis Complete.")


if __name__ == "__main__":
    main()
