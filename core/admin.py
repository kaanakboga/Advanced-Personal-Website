from django.contrib import admin
from .models import CorsAllowedOrigin
from .models import CV

admin.site.register(CorsAllowedOrigin)

from django.contrib import admin

admin.site.register(CV)

