# users/models.py
from mongoengine import Document, EmailField, StringField, BooleanField, DateTimeField
from django.db import models
from django.utils import timezone
from datetime import datetime  

class User(Document):
    meta = {"collection": "user"}
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    profile_image = StringField()
    first_name = StringField()
    last_name = StringField()
    mobile = StringField()
    avatar_file_id = StringField()

    def to_dict(self):
        return {
            "id": str(self.id),
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name or "",
            "last_name": self.last_name or "",
            "mobile": self.mobile or "",
            "profile_image": self.profile_image or "",
            "avatar_file_id": self.avatar_file_id or "",
        }

    def __str__(self):
        return self.username
    
class PasswordResetOTP(Document):
    meta = {"collection": "password_reset_otps"}
    
    email = EmailField(required=True)
    otp = StringField(required=True, max_length=6)
    created_at = DateTimeField(default=datetime.utcnow)
    is_used = BooleanField(default=False)

    def is_valid(self):
        diff = datetime.utcnow() - self.created_at
        return not self.is_used and diff.seconds < 600
    @property
    def is_authenticated(self):
        """Needed so DRF permissions work."""
        return True

