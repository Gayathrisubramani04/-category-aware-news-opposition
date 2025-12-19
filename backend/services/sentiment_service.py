"""Sentiment analysis service using VADER.

Provides a simple function returning a label and compound score.
"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import Dict, Tuple

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> Tuple[str, float]:
    """Return (label, compound_score).

    Labels: 'Positive', 'Neutral', 'Negative'
    """
    if not text:
        return 'Neutral', 0.0
    scores = analyzer.polarity_scores(text)
    compound = scores.get('compound', 0.0)
    if compound >= 0.05:
        label = 'Positive'
    elif compound <= -0.05:
        label = 'Negative'
    else:
        label = 'Neutral'
    return label, float(compound)
