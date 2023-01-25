"""
models
"""
from django.db import models


# Create your models here.


class New(models.Model):
    """
    new in news
    """
    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self):
        """
        str
        :return:
        """
        return self.title[:10]
