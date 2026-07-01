def generate_recommendations(profile, breakdown):
    recommendations = []

    if breakdown["savings"] < 30:
        recommendations.append(
            "Increase your monthly savings."
        )

    if breakdown["emergency"] < 25:
        recommendations.append(
            "Build an emergency fund covering at least 6 months of expenses."
        )

    if breakdown["insurance"] < 20:
        recommendations.append(
            "Increase your life insurance coverage."
        )

    if breakdown["debt"] < 25:
        recommendations.append(
            "Reduce your EMI and avoid taking unnecessary loans."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Excellent financial health! Keep it up."
        )

    return recommendations