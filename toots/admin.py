from django.contrib import admin

# Register your models here.
from .models import Toot, TootLike

class TootLikeAdmin(admin.TabularInline):
    model = TootLike

class TootAdmin(admin.ModelAdmin):
    inlines = [TootLikeAdmin]
    list_display = ["id", "__str__", "user"]
    search_fields = ["user__username", "user__email", "content"]

    class Meta:
        model = Toot

admin.site.register(Toot, TootAdmin)