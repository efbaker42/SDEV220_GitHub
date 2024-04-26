"""
DiceRollFuncs
Elizabeth Baker
Python 3.12.2 10APR2024
This is a collection of dice rolling functions that will be used in the D&D Character sheet for Cerulean group's final project.
"""
def generate_abilities():
    """Generate stats for character abilities"""
    import random
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

def update_mod(abilities):
    """updates modifier for each ability score"""
    modifiers = []
    for abl in abilities:
        mod = (abl - 10) // 2
        modifiers.append(mod)
    return modifiers

def ability_names():
    ability_names = ['Strength','Dexterity','Constitution','Intelligence','Wisdom','Charisma']
    return ability_names

def gen_passive_abilities(modifiers):
    """adds 10 to each modifier to create passive ability score"""
    passive_abilities = []
    for mod in modifiers:
        pasAbl = mod + 10
        passive_abilities.append(pasAbl)
    return passive_abilities

def skill_names():
    skill_names = ['Acrobatics','Animal Handling','Arcana','Athletics','Deception','History','Insight','Intimidation','Investigation','Medicine','Nature','Perception','Performance','Persuasion','Religion','Sleight of Hand','Stealth','Survival']
    return skill_names

#Do I need to zip mods and abilities to ability names?

def level():
    level = print(input("Enter level: "))
    return level

def proficiency(level):
    """calculates proficiency"""
    import math
    proficiency = math.ceil(level/4) + 1
    return proficiency



def gen_skills(proficiency,modifiers):
    """Rolls skills checks and adds modifier and passive abilities"""

def roll_dice():
    """Rolls dice of user's choosing"""
    import random
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

#problem: skill may be overridden by user as it comes from a number of variables in addition to proficiency
#even when proficiency is factored in, users typically write the skill score to include proficiency, so it is not added as a separate step after rolling
#for above reasons, commented out below version; may discard later

"""def roll_skill(proficiency):
    """Rolls skill check"""
    skill = print(int(input("Enter skill score: "))) #this will come from the db later
    isProf = print(input("Are you proficient (Y/N)?")) #skill may be modified by user later
    if isProf == "N":
        proficiency = 0
    skillRoll = skill + proficiency + random.randint(1,20)
    return skillRoll"""

def roll_skill():
    """Rolls skill check using user's entries"""
    skill = print(int(input("Enter skill score: "))) #this will come from the db later
    skillRoll = skill + proficiency + random.randint(1,20)
    return skillRoll