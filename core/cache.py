from collections import deque

class AuthTokenCache:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.cache = deque()

    def get_token(self, token_key):
        # Iterate through the cache to find the token
        for token in self.cache:
            if token['key'] == token_key:
                return token['token']
        return None

    def set_token(self, token_key, token_value):
        # Remove the token if it already exists
        for token in self.cache:
            if token['key'] == token_key:
                self.cache.remove(token)
                break

        # Add new token
        if len(self.cache) >= self.max_size:
            self.cache.popleft()  # Remove the oldest token

        self.cache.append({'key': token_key, 'token': token_value})
