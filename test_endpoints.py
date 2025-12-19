from backend import create_app

app = create_app()
client = app.test_client()

print('CATEGORY ->', client.post('/category', json={'text':'The president discussed new government policy and the economy.'}).get_json())
print('SENTIMENT ->', client.post('/sentiment', json={'text':'I absolutely love this product, it exceeded expectations!'}).get_json())
print('OPPOSITION ->', client.post('/opposition', json={'text':'This new policy will greatly improve our economy and help small businesses.'}).get_json())
