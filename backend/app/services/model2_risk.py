def assess_risk(data):
    risks = []

    if data.get("hemoglobin", 15) < 12:
        risks.append("Possible Anemia")

    if data.get("platelets", 200000) < 150000:
        risks.append("Low Platelet Risk")

    return risks
