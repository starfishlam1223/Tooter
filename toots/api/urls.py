"""tooter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import (
    api_toot_action_view,
    api_toot_delete_view,
    api_toot_detail_view,
    api_toot_list_view,
    api_toot_feed_view,
    api_toot_create_view,
)

urlpatterns = [
    path("", api_toot_list_view),
    path("feed/", api_toot_feed_view),
    path("action/", api_toot_action_view),
    path("create/", api_toot_create_view),
    path("delete/<int:toot_id>/", api_toot_delete_view),
    path("<int:toot_id>/", api_toot_detail_view),
]
