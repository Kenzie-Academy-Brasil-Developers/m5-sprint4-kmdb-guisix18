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

    def update(self, instance: Movie, validated_data: dict):
        instance.title = validated_data.get("title", instance.title)
        instance.premiere = validated_data.get("premiere", instance.premiere)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.classification = validated_data.get(
            "classification", instance.classification
        )
        instance.synopsis = validated_data.get("synopsis", instance.synopsis)

        all_genres = validated_data.get("genres", instance.genres)

        if all_genres != instance.genres:
            new_genre = []

            for gen in all_genres:
                genre, _ = Genre.objects.get_or_create(**gen)
                new_genre.append(genre)

            instance.genres.set(new_genre)

        instance.save()

        return instance
