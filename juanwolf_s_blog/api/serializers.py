from rest_framework import serializers
from blogengine import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
