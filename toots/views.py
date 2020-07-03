import random
from django.conf import settings
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

from .forms import TootForm
from .models import Toot
from .serializers import TootSerializer, TootActionSerializer, TootCreateSerializer

# Create your views here.

def toot_list_view(request, *args, **kwargs):
    return render(request, "toots/list.html", context={}, status=200)

def toot_detail_view(request, toot_id, *args, **kwargs):
    return render(request, "toots/detail.html", context={"toot_id": toot_id}, status=200)

def toot_profile_view(request, username, *args, **kwargs):
    return render(request, "toots/profile.html", context={"profile_username": username}, status=200)

def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)