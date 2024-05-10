from django.conf import settings
from django.db import models
from django.utils import timezone
#removed all extraneous functions and put all fields under a single model to improve access to id field

class Sheet(models.Model):
    """Takes all the data from the other classes to produce a sheet"""
    last_saved = models.DateTimeField(blank=True, null=True)
    character_name = models.TextField(unique=True)
    level = models.SmallIntegerField()
    armor_class = models.SmallIntegerField()
    initiative = models.SmallIntegerField()
    hit_points = models.SmallIntegerField()
    conditions = models.TextField(blank=True,null=True)
    inspiration = models.BooleanField()
    inventory = models.TextField()
    spells = models.TextField(blank=True,null=True)
    speed = models.TextField()
    defenses = models.TextField()
    features = models.TextField()
    traits = models.TextField()
    proficiencies = models.TextField()
    proficiency_value = models.SmallIntegerField() #should this be generated instead? or will it generate every time the sheet is pulled up, overriding the player's settings?
    languages = models.TextField()
    description = models.TextField(blank=True,null=True)
    notes = models.TextField(blank=True,null=True)
    skill_entry = models.TextField()
    strength_score = models.SmallIntegerField()
    dexterity_score = models.SmallIntegerField()
    constitution_score = models.SmallIntegerField()
    intelligence_score = models.SmallIntegerField()
    wisdom_score = models.SmallIntegerField()
    charisma_score = models.SmallIntegerField()

    def publish(self):
        self.last_saved = timezone.now()
        self.save()

    def __str__(self):
        return self.character_name