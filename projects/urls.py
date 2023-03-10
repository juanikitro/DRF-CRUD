from rest_framework import routers
from .views import ProjectViewSet

router = routers.DefaultRouter()

router.register("api/projects", ProjectViewSet)

urlpatterns = router.urls
