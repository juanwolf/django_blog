from rest_framework import viewsets

from api import serializers
from blogengine import models


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple viewset to retrieve all the posts of blog.juanwolf.fr.
    """
    queryset = models.Post.objects.all().select_related('category').prefetch_related('tags')
    serializer_class = serializers.PostSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple viewset to retrieve all the posts of blog.juanwolf.fr.
    """
    queryset = models.Category.objects.all().prefetch_related('post_set', 'post_set__tags')
    serializer_class = serializers.CategorySerializer
