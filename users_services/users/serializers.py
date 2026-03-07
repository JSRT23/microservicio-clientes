from rest_framework import serializers
from .models import User, Empleado

# Este es el traductor para el modelo User que ya estaba
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Este es el nuevo traductor para tu modelo Empleado
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'