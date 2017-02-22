from django.contrib import admin
from .models import Meme


class MemeModelAdmin(admin.ModelAdmin):
    list_display = ["username", "creation_date"]
    list_display_links = ["username", "creation_date"]
    list_filter = ["creation_date"]
    search_fields = ["username", "creation_date"]

    class Meta:
        model = Meme

admin.site.register(Meme, MemeModelAdmin)
