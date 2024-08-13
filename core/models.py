from utils.base_model import BaseModel
from django.db import models


class Skill(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="media/skills/", blank=True, null=True)

    def __str__(self):
        return self.name


class Project(BaseModel):
    pass


class JobExperience(BaseModel):
    pass


class Education(BaseModel):
    pass


class Interest(BaseModel):
    pass


class Certificate(BaseModel):
    pass
