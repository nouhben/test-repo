from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Radio(models.Model):
    LANGUAGES = [
        ('Eng', 'English'),
        ('Ar', 'Arabic'),
        ('Fr', 'French'),
        ('Hindi', 'Hindi'),
        ('Ch', 'Chineese'),
    ]
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    language = models.CharField(max_length=200, choices=LANGUAGES)
    category = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    icon = models.URLField()
    image = models.URLField()
    isDisliked = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.name}: {self.tagline}'


class RadioOwner(models.Model):
    owner = models.ForeignKey(Radio, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
