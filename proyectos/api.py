from .models import Proyecto
from rest_framework import viewsets, permissions
from .serializers import Serializador

class Visualizador(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Serializador