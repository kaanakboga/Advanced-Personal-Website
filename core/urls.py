from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
]

