from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    people = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    hlink = models.TextField()
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