import jwt

# Ensure PyJWT names exist for django-allauth compatibility

# jwt.decode ALWAYS exists in PyJWT>=2.x, but keep fallback for safety
if not hasattr(jwt, "decode"):
    # fallback: import decode manually
    from jwt.api_jwt import decode as jwt_decode
    jwt.decode = jwt_decode

# Ensure PyJWTError exists
if not hasattr(jwt, "PyJWTError"):
    try:
        from jwt.exceptions import InvalidTokenError as PyJWTError
    except ImportError:
        class PyJWTError(Exception):
            pass
    jwt.PyJWTError = PyJWTError

# Ensure ExpiredSignatureError exists
if not hasattr(jwt, "ExpiredSignatureError"):
    try:
        from jwt.exceptions import ExpiredSignatureError
    except ImportError:
        class ExpiredSignatureError(jwt.PyJWTError):
            pass
    jwt.ExpiredSignatureError = ExpiredSignatureError

# Ensure InvalidAudienceError exists
if not hasattr(jwt, "InvalidAudienceError"):
    try:
        from jwt.exceptions import InvalidAudienceError
    except ImportError:
        class InvalidAudienceError(jwt.PyJWTError):
            pass
    jwt.InvalidAudienceError = InvalidAudienceError
