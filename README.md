# Authentication Service with Caching

This project demonstrates a simple implementation of an authentication service with a local caching mechanism. It leverages a third-party authentication service to obtain user tokens and caches them locally to reduce latency and improve performance.

## Project Structure

- `auth_service.py`: Contains the `AuthenticationService` class that handles token retrieval and caching.
- `cache.py`: Implements the `AuthTokenCache` class that provides an in-memory cache with FIFO eviction.

## Setup

To get started with this project, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install Requirements:**

    Make sure you have Python 3.11+ installed. Then, install the necessary Python packages using:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configuration:**

    Update the `auth_service.py` file with the correct URL for your third-party authentication service.

4. **Usage:**

    The `AuthenticationService` class can be used to fetch and cache authentication tokens. Here’s an example of how to use it:

    ```python
    from core.third_party_auth_service import AuthenticationService

    # Initialize the service with your authentication URL
    auth_service = AuthenticationService(auth_url='https://example.com/auth')

    # Fetch or cache a token for a user
    user_id = 'example_user'
    token = auth_service.get_auth_token(user_id)
    print(f'Token for user {user_id}: {token}')
    ```

## Explanation

- **`AuthTokenCache`**: This class provides an in-memory cache for tokens. It uses a deque with a fixed maximum size to store tokens. When the cache exceeds its maximum size, it evicts the oldest token (FIFO).
  
- **`AuthenticationService`**: This class interacts with a third-party authentication service to retrieve tokens. It first checks the local cache for the token before making a network request. If the token is not in the cache, it requests a new token and stores it in the cache.
