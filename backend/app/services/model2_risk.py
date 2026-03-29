from app.utils.constants import RISK_RULES


def assess_risk(data: dict):
    risks = []

    for rule_name, rule in RISK_RULES.items():
        try:
            if rule["condition"](data):
                risks.append(rule["message"])
        except Exception:
            # Fail-safe: skip broken rule
            continue

    return risks
