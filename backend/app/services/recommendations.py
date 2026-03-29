from app.utils.constants import RECOMMENDATIONS_MAP


def generate_recommendations(summary: dict):
    recommendations = set()

    risks = summary.get("risks", [])

    for risk in risks:
        if risk in RECOMMENDATIONS_MAP:
            for rec in RECOMMENDATIONS_MAP[risk]:
                recommendations.add(rec)

    return list(recommendations)
