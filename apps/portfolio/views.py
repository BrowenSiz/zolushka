from django.shortcuts import render
from .models import PortfolioProject, PortfolioCategory
from django.http import JsonResponse

def portfolio_list_view(request):
    projects = PortfolioProject.objects.filter(is_visible=True)
    categories = PortfolioCategory.objects.all()
    context = {
        'projects': projects,
        'categories': categories,
    }
    return render(request, 'portfolio/list.html', context)

def portfolio_detail_json_view(request, pk):
    try:
        project = PortfolioProject.objects.get(pk=pk)
        after_images = [image.image.url for image in project.after_images.all()]

        data = {
            'title': project.title,
            'short_description': project.short_description,
            'image_before_url': project.image_before.url,
            'after_images_urls': after_images,
            'area': project.area,
            'time_spent': project.time_spent,
            'team_size': project.team_size,
        }
        return JsonResponse(data)
    except PortfolioProject.DoesNotExist:
        return JsonResponse({'error': 'Project not found'}, status=404)