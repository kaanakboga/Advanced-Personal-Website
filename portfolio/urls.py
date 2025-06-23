from django.urls import path
from .views import (
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    SkillListCreateAPIView,
    SkillRetrieveUpdateDestroyAPIView,
    ServiceListCreateAPIView,
    ServiceRetrieveUpdateDestroyAPIView,
    project_detail
)

urlpatterns = [
    # Project CRUD
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:id>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail-update-delete'),

    # Skill CRUD
    path('skills/', SkillListCreateAPIView.as_view(), name='skill-list-create'),
    path('skills/<int:id>/', SkillRetrieveUpdateDestroyAPIView.as_view(), name='skill-detail-update-delete'),

    # Service CRUD
    path('services/', ServiceListCreateAPIView.as_view(), name='service-list-create'),
    path('services/<int:id>/', ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service-detail-update-delete'),

    # HTML Detay Sayfa
    path('project/<slug:slug>/', project_detail, name='project_detail'),
]
