from rest_framework import routers
from .api import Visualizador

router = routers.DefaultRouter()
router.register('api/proyectos',Visualizador,'Proyectos')

urlpatterns = router.urls