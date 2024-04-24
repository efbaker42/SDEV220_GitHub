from DiceRollFuncs import *
import unittest

#ensure generate_abilities() works as expected:
abilities_list = generate_abilities()
print(f"abilities are: {abilities_list}")

#verify that update_mod(abilities) works as expected:
modifier_list = update_mod(abilities_list)
print(f"modifiers are: {modifier_list}")