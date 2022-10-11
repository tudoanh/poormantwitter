from rest_framework import serializers
from twitter.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ("id", "author", "content", "created")

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['created'] = instance.created.strftime("%Y-%m-%d %H:%M:%S")
        return rep
