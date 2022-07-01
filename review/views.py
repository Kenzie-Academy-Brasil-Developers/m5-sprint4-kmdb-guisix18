from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Response, status
from rest_framework.pagination import PageNumberPagination
from movie.models import Movie
from .models import Review
from .serializer import ReviewSerializer

from movie.permission import CustomPermission
from .permission import AuthReview, AuthDeleteReview
from review import serializer

# Create your views here.
class CreateReviewView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AuthReview]

    def post(self, request, movie_id):
        find_movie = get_object_or_404(Movie, pk=movie_id)
        serializer = ReviewSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(movies=find_movie, critic=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, movie_id):
        find_movie = get_object_or_404(Movie, pk=movie_id)
        movies_reviews = Review.objects.filter(movies=movie_id)

        result_page = self.paginate_queryset(movies_reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class DeleteReviewView(APIView):
    permission_classes = [AuthDeleteReview]
    authentication_classes = [TokenAuthentication]

    def delete(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)

        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ListAllReviewsView(APIView, PageNumberPagination):
    def get(self, request):
        reviews = Review.objects.all()

        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
