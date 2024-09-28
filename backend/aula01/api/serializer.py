from rest_framework import serializers
from .models import Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
class LivroCustomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    titulo = serializers.CharField(max_length=100, required=False)
    autor = serializers.CharField(max_length=100, required=False)
    publicado_em = serializers.DateField(required=False)