from rest_framework import routers
from .api import ProyectoViewSet

router = routers.DefaultRouter()
#ruta/conjuntodat/nombrerut
router.register('api/proyecto', ProyectoViewSet, 'proyecto')

urlpatterns = router.urls #genera url
