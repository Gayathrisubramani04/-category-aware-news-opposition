from flask import Blueprint, request, jsonify
from .sentiment import analyzer

bp = Blueprint('opposition', __name__)


def generate_opposition(text: str) -> str:
    scores = analyzer.polarity_scores(text)
    compound = scores.get('compound', 0.0)
    if compound >= 0.05:
        suggestion = "raise concerns or highlight potential downsides"
    elif compound <= -0.05:
        suggestion = "point out benefits or mitigating factors"
    else:
        suggestion = "provide a clear opposing stance"
    snippet = text.strip().split('.')
    first = snippet[0] if snippet and snippet[0] else text[:120]
    return f'Opposing view to the article\'s opening "{first.strip()}": Consider the alternative perspective that {suggestion}.'


@bp.route('/opposition', methods=['POST'])
def opposition():
    data = request.get_json() or {}
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'text required'}), 400
    opp = generate_opposition(text)
    return jsonify({'opposition': opp})
