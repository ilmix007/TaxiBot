from django.contrib import admin

from coreapp.models import Bot


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('name', 'token')

