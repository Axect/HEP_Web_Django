from django.db import models
from django.utils import timezone
import ast

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    year = models.CharField(max_length=10)
    index = models.CharField(max_length=5)
    people = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    hyperlink = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save

    def __str__(self):
        return self.title
