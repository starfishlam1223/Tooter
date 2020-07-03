from django.shortcuts import render, redirect

# Create your views here.

def toot_list_view(request, *args, **kwargs):
    return render(request, "toots/list.html", context={}, status=200)

def toot_detail_view(request, toot_id, *args, **kwargs):
    return render(request, "toots/detail.html", context={"toot_id": toot_id}, status=200)