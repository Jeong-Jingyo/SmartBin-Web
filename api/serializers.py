from rest_framework import serializers
from .models import Door, Trash


class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trash
        fields = ["feedback_type", "feedback_foreign_subst"]


class TerminateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["terminate"]
