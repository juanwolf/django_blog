from django.contrib.sites.models import Site


def get_current_path(request):
    return {
        'current_path': request.build_absolute_uri()
    }


def site_processor(request):
    return {
        'site': Site.objects.get_current()
    }