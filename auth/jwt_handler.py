import time
from typing import Dict
from jwt import encode, decode

from config.config import Settings


def token_response(token: str):
    return {"access_token": token, "token_type": "Bearer"}


secret_key = Settings().secret_key


def sign_jwt(email: str) -> Dict[str, str]:
    # Set the expiry time.
    payload = {"email": email, "expires": time.time() + 2400}
    return token_response(encode(payload, secret_key, algorithm="HS256"))


def decode_jwt(token: str) -> dict:
    decoded_token = decode(token.encode(), secret_key, algorithms=["HS256"])
    return decoded_token if decoded_token["expires"] >= time.time() else {}