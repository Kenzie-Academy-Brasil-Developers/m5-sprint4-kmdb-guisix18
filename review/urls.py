from django.urls import path

from . import views

urlpatterns = [
    path("movies/<int:movie_id>/reviews/", views.CreateReviewView.as_view()),
    path("reviews/<int:review_id>/", views.DeleteReviewView.as_view()),
    path("reviews/", views.ListAllReviewsView.as_view()),
]
