from django.contrib import admin
from django import forms
from .models import Service, ServiceChecklistItem, AdditionalServiceCategory, AdditionalServiceItem
from django_select2.forms import Select2Widget

ICON_CHOICES = [
    ('', '---------'),
    ('cleaning_services', 'Веник и совок'), ('construction', 'Инструменты'),
    ('diamond', 'Бриллиант'), ('house', 'Дом'), ('cottage', 'Коттедж'),
    ('apartment', 'Квартира'), ('window', 'Окно'), ('chair', 'Кресло'),
    ('bug_report', 'Жук'), ('eco', 'Экология'), ('health_and_safety', 'Безопасность'),
]

class ServiceAdminForm(forms.ModelForm):
    icon_selector = forms.ChoiceField(
        choices=ICON_CHOICES,
        label="Выберите иконку",
        required=False
    )

    class Meta:
        model = Service
        exclude = ['icon']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['icon_selector'].initial = self.instance.icon

class ServiceChecklistItemInline(admin.TabularInline):
    model = ServiceChecklistItem
    extra = 1
    verbose_name = "Пункт чек-листа"
    verbose_name_plural = "Пункты чек-листа"

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ('title', 'order', 'is_visible')
    list_editable = ('order', 'is_visible')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    inlines = [ServiceChecklistItemInline]
    view_on_site = True
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'short_description', 'price_display', 'icon_selector', 'order', 'is_visible')
        }),
        ('Контент для страницы услуги', {
            'fields': ('hero_image', 'full_description')
        }),
        ('SEO-настройки', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description')
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.icon = form.cleaned_data['icon_selector']
        super().save_model(request, obj, form, change)

class AdditionalServiceItemInline(admin.TabularInline):
    model = AdditionalServiceItem
    extra = 1

@admin.register(AdditionalServiceCategory)
class AdditionalServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    inlines = [AdditionalServiceItemInline]