from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from api.models import Team


class Quarter(models.Model):
    quarter_name = models.CharField(max_length=100, null=False)
    quarter_start_date = models.DateField()
    quarter_end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Sheet(models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.PROTECT)
    quarter_id = models.ForeignKey(Quarter, on_delete=models.PROTECT)
    progress = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Objective(models.Model):
    title = models.CharField(max_length=500, null=False)
    quarter_sheet = models.ForeignKey(Sheet, on_delete=models.PROTECT)
    progress = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class KeyResults(models.Model):
    title = models.CharField(max_length=500, null=False)
    objective = models.ForeignKey(Objective, on_delete=models.PROTECT)
    progress = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
