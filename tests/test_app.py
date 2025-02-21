import requests

def test_api_endpoint():
    response = requests.get('https://your-deployed-url.vercel.app/api/your-endpoint')
    assert response.status_code == 200
    assert 'expected_key' in response.json()