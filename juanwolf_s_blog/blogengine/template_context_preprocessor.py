def get_current_path(request):
    return {
       'current_path': request.build_absolute_uri()
     }