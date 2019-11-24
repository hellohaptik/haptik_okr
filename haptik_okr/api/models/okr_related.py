from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from haptik_okr.api.models import Team


class Sheet(models.Model):
    team_id = models.ForeignKey(Team)
    quarter_name = models.CharField(max_length=100, null=False)
    quarter_start_date = models.DateField()
    quarter_end_date = models.DateField()
    progress = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Objective(models.Model):
    title = models.CharField(max_length=500, null=False)
    quarter_sheet = models.ForeignKey(Sheet)
    progress = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class KeyResults(models.Model):
    title = models.CharField(max_length=500, null=False)
    objective = models.ForeignKey(Objective)
    progress = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)