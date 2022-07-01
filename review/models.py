from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class ReviewsChoices(models.TextChoices):
    MUST_WATCH = ("MW", "Must Watch")
    SHOULD_WATCH = ("SW", "Should Watch")
    AVOID_WATCH = ("AW", "Avoit Watch")
    NO_OPINION = ("NO", "No opinion")


class Review(models.Model):
    stars = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(
        max_length=50, choices=ReviewsChoices.choices, default=ReviewsChoices.NO_OPINION
    )
    movies = models.ForeignKey(
        "movie.Movie", on_delete=models.CASCADE, related_name="movies_reviews"
    )
    critic = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="users_reviews"
    )
