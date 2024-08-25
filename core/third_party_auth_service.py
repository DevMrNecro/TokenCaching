# auth_service.py
import requests
from .cache import AuthTokenCache

# Initialize the cache with a maximum size
TOKEN_CACHE = AuthTokenCache(max_size=100)  # Adjust max_size as needed

class AuthenticationService:
    def __init__(self, auth_url):
        self.auth_url = auth_url

    def get_auth_token(self, user_id):
        # Check if token is in cache
        token = TOKEN_CACHE.get_token(user_id)
        if token:
            return token

        # If not in cache, request from third-party service
        response = requests.post(self.auth_url, data={'user_id': user_id})
        if response.status_code == 200:
            token = response.json().get('token')
            # Store token in cache
            TOKEN_CACHE.set_token(user_id, token)
            return token
        else:
            response.raise_for_status()
