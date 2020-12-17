from rest_framework import serializers
from .models import Radio, Post

"""
    serializers are like CBF forms
        - GET request
        - POST request: check if the data is valid and then preform the correct 
               manipulation
"""


class RadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radio
        fields = [
            'name', 'tagline', 'language',
            'category', 'color', 'description',
            'url', 'icon', 'image',
            'isDisliked', 'order',
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'desc', 'author']
