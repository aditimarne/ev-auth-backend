# users/authentication.py
import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from .models import User

class MongoJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        # ✅ No token → skip authentication (AllowAny APIs)
        if not auth_header:
            return None

        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return None

        token = parts[1]

        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            # 🔥 IMPORTANT: don't block public APIs
            return None
        except jwt.InvalidTokenError:
            return None

        user_id = payload.get("user_id")
        if not user_id:
            return None

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

        return (user, None)