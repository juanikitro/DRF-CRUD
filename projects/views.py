from .models import Project
from .serializers import ProjectSerializer
from rest_framework import viewsets, permissions


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
