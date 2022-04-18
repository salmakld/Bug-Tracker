from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status, permissions, filters
from rest_framework.pagination import PageNumberPagination

from .models import Project, Ticket
from .serializers import ProjectSerializer, TicketSerializer, UserSerializer


class ResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 3


class ProjectList(APIView):
    """
    List all projects, or create a new project.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        projects = Project.objects.all()
        projects_serializer = ProjectSerializer(projects, many=True)
        return Response(projects_serializer.data)

    def post(self, request, format=None):
        projects_serializer = ProjectSerializer(data=request.data)
        if projects_serializer.is_valid():
            projects_serializer.save()
            return Response(projects_serializer.data, status=status.HTTP_201_CREATED)
        return Response(projects_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    """
    Retrieve, update or delete a project.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        project_serializer = ProjectSerializer(project)
        return Response(project_serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        project_serializer = ProjectSerializer(project, data=request.data)
        if project_serializer.is_valid():
            project_serializer.save()
            return Response(project_serializer.data)
        return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class TicketList(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering = ['updated_on']
    pagination_class = ResultsSetPagination

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class UserList(ListAPIView):
    filter_backends = [filters.OrderingFilter]
    ordering = ['username']

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

