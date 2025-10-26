from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone')
    readonly_fields = ('name', 'phone', 'message', 'created_at')
    list_per_page = 20

    def has_add_permission(self, request):
        return False # Запрещаем создавать заявки из админки