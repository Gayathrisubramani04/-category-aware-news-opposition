from backend import create_app

app = create_app()
client = app.test_client()

samples = [
    "The government announced a new election reform that aims to increase voter turnout.",
    "The team secured a last-minute victory in the championship match after an incredible comeback.",
    "A local shop opened downtown offering artisanal bread and coffee."
]

for s in samples:
    resp = client.post('/analyze', json={'text': s})
    print('INPUT:', s)
    print('STATUS:', resp.status_code)
    print('JSON:', resp.get_json())
    print('-' * 60)
