from django import forms
from models import Sheet

class SheetForm(forms.ModelForm):

    class Meta:
        model = Sheet
        fields = ('character_name','level','armor_class','initiative','hit_points','conditions','inspiration','inventory','spells','speed','defenses','features','traits','proficiencies','proficiency_value','languages','description,notes','strength_score','dexterity_score','constitution_score','intelligence_score','wisdom_score','charisma_score',)