from django.urls import path

from . import views

urlpatterns = [
    path("users/register/", views.UserView.as_view()),
    path("users/login/", views.UserLoginView.as_view()),
    path("users/", views.ListUserView.as_view()),
    path("users/<int:user_id>/", views.ListUserByIdView.as_view()),
]
