from django.db import models

# Create your models here.
class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(max_length=50)
    movies = models.ForeignKey(
        "movie.Movie", on_delete=models.CASCADE, related_name="movies_reviews"
    )
    users = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="users_reviews"
    )
