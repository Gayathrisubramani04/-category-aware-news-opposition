"""Category detection service (simple rule-based).

Detects only two categories: Politics and Sports. Returns 'Politics', 'Sports', or 'Unknown'.
"""
from typing import Literal

Category = Literal['Politics', 'Sports', 'Unknown']

POLITICS_KEYWORDS = {'election', 'government', 'policy', 'senate', 'congress', 'president', 'minister', 'vote'}
SPORTS_KEYWORDS = {'match', 'game', 'team', 'score', 'player', 'coach', 'tournament', 'league'}


def detect_category(text: str) -> Category:
    """Detects whether `text` is Politics, Sports, or Unknown.

    Uses simple keyword matching; case-insensitive. If both categories match, the one
    with more keyword hits wins; ties -> Unknown.
    """
    if not text:
        return 'Unknown'
    txt = text.lower()

    p_hits = sum(1 for kw in POLITICS_KEYWORDS if kw in txt)
    s_hits = sum(1 for kw in SPORTS_KEYWORDS if kw in txt)

    if p_hits > s_hits and p_hits > 0:
        return 'Politics'
    if s_hits > p_hits and s_hits > 0:
        return 'Sports'
    return 'Unknown'
