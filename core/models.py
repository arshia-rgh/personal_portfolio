from django.db import models
from django.utils import timezone
from utils.base_model import BaseModel


class Skill(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="media/skills/", blank=True, null=True)
    priority = models.IntegerField()

    class Meta:
        ordering = ["priority"]

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


class JobExperience(BaseModel):
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(default=None, blank=True, null=True)

    class Meta:
        ordering = ["-start_date"]

    @property
    def years_of_experience(self):
        if self.end_date:
            return self.end_date.year - self.start_date.year
        return 0

    def __str__(self):
        return f"{self.company_name} {self.position}"


class Education(BaseModel):
    university_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(default=None, blank=True, null=True)

    def save(self, **kwargs):
        if self.end_date is None:
            self.end_date = timezone.now()
        super().save(**kwargs)

    def __str__(self):
        return f"{self.university_name} {self.degree}"


class Interest(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Certificate(BaseModel):
    name = models.CharField(max_length=200)
    certificate_link = models.URLField("link", blank=True, null=True)

    def __str__(self):
        return self.name
