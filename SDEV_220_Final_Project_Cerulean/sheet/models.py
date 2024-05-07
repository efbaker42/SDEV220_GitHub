from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import F
from django.db.models import Value

#import model form 
from django.forms import ModelForm

import random
import math #previously imported them within the func so it would work right, but it would be best to import these once if possible
#documentation states that all fields are editable by default
#instead of importing defs from DiceRollFuncs, I'm copying and pasting them into the relevant class
#so I can see the variables and troubleshoot without flipping back and forth between files

#put Player_Entry first because players will enter character name, level, and other traits first
class Player_Entry(models.Model):
    """Everything I didn't create a function for, which will be entered by the player as they tease out what their character's class and race needs"""
    character_name = models.TextField(primary_key=True)
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

    def proficiency(level):
        """calculates proficiency"""
        #import math
        proficiency_value = math.ceil(level/4) + 1
        return proficiency_value

class Abilities(models.Model):
    """Define Abilities table; explicitly calculates each ability"""
    strength_score = models.SmallIntegerField()
    @property
    def strength_modifier(self):
        return((self.strength_score-10)//2)
    @property
    def passive_strength(self):
        return(self.strength_modifier+10)
    dexterity_score = models.SmallIntegerField()
    @property
    def dexterity_modifier(self):
        return((self.dexterity_score-10)//2)
    @property
    def passive_dexterity(self):
        return(self.dexterity_modifier+10)
    constitution_score = models.SmallIntegerField()
    @property
    def constitution_modifier(self):
        return((self.constitution_score-10)//2)
    @property
    def passive_constitution(self):
        return(self.constitution_modifier+10)
    intelligence_score = models.SmallIntegerField()
    @property
    def intelligence_modifier(self):
        return((self.intelligence_score-10)//2)
    @property
    def passive_intelligence(self):
        return(self.intelligence_modifier+10)
    wisdom_score = models.SmallIntegerField()
    @property
    def wisdom_modifier(self):
        return((self.wisdom_score-10)//2)
    @property
    def passive_wisdom(self):
        return(self.wisdom_modifier+10)
    charisma_score = models.SmallIntegerField()
    @property
    def charisma_modifier(self):
        return((self.charisma_score-10)//2)
    @property
    def passive_charisma(self):
        return(self.charisma_modifier+10)
    
    #test Abilities in python shell
    def __str__(self):
        return (
            f"Strength score: {self.strength_score}  mod:{self.strength_modifier} passive: {self.passive_strength}\nDexterity score: {self.dexterity_score}  mod:{self.dexterity_modifier} passive: {self.passive_dexterity}\nConstitution score: {self.constitution_score}  mod:{self.constitution_modifier} passive: {self.passive_constitution}\nIntelligence score: {self.intelligence_score}  mod:{self.intelligence_modifier} passive: {self.passive_intelligence}\nWisdom score: {self.wisdom_score}  mod:{self.wisdom_modifier} passive: {self.passive_wisdom}\nCharisma score: {self.charisma_score}  mod:{self.charisma_modifier} passive: {self.passive_charisma}"
            )
    
    def generate_abilities(): #unsure how to populate each row
        """Generate stats for character abilities"""
        #import random
        abl = 0 #holds number of abilities
        abilities = [] #empty list to hold abilities
        while abl < 6:
            roll = 0 #each individual roll
            Rolls = 0 #holds total roll for abilities
            while roll < 3:
                Rolls = Rolls + random.randint(1,6)
                roll += 1
            abl += 1
            abilities.append(Rolls)
        return abilities
    
    def update_mod(abilities): #unsure how to populate each row
        """updates modifier for each ability score"""
        modifiers = []
        for abl in abilities:
            mod = (abl - 10) // 2
            modifiers.append(mod)
        return modifiers
    
    def gen_passive_abilities(modifiers): #unsure how to populate each row
        """adds 10 to each modifier to create passive ability score"""
        passive_abilities = []
        for mod in modifiers:
            pasAbl = mod + 10
            passive_abilities.append(pasAbl)
        return passive_abilities

#should inherit level from Player_Entry; don't want to enter this more than once to reduce errors
class Skills(Player_Entry):
    """Define Skills table"""
    skill = models.CharField(primary_key=True,max_length=17)
    base_score = models.SmallIntegerField()
    prof = models.BooleanField() #either a skill has proficiency or it doesn't; proficiency is calculated in the Player_Entry, because it needs its own space as it is sometimes used for other rolls
    abl = models.SmallIntegerField()
    skill_score = models.SmallIntegerField()

    def roll_base_skill(self,prof,skill_score): #unsure how to populate each row
        """Rolls base skill, which can be overridden by player later"""
        #import random
        if prof == False:
            skill_score = self.base_score + random.randint(1,20)
        else:
            skill_score = self.base_score + Player_Entry.proficiency_value + random.randint(1,20)
        return skill_score

class Sheet(Skills,Abilities):
    """Takes all the data from the other classes to produce a sheet"""
    last_saved = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.last_saved = timezone.now()
        self.save()

    def __str__(self):
        return self.character_name

    def roll_dice():
        """Rolls dice of user's choosing"""
        #import random
        numDice = print(int(input("How many dice do you want to roll? ")))
        sideDice = print(int(input("Which dice do you want to roll? Choose from 4, 6, 8, 10, 20, or 100: ")))
        validDice = [4,6,8,10,20,100]
        finalRoll = 0
        if sideDice not in validDice:
            sideDice = print(int(input("Invalid choice. Choose from 4, 6, 8, 10, 20, or 100: ")))
        while numDice != 0:
            finalRoll = finalRoll + random.randint(1,sideDice)
            numDice -= 1
        return finalRoll
    
    def roll_skill_check():
        """Rolls skill check using user's entries"""
        skill = print(int(input("Enter skill score: "))) #this will come from the db later
        skillRoll = skill + proficiency + random.randint(1,20)
        return skillRoll
    
#Create the class for the form.    
class SheetForm(ModelForm):
    class Meta:
        model = Sheet
        #required to ether use fields or exluce (might be easier just to exlude this field than list all)
        exclude = ('last_saved',)
    