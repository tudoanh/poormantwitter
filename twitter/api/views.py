from rest_framework import viewsets
from twitter.models import Tweet

from .serializers import TweetSerializer


class TweetViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.RetrieveModelMixin,
):
    queryset = Tweet.objects.all().order_by("-created")
    serializer_class = TweetSerializer
