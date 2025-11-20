import requests
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError

BASE_URL = "https://reqres.in/api"

# Define the expected JSON Schema for a single user response (Contract Validation)
SINGLE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
            },
            # All these fields are MANDATORY in the response
            "required": ["id", "email", "first_name", "last_name"], 
        },
        "support": {"type": "object"}
    },
    "required": ["data", "support"]
}

def test_get_single_user_success():
    """Test Case 1: Verifies successful fetching of a user and validates the API contract (schema)."""
    user_id = 2
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    
    # Senior Skill 1: Validate Status Code
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    
    response_data = response.json()
    
    # Senior Skill 2: Validate Data Payload / Contract using jsonschema
    try:
        validate(instance=response_data, schema=SINGLE_USER_SCHEMA)
    except ValidationError as e:
        pytest.fail(f"Schema Validation Failed: {e}") # Fail the test if the structure is wrong
        
    # Senior Skill 3: Validate Business Logic/Data
    assert response_data['data']['id'] == user_id
    assert response_data['data']['first_name'] == "Janet"


def test_post_create_user_success():
    """Test Case 2: Verifies successful creation of a new user."""
    
    new_user_data = {
        "name": "Jane Doe",
        "job": "QA Automation Senior"
    }
    
    response = requests.post(f"{BASE_URL}/users", json=new_user_data)
    
    # Validate Status Code (201 is the standard for POST/Creation)
    assert response.status_code == 201, f"Expected status 201 (Created), got {response.status_code}"
    
    response_data = response.json()
    
    # Validate payload contains expected data and generated fields
    assert response_data['name'] == new_user_data['name']
    assert response_data['job'] == new_user_data['job']
    assert 'id' in response_data # Check that the system assigned an ID
    assert 'createdAt' in response_data # Check for a creation timestamp


def test_get_user_not_found():
    """Test Case 3: Verifies correct error handling for a non-existent user."""
    
    user_id = 999
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    
    # Validate Status Code (404 Not Found)
    assert response.status_code == 404, f"Expected status 404, got {response.status_code}"
    
    # Validate response body is empty (common for 404 on this API)
    assert response.json() == {}
