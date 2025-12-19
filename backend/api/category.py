from flask import Blueprint, request, jsonify

bp = Blueprint('category', __name__)

CATEGORIES = {
    'politics': ['election', 'government', 'policy', 'senate', 'congress', 'president', 'minister'],
    'sports': ['game', 'match', 'tournament', 'score', 'player', 'team', 'league', 'coach'],
    'technology': ['technology', 'tech', 'software', 'hardware', 'ai', 'machine learning', 'app', 'internet', 'computer'],
    'business': ['market', 'stock', 'economy', 'startup', 'business', 'company', 'finance', 'investment'],
    'entertainment': ['movie', 'film', 'music', 'celebrity', 'tv', 'show', 'concert', 'actor', 'actress'],
    'health': ['health', 'medical', 'doctor', 'disease', 'hospital', 'covid', 'vaccine']
}


def detect_category(text: str) -> str:
    text_l = text.lower()
    scores = {}
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in text_l:
                scores[cat] = scores.get(cat, 0) + 1
    if not scores:
        return 'uncategorized'
    return max(scores, key=scores.get)


@bp.route('/category', methods=['POST'])
def category():
    data = request.get_json() or {}
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'text required'}), 400
    cat = detect_category(text)
    return jsonify({'category': cat})
