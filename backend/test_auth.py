import requests
import json

BASE_URL = "http://localhost:8000"

def test_register():
    """Test the registration endpoint"""
    print("Testing registration endpoint...")
    
    register_data = {
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "securepassword123"
    }
    
    response = requests.post(f"{BASE_URL}/api/v1/auth/register", json=register_data)
    print(f"Registration Status Code: {response.status_code}")
    print(f"Registration Response: {json.dumps(response.json(), indent=2)}")
    
    return response

def test_login():
    """Test the login endpoint"""
    print("\nTesting login endpoint...")
    
    login_data = {
        "username": "testuser@example.com",  # Using email as username for login
        "password": "securepassword123"
    }
    
    response = requests.post(f"{BASE_URL}/api/v1/auth/login", data=login_data)
    print(f"Login Status Code: {response.status_code}")
    print(f"Login Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 200:
        return response.json().get('access_token')
    return None

if __name__ == "__main__":
    # Test registration
    register_response = test_register()
    
    # Test login if registration was successful
    if register_response.status_code == 200:
        access_token = test_login()
        if access_token:
            print(f"\nSuccessfully obtained access token: {access_token[:20]}...")
    else:
        print("\nRegistration failed, skipping login test.")