from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("users/login/", obtain_auth_token),
    path("users/", views.ListUserView.as_view()),
    path("users/register/", views.RegisterUserView.as_view()),
    path("users/<user_id>/", views.RetrieveUpdateDestroyUserProfile.as_view()),
]
