from django.conf import settings
from django.db import models
from django.utils import timezone
#documentation states that all fields are editable by default

class Abilities(models.Model):
    ablity = models.CharField(primary_key=True,max_length=12)
    score = models.SmallIntegerField()
    modifier = models.SmallIntegerField()

class Skills(models.Model):
    skill = models.CharField(primary_key=True,max_length=17)
    base_score = models.SmallIntegerField()
    prof = models.SmallIntegerField()
    abl = models.SmallIntegerField()
    skill_score = models.SmallIntegerField()

class Player_Entry(models.Model):
    character_name = models.TextField(primary_key=True)
    armor_class = models.SmallIntegerField()
    initiative = models.SmallIntegerField()
    hit_points = models.SmallIntegerField()
    conditions = models.TextField(null=True)
    inspiration = models.BooleanField()
    inventory = models.TextField()
    spells = models.TextField(null=True)
    speed = models.TextField()
    defenses = models.TextField()
    features = models.TextField()
    traits = models.TextField()
    proficiencies = models.TextField()
    languages = models.TextField()
    description = models.TextField(null=True)
    notes = models.TextField(null=True)