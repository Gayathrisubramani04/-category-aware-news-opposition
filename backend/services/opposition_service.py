"""Opposition opinion generator.

Generates a respectful, non-inflammatory counter-opinion based on category and sentiment.
Always appends a disclaimer that this is an AI-generated educational opinion.
"""
from typing import Optional


def generate_opposition(text: str, category: Optional[str] = None, sentiment: Optional[str] = None) -> str:
    """Create a short, respectful counter-opinion.

    Parameters:
    - text: original article or excerpt
    - category: 'Politics' | 'Sports' | 'Unknown'
    - sentiment: 'Positive' | 'Neutral' | 'Negative' | None

    Returns a string that includes a one-sentence counterpoint and a disclaimer.
    """
    base = (text.strip().split('.') or [''])[0].strip()
    if not base:
        base = 'The article'

    # Default safe suggestions
    if category == 'Politics':
        if sentiment == 'Positive':
            counter = "consider potential unintended consequences and fiscal or social trade-offs."
        elif sentiment == 'Negative':
            counter = "acknowledge possible benefits or longer-term gains that may be overlooked."
        else:
            counter = "offer a concrete alternative policy or approach that addresses the same goals."
    elif category == 'Sports':
        if sentiment == 'Positive':
            counter = "highlight tactical or personnel concerns that could affect future performance."
        elif sentiment == 'Negative':
            counter = "note underlying strengths or contextual factors that support the team or player."
        else:
            counter = "suggest a different strategic interpretation or emphasize additional evidence."
    else:
        # Unknown category: neutral, general-style counterpoint
        if sentiment == 'Positive':
            counter = "point out caveats and scenarios where the positive outcome may not hold."
        elif sentiment == 'Negative':
            counter = "mention possible advantages or counter-evidence that soften the negative view."
        else:
            counter = "provide an alternative interpretation that encourages further exploration."

    opposition = f"Opposing perspective to '{base}': I would {counter}"
    disclaimer = (
        "\n\nDisclaimer: This is an AI-generated educational opinion intended to encourage critical thinking. "
        "It is not professional advice."
    )
    return opposition + disclaimer
