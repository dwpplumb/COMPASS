"""
Goal Reflection Module
Analyzes alignment of an action or plan with the system's internal goal model.
"""

def reflect_on_goal(data):
    """
    Erweiterte Zielreflexionslogik.
    :param data: dict
    :return: str – "aligned", "neutral" oder "misaligned"
    """
    system_goals = {"connect", "stabilize", "harmonize"}
    user_goal = data.get("goal")

    if not user_goal:
        return "neutral"

    if isinstance(user_goal, list):
        alignment_scores = [1 if goal in system_goals else 0 for goal in user_goal]
        average_score = sum(alignment_scores) / len(alignment_scores)
        if average_score > 0.7:
            return "aligned"
        elif average_score > 0.3:
            return "neutral"
        else:
            return "misaligned"
    else:
        return "aligned" if user_goal in system_goals else "misaligned"
