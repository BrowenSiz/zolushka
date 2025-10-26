from django.shortcuts import render, get_object_or_404
from .models import Service, AdditionalServiceCategory

def service_list_view(request):
    main_services = Service.objects.filter(is_visible=True)
    additional_categories = AdditionalServiceCategory.objects.all()
    context = {
        'main_services': main_services,
        'additional_categories': additional_categories,
    }
    return render(request, 'services/list.html', context)

def service_detail_view(request, slug):
    service = get_object_or_404(Service, slug=slug, is_visible=True)
    context = {
        'service': service,
    }
    return render(request, 'services/detail.html', context)