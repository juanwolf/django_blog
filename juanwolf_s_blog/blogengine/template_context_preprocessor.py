from django.contrib.sites.models import Site
from blogengine.models import Category

def get_current_path(request):
    return {
        'current_path': request.build_absolute_uri()
    }


def get_categories(request):
    return {
        'categories': Category.objects.all()
    }

def site_processor(request):
    return {
        'site': request.get_host()
    }
