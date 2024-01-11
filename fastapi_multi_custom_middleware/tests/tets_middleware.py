from fastapi.testclient import TestClient
import app

# at the end of the file
client = TestClient(app)

def test_modify_request_response_middleware():
    # Send a GET request to the hello endpoint
    response = client.get("/norma/with_extra_heasers")
    # Assert the response status code is 200
    assert response.status_code == 200
    # Assert the middleware has been applied
    assert response.headers.get("X-Custom-Header") == "Modified"
    # Assert the response content
    assert response.json() == {"message": "Hello, World!"}
    