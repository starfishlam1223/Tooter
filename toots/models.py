from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class TootLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    toot = models.ForeignKey("Toot", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
class Toot(models.Model):
    # id = models.AutoField(primary_key=true)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="liked_user", blank=True, through=TootLike)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        if (self.content):
            return self.content
        return "NULL CONTENT"

    @property
    def is_retoot(self):
        return self.parent != None