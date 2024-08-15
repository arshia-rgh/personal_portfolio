from django.contrib import admin

from core.models import Skill, Project, JobExperience


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(JobExperience)
class JobExperienceAdmin(admin.ModelAdmin):
    pass
