from django.urls import URLPattern, path
from .views import ProjectList, ProjectDetail, TicketList, TicketDetail, UserList, UserDetail

urlpatterns = [
    path('projects/', ProjectList.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('tickets/', TicketList.as_view()),
    path('tickets/<int:pk>', TicketDetail.as_view()),
    path('users/', UserList.as_view()),
    path('tickets/<int:pk>', UserDetail.as_view()),


]