from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

from .models import Toot

# Create your tests here.
User = get_user_model()


class TootTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.user2 = User.objects.create_user(username="test2", password="test")

        Toot.objects.create(content="my toot", user=self.user)
        Toot.objects.create(content="my toot", user=self.user)
        Toot.objects.create(content="my toot", user=self.user2)
        Toot.objects.create(content="my toot", user=self.user2)

    def test_user_created(self):
        self.assertEqual(self.user.username, "test")

    def test_toot_created(self):
        toot = Toot.objects.create(content="my toot", user=self.user)
        self.assertEqual(toot.id, 5)
        self.assertEqual(toot.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password="test")
        return client

    def test_toot_create_api(self):
        client = self.get_client()
        data = {
            "content": "api test"
        }
        response = client.post("/api/toots/create/", data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get("id"), 5)

    def test_toot_detail_api(self):
        client = self.get_client()
        response = client.get("/api/toots/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("id"), 1)

    def test_toot_delete_api(self):
        client = self.get_client()
        response = client.delete("/api/toots/delete/1/")
        self.assertEqual(response.status_code, 200)
        response = client.delete("/api/toots/delete/1/")
        self.assertEqual(response.status_code, 404)
        response = client.delete("/api/toots/delete/3/")
        self.assertEqual(response.status_code, 401)

    def test_toot_list(self):
        client = self.get_client()
        response = client.get("/api/toots/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)

    def test_related_name(self):
        user = self.user
        self.assertEqual(user.toots.count(), 2)

    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/toots/action/", {"id": 1, "action": "like"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("likeCount"), 1)
        user = self.user
        liked_toots = user.tootlike_set.count()
        self.assertEqual(liked_toots, 1)
        liked_toots = user.liked_toots.count()
        self.assertEqual(liked_toots, 1)


    def test_action_unlike(self):
        client = self.get_client()
        response = client.post("/api/toots/action/", {"id": 2, "action": "like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/toots/action/", {"id": 2, "action": "unlike"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("likeCount"), 0)

    def test_action_retoot(self):
        client = self.get_client()
        response = client.post("/api/toots/action/", {"id": 1, "action": "retoot"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get("id"), 5)
        self.assertEqual(response.json().get("parent").get("id"), 1)