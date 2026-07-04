def recommend_career(score):

    if score >= 45:
        return "AI Engineer"

    elif score >= 38:
        return "Data Scientist"

    elif score >= 30:
        return "Software Engineer"

    elif score >= 22:
        return "Web Developer"

    else:
        return "Computer Operator"