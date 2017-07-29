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
    arxiv = models.CharField(max_length=200, null=True, blank=True)
    arxivlink = models.TextField(null=True, blank=True)
    journal = models.CharField(max_length=200, null=True, blank=True)
    hyperlink = models.TextField(null=True, blank=True)
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

class People(models.Model):
    """Model definition for People."""
    POSITION_CHOICES = (
        ('Undergraduate', 'Undergraduate'),
        ('Graduate', 'Graduate'),
        ('Post-Doc', 'Post-Doc'),
        ('Professor', 'Professor'),
        ('Research Professor', 'Research Professor'),
        ('Alumni', 'Alumni')
    )

    # TODO: Define fields here
    position = models.CharField(max_length=30, choices=POSITION_CHOICES)
    index = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    link = models.TextField(null=True, blank=True)
    img = models.TextField(null=True, blank=True)
    

    class Meta:
        """Meta definition for People."""

        verbose_name = 'People'
        verbose_name_plural = 'Peoples'

    def __unicode__(self):
        """Unicode representation of People."""
        pass

    def __str__(self):
        return self.name

class Seminar(models.Model):
    """Model definition for Seminar."""

    # TODO: Define fields here
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    date_start = models.CharField(max_length=50)
    date_end = models.CharField(max_length=50, null=True, blank=True)
    place = models.CharField(max_length=50)
    lecturer = models.CharField(max_length=100)
    ref = models.CharField(max_length=200, null=True, blank=True)
    ref_link = models.TextField(null=True, blank=True)
    topic = models.TextField(null=True, blank=True)
    schedule = models.TextField()
    note = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    class Meta:
        """Meta definition for Seminar."""

        verbose_name = 'Seminar'
        verbose_name_plural = 'Seminars'

    def __unicode__(self):
        """Unicode representation of Seminar."""
        pass
