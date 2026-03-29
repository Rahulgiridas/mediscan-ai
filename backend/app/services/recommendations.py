def generate_recommendations(summary):
    recs = []

    if "Possible Anemia" in summary["risks"]:
        recs.append("Increase iron-rich foods")
        recs.append("Consult a doctor")

    return recs
