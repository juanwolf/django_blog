from rest_framework import viewsets

from api import serializers
from blogengine import models


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple viewset to retrieve all the posts of blog.juanwolf.fr.
    """
    queryset = models.Post.objects.all().select_related('category').prefetch_related('tags')
    serializer_class = serializers.PostSerializer
