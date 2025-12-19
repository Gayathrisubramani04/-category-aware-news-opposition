from flask import Blueprint, request, jsonify

from ..services.category_service import detect_category
from ..services.sentiment_service import analyze_sentiment
from ..services.opposition_service import generate_opposition

bp = Blueprint('analyze', __name__)


@bp.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json() or {}
        text = data.get('text')
        if text is None:
            return jsonify({'error': 'text field is required'}), 400
        if not isinstance(text, str):
            return jsonify({'error': 'text must be a string'}), 400
        text = text.strip()
        if len(text) == 0:
            return jsonify({'error': 'text must not be empty'}), 400
        if len(text) < 10:
            return jsonify({'error': 'text must be at least 10 characters'}), 400
        if len(text) > 5000:
            return jsonify({'error': 'text must be at most 5000 characters'}), 400

        category = detect_category(text)
        label, score = analyze_sentiment(text)
        opp_full = generate_opposition(text, category=category, sentiment=label)

        # The opposition service appends a disclaimer. Try to split it out.
        disclaimer_marker = "\n\nDisclaimer:"
        if disclaimer_marker in opp_full:
            opposition_view, disclaimer_tail = opp_full.split(disclaimer_marker, 1)
            disclaimer = "Disclaimer:" + disclaimer_tail.strip()
            opposition_view = opposition_view.strip()
        else:
            opposition_view = opp_full
            disclaimer = (
                "Disclaimer: This is an AI-generated educational opinion intended to encourage critical thinking. "
                "It is not professional advice."
            )

        response = {
            'category': category,
            'sentiment': {'label': label, 'score': score},
            'opposition_view': opposition_view,
            'disclaimer': disclaimer
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': 'internal server error', 'details': str(e)}), 500
