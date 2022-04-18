from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project, Ticket


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    # tickets = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email'] #, 'projects', 'tickets']