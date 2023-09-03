from django.contrib import admin

from coreapp.models import Bot, CustomUser


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('name', 'token')


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'in_waiting', 'on_the_route',
                    'last_updated', 'location')
    list_filter = ('in_waiting', 'on_the_route')
