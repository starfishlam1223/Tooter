from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

# Create your tests here.
User = get_user_model()


# Create your tests here.
from .models import Profile

User = get_user_model()

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.user2 = User.objects.create_user(username="test2", password="test")

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password="test")
        return client

    def test_profile_created(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_following(self):
        fst = self.user
        snd = self.user2

        fst.profile.followers.add(snd)

        qs = snd.following_users.filter(user=fst)
        self.assertTrue(qs.exists())
        qs = fst.following_users.all()
        self.assertFalse(qs.exists())

    def test_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(
            f"/api/profiles/follow/{self.user2.username}/",
            {"action": "follow"}
        )
        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count, 1)

    def test_unfollow_api_endpoint(self):
        fst = self.user
        snd = self.user2
        fst.profile.followers.add(snd)

        client = self.get_client()
        response = client.post(
            f"/api/profiles/follow/{self.user2.username}/",
            {"action": "unfollow"}
        )
        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count, 0)

    def test_cannot_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(
            f"/api/profiles/follow/{self.user.username}/",
            {"action": "follow"}
        )
        r_data = response.json()
        count = r_data.get("count")
        self.assertEqual(count, 0)