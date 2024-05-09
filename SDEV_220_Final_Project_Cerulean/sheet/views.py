from django.shortcuts import render
from django.utils import timezone
from .models import Sheet

#may replace with sheet later
def character_sheet(request):
    characters = Sheet.objects.filter(last_saved__lte=timezone.now()).order_by('last_saved')
    return render(request, 'sheet/character_sheet.html', {'characters':characters}) #requests character sheet template