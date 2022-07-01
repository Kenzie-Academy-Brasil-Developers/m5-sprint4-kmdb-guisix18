from rest_framework import serializers
from .models import Review


class CriticSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)


class ReviewSerializer(serializers.ModelSerializer):

    critic = CriticSerializer(read_only=True)

    movie_id = serializers.SerializerMethodField()

    def get_movie_id(self, obj):
        return obj.movies.id

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "recomendation",
            "movies",
            "movie_id",
            "critic",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {"movies": {"write_only": True, "required": False}}

    def create(self, validated_data):

        critic = validated_data.pop("critic")
        movie = validated_data.pop("movies")

        reviews = Review.objects.create(**validated_data, movies=movie, critic=critic)

        return reviews
