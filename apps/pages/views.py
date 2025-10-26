from django.shortcuts import render
from .models import Review, FAQ
from apps.services.models import Service
from apps.portfolio.models import PortfolioProject
from django.http import JsonResponse
from apps.feedback.models import ServiceRequest
import json

def homepage_view(request):
    services = Service.objects.filter(is_visible=True)[:4] 
    portfolio_items = PortfolioProject.objects.filter(is_visible=True)[:3] 
    
    context = {
        'services': services,
        'portfolio_items': portfolio_items,
    }
    return render(request, 'pages/index.html', context)

def about_view(request):
    return render(request, 'pages/about.html')

def reviews_view(request):
    reviews = Review.objects.filter(is_published=True)
    context = {
        'reviews': reviews,
    }
    return render(request, 'pages/reviews.html', context)

def submit_form_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        
        message_parts = []
        for key, value in data.items():
            if key not in ['name', 'phone', 'csrfmiddlewaretoken']:
                message_parts.append(f"{key}: {value}")
        
        message = "\n".join(message_parts)

        ServiceRequest.objects.create(
            name=data.get('name', 'Не указано'),
            phone=data.get('phone'),
            message=message
        )
        
        return JsonResponse({'success': True, 'message': 'Спасибо! Ваша заявка отправлена.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})