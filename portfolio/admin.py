from django.contrib import admin
from .models import Project, Skill, Service  # Service'i eklediğine emin ol

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator_name', 'date_range')
    list_filter = ('date_range',)
    search_fields = ('title', 'creator_name', 'tools_used')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')
    search_fields = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
    search_fields = ('title',)
