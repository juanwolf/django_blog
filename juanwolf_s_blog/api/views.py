from rest_framework import viewsets

from api import serializers
from blogengine import models


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple viewset to retrieve all the posts of blog.juanwolf.fr.
    """
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
