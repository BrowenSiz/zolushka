from django.contrib import admin
from .models import PortfolioCategory, PortfolioProject, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    verbose_name = "Фотография 'ПОСЛЕ'"
    verbose_name_plural = "Галерея фотографий 'ПОСЛЕ'"

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_completed', 'order', 'is_visible')
    list_filter = ('category',)
    list_editable = ('order', 'is_visible')
    search_fields = ('title',)
    inlines = [ProjectImageInline]
    view_on_site = True
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'preview_image', 'order', 'is_visible')
        }),
        ('Описание и статистика', {
            'fields': ('short_description', 'date_completed', ('area', 'time_spent', 'team_size'))
        }),
        ('Слайдер "До/После"', {
            'fields': ('image_before',)
        }),
    )