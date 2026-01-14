# estructura (MODELO)python a (OBJETO)json / (UserViewSet)
from rest_framework import serializers
from .models import Proyecto

class ProyectoSerializer(serializers. ModelSerializer):
    class Meta:
        model = Proyecto
        #para consultas
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('create_at', )