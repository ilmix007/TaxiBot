from django.contrib import admin

from taxiapp.models import Driver, Customer


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'loc', 'in_waiting', 'on_the_route')
    list_filter = ('user__in_waiting', 'user__on_the_route')
    raw_id_fields = ('user',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'loc', 'in_waiting', 'on_the_route')
    list_filter = ('user__in_waiting', 'user__on_the_route')
    raw_id_fields = ('user',)
