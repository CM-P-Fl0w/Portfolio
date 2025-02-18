
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))
import pytest
from app import app  

@pytest.fixture
def client():
    """Create a test client for Flask app"""
    app.config["TESTING"] = True 
    with app.test_client() as client:
        yield client  

def test_home(client):
    """Test if home route is working"""
    response = client.get("/")
    assert response.status_code == 200
  
