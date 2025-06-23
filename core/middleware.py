from django.utils.deprecation import MiddlewareMixin
from .models import CorsAllowedOrigin

class DynamicCorsMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        allowed_origins = CorsAllowedOrigin.objects.values_list('domain', flat=True)
        origin = request.META.get('HTTP_ORIGIN')

        if origin in allowed_origins:
            response["Access-Control-Allow-Origin"] = origin
            response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Origin, Content-Type, Authorization"

        return response
