from functools import partial
from django.shortcuts import render

from rest_framework.views import APIView, Response, status
from rest_framework.authentication import TokenAuthentication

from movie.models import Movie

from .permission import CustomPermission

from .serializer import MovieSerializer
from movie import serializer

# Create your views here.
class MovieView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomPermission]

    def post(self, request):

        serializer = MovieSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)


class MoviewByIDView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomPermission]

    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            serializer = MovieSerializer(movie)

            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(
                {"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)

            serializer = MovieSerializer(movie, request.data, partial=True)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response(serializer.data)

        except Movie.DoesNotExist:
            return Response(
                {"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(
                {"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )
