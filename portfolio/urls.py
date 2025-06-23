from django.urls import path
from .views import ProjectListAPIView, SkillListAPIView, ServiceListAPIView, project_detail

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('skills/', SkillListAPIView.as_view(), name='skill-list'),
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('project/<slug:slug>/', project_detail, name='project_detail'),
]
