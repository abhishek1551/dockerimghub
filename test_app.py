from app import app

def test_home():
    # Creating a test client for the Flask app
    response=app.test_client().get("/")
    # Asserting that the status code is 200 (OK)
    assert response.status_code==200
    # Asserting that the response data is 'Hello World' (note the b prefix for bytes)
    assert response.data== b"Hello, World!"