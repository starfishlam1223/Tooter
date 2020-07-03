from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from .models import Profile

User = get_user_model()

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.user2 = User.objects.create_user(username="test2", password="test")

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