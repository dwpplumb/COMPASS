"""
Contextual Response Generation for COMPASS
Based on evaluation, reflection, and goal structure.
"""

def generate_response_text(goal: str, alignment: str, axiom_comment: str) -> str:
    """
    Generates a natural language response based on evaluation and reflection.
    :param goal: User input (goal term)
    :param alignment: Evaluation (aligned / neutral / misaligned)
    :param axiom_comment: Reflection from axiom profile
    :return: Textual response
    """
    if alignment == "aligned":
        intro = f"✅ The goal \"{goal}\" aligns well with the system's core values."
    elif alignment == "neutral":
        intro = f"ℹ️ The goal \"{goal}\" lies outside the primary system axes but shows potential for integration."
    else:
        intro = f"⚠️ The goal \"{goal}\" tends to diverge from current system logic."

    # Enriched follow-up
    if "strong" in axiom_comment or "high" in axiom_comment:
        follow = " This indicates systemic relevance."
    elif "low" in axiom_comment or "weak" in axiom_comment:
        follow = " The goal may not yet be sufficiently structured or connected."
    else:
        follow = ""

    return intro + "\n" + axiom_comment + follow
