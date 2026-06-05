from django.urls import path
from .views import RegisterView,  LoginView ,get_profile, ChangePasswordView, update_profile, ServeAvatarView, DeleteAvatarView, send_otp, verify_otp, reset_password


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path("profile/", get_profile, name="get_profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
    path("profile/update/", update_profile, name="update-profile"),
    path("avatar/<str:file_id>/", ServeAvatarView.as_view(), name="serve_avatar"),
    path("delete-avatar/", DeleteAvatarView.as_view(), name="delete_avatar"),
    path('send-otp/', send_otp, name='send_otp'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('reset-password/', reset_password, name='reset_password'),
]


