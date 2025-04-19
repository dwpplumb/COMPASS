"""
Sprachliche Interpretation von Axiommustern im COMPASS-System
"""

def generate_response_text(user_input: str, alignment: str, profile: dict) -> str:
    """
    Generates a logical, coherent English response based on the axiom profile and alignment.
    The output is designed to sound natural and context-aware, similar to GPT-style interactions.
    """
    phrases = []

    # Intro
    if alignment == "aligned":
        phrases.append(f"Your input \"{user_input}\" aligns well with the system's core principles.")
    elif alignment == "neutral":
        phrases.append(f"Your input \"{user_input}\" shows partial structural relevance, but lacks direct alignment with core goals.")
    elif alignment == "misaligned":
        phrases.append(f"The input \"{user_input}\" diverges from key system values and cannot be readily integrated.")

    # Axiom-based insights
    if profile.get("A1", 0) > 0.4:
        phrases.append("It reflects a distinct existential or identity component.")
    elif profile.get("A1", 0) > 0.2:
        phrases.append("There is a minimal sense of identity or grounding present.")

    if profile.get("A2", 0) > 0.5:
        phrases.append("The structure appears adaptable, with potential for dynamic transformation.")
    elif profile.get("A2", 0) < 0.2:
        phrases.append("Its rigidity suggests low responsiveness to change.")

    if profile.get("A3", 0) > 0.6:
        phrases.append("Temporal progression or sequencing seems dominant.")
    elif profile.get("A3", 0) < 0.2:
        phrases.append("It lacks temporal directionality.")

    if profile.get("A5", 0) > 0.5:
        phrases.append("There is high potential for systemic connection or synergy.")
    elif profile.get("A5", 0) < 0.2:
        phrases.append("The system integration potential is weak.")

    if profile.get("A6", 0) > 0.45:
        phrases.append("It could trigger structural reconfiguration or instability.")

    if profile.get("A7", 0) > 0.4:
        phrases.append("Reflective awareness is active, allowing metalevel interpretation.")

    # Combine
    full_response = " ".join(phrases)
    return full_response or "No evaluative signal could be inferred from the input."


def interpret_axiom_profile(profile: dict) -> str:
    """
    Analyzes the axiom profile and returns a compact descriptive reflection string.
    """
    comments = []

    if profile.get("A1", 0) > 0.5:
        comments.append("strong existential grounding")
    elif profile.get("A1", 0) > 0.3:
        comments.append("moderate sense of identity or presence")

    if profile.get("A2", 0) > 0.5:
        comments.append("dynamic structural flexibility")
    elif profile.get("A2", 0) < 0.2:
        comments.append("low transformation resistance")

    if profile.get("A3", 0) > 0.6:
        comments.append("strong temporal orientation")
    elif profile.get("A3", 0) < 0.2:
        comments.append("no temporal gradient identified")

    if profile.get("A5", 0) > 0.5:
        comments.append("strong systemic connectivity")
    elif profile.get("A5", 0) < 0.2:
        comments.append("weak integrative capability")

    if profile.get("A6", 0) > 0.45:
        comments.append("potential for structural destabilization")

    if profile.get("A7", 0) > 0.4:
        comments.append("reflective awareness present")

    if not comments:
        return "low semantic anchoring detected"

    return ", ".join(comments)
