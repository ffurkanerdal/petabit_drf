from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserCreateView, LoginView, UserListAPIView, LogoutView, WhoAuthenticate

urlpatterns = [
    path("login/", LoginView.as_view(), name="user-login"),
    path("register/", UserCreateView.as_view(), name="user-create"),
    path("users/", UserListAPIView.as_view(), name="users"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("who/", WhoAuthenticate.as_view(), name="who")
]
