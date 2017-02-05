from rest_framework import serializers
from blogengine import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = "__all__"
        depth = 2


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        depth = 2
        fields = ['name_fr', 'name_en', 'description_en', 'description_fr', 'slug_fr', 'slug_en', 'post_set']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = "__all__"
