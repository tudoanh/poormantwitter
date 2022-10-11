from rest_framework import routers

from .api.views import TweetViewSet

router = routers.DefaultRouter()

router.register(r'tweets', TweetViewSet)


urlpatterns = router.urls
