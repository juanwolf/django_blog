from rest_framework import routers
from api import views

# Creating a default router, to learn more about read :
# http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
router = routers.DefaultRouter()

router.register(r'posts', viewset=views.PostViewSet)
router.register(r'categories', viewset=views.CategoryViewSet)

urlpatterns = router.urls