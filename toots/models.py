from django.conf import settings
from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class TootLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    toot = models.ForeignKey("Toot", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
class TootQuerySet(models.QuerySet):
    def feed(self, user):
        followees_exists = user.following_users.exists()

        followee_id=[]
        if followees_exists:
            followee_id = user.following_users.vales_list("user__id", flat=True)

        return self.filter(Q(user__id__in=followee_id) | Q(user=user)).distinct().order_by("-timestamp")

class TootManager(models.Manager):
    def get_query_set(self, *args, **kwargs):
        return TootQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_query_set().feed(user)

class Toot(models.Model):
    # id = models.AutoField(primary_key=true)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="toots")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="children")
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="liked_toots", blank=True, through=TootLike)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TootManager()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        if (self.content):
            return self.content
        return "NULL CONTENT"

    @property
    def is_retoot(self):
        return self.parent != None