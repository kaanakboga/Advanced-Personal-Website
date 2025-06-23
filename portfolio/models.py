from django.db import models

ICON_CHOICES = [
    ('fa-code', 'Code'),
    ('fa-database', 'Database'),
    ('fa-gamepad', 'Gamepad'),
    ('fa-paint-brush', 'Design'),
    ('fa-robot', 'AI/Robot'),
    ('fa-lock', 'Cybersecurity'),
    ('fa-mobile-alt', 'Mobile'),
    ('fa-globe', 'Web'),
]

class Project(models.Model):
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='fa-code')
    title = models.CharField(max_length=100)
    creator_name = models.CharField(max_length=100, default="Unknown")
    date_range = models.CharField(max_length=50, default="June 2025")
    tools_used = models.CharField(max_length=200, default="Django, Bootstrap")
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()  # Yüzde değeri (0-100 arası)

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='fa-code')  # İkon seçimi ekledim

    def __str__(self):
        return self.title
