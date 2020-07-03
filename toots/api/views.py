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

from ..forms import TootForm
from ..models import Toot
from ..serializers import TootSerializer, TootActionSerializer, TootCreateSerializer

# Create your views here.
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_toot_create_view(request, *args, **kwargs):
    serializer = TootCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        obj = serializer.data
        obj["likeCount"] = 0
        return Response(obj, status=201)

    return Response({}, status=400)


@api_view(["GET"])
def api_toot_list_view(request, *args, **kwargs):
    qs = Toot.objects.all()
    username = request.GET.get("username")
    if username != None:
        qs = qs.filter(user__username__iexact=username)
    serializer = TootSerializer(qs, many=True)
    return Response(serializer.data, status=200)


@api_view(["GET"])
def api_toot_detail_view(request, toot_id, *args, **kwargs):
    qs = Toot.objects.filter(id=toot_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = TootSerializer(obj)
    return Response(serializer.data, status=200)


@api_view(["DELETE", "POST"])
@permission_classes([IsAuthenticated])
def api_toot_delete_view(request, toot_id, *args, **kwargs):
    qs = Toot.objects.filter(id=toot_id)
    if not qs.exists():
        return Response({"message": "This toot does not exist"}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message": "The toot does not blongs to you"}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Successfully deleted the toot"}, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_toot_action_view(request, *args, **kwargs):
    serializer = TootActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        toot_id = data.get("id")
        action = data.get("action")
        content = data.get("content")

    qs = Toot.objects.filter(id=toot_id)
    if not qs.exists():
        return Response({"message": "This toot does not exist"}, status=404)
    obj = qs.first()

    if action == "like":
        obj.likes.add(request.user)
        serializer = TootSerializer(obj)
        return Response(serializer.data, status=200)
    elif action == "unlike":
        obj.likes.remove(request.user)
        serializer = TootSerializer(obj)
        return Response(serializer.data, status=200)
    elif action == "retoot":
        new_toot = Toot.objects.create(user=request.user, parent=obj, content=content)
        serializer = TootSerializer(new_toot)
        return Response(serializer.data, status=201)