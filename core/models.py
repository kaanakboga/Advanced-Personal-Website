from django.db import models

class CorsAllowedOrigin(models.Model):
    domain = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.domain

class CV(models.Model):
    file = models.FileField(upload_to='cv/')

    def __str__(self):
        return f"CV - {self.file.name}"