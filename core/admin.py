from django.contrib import admin

from core.models import Skill, Project


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
