from rest_framework import viewsets
from twitter.models import Tweet

from .serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
