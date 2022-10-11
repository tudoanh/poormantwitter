from django.test import TestCase

from twitter.models import Tweet
from rest_framework.test import APIClient

client = APIClient()


class TweetTestCase(TestCase):
    """Test tweet CRUD with API endpoints"""

    def test_tweet_create(self):
        """Test tweet creation"""
        client.post("/tweets/", {"author": "god", "content": "test"})
        self.assertEqual(Tweet.objects.count(), 1)
        self.assertEqual(Tweet.objects.first().author, "god")
        self.assertEqual(Tweet.objects.first().content, "test")

    def test_tweet_list(self):
        """Test tweet list"""
        client.post("/tweets/", {"author": "god", "content": "protect"})
        client.post("/tweets/", {"author": "devil", "content": "chaos"})
        client.post("/tweets/", {"author": "human", "content": "pure"})
        response = client.get("/tweets/")
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["author"], "human")
        self.assertEqual(response.data[0]["content"], "pure")

    def test_tweet_retrieve(self):
        """Test tweet retrieve"""
        client.post("/tweets/", {"author": "god", "content": "protect"})
        client.post("/tweets/", {"author": "devil", "content": "chaos"})
        client.post("/tweets/", {"author": "human", "content": "pure"})
        response = client.get("/tweets/1/")
        self.assertEqual(response.data["author"], "god")
        self.assertEqual(response.data["content"], "protect")
