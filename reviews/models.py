from django.db import models
from django.conf import settings

# Create your models here.


class Comment(models.Model):
    # review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
