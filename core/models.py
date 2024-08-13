from django.db import models

from utils.base_model import BaseModel


class Skill(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="media/skills/", blank=True, null=True)

    def __str__(self):
        return self.name


class Project(BaseModel):
    class ProjectStatusChoices(models.TextChoices):
        Ongoing = ("Ongoing", "Ongoing")
        Completed = ("Completed", "Completed")
        OnHold = ("OnHold", "OnHold")

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    source_link = models.URLField()
    live_link = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=ProjectStatusChoices.choices)

    def __str__(self):
        return self.name


# class JobExperience(BaseModel):
#     pass
#
#
# class Education(BaseModel):
#     pass
#
#
# class Interest(BaseModel):
#     pass
#
#
# class Certificate(BaseModel):
#     pass
