from rest_framework import serializers
from .models import Murojaat

class MurojaatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Murojaat
        fields = ['id', 'subject', 'status', 'is_read', 'answer', 'created_at', 'updated_at']
