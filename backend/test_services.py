from services.category_service import detect_category
from services.sentiment_service import analyze_sentiment
from services.opposition_service import generate_opposition


def run_tests():
    samples = [
        ("The government passed a new election reform policy to improve voter access.", 'Politics'),
        ("The team won the match with an incredible comeback in the final minute.", 'Sports'),
        ("Local bakery opens downtown.", 'Unknown')
    ]

    for text, expected_cat in samples:
        cat = detect_category(text)
        label, score = analyze_sentiment(text)
        opp = generate_opposition(text, category=cat, sentiment=label)
        print('TEXT:', text)
        print('DETECTED CATEGORY:', cat, 'EXPECTED:', expected_cat)
        print('SENTIMENT:', label, 'COMPOUND:', score)
        print('OPPOSITION SAMPLE:', opp)
        print('-' * 60)


if __name__ == '__main__':
    run_tests()
