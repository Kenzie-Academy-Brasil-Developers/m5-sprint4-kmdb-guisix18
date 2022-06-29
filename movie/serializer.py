from rest_framework import serializers
from genre.models import Genre

from genre.serializer import GenreSerializer
from movie.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    premiere = serializers.DateField()
    duration = serializers.CharField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    genres = GenreSerializer(many=True)

    def create(self, validated_data):
        genre = []

        for gen in validated_data["genres"]:
            gene, _ = Genre.objects.get_or_create(**gen)
            genre.append(gene)

        del validated_data["genres"]

        new_infos = {**validated_data}

        movie = Movie.objects.create(**new_infos)
        movie.genres.set(genre)

        return movie
