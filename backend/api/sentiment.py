from flask import Blueprint, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

bp = Blueprint('sentiment', __name__)
analyzer = SentimentIntensityAnalyzer()


@bp.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.get_json() or {}
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'text required'}), 400
    scores = analyzer.polarity_scores(text)
    compound = scores.get('compound', 0.0)
    if compound >= 0.05:
        label = 'positive'
    elif compound <= -0.05:
        label = 'negative'
    else:
        label = 'neutral'
    return jsonify({'scores': scores, 'label': label})
