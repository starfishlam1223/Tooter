import random
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.http import is_safe_url

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response

from ..models import Profile

User = get_user_model()

# Create your views here.
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def api_user_follow_view(request, username, *args, **kwargs):
    follower = request.user
    followee_qs = User.objects.filter(username=username)

    if not followee_qs.exists():
        return Response({}, status=400)

    followee = followee_qs.first()
    followee_profile = followee.profile

    data = {}
    if request.method == "GET":
        data = request.GET
    elif request.method == "POST":
        data = request.data

    action = data.get("action")

    print(request.data)
    print(request.GET)


    if action == "unfollow":
        followee_profile.followers.remove(follower)
    elif action == "follow":
        followee_profile.followers.add(follower)

    return Response({"count": followee_profile.followers.all().count()}, status=200)