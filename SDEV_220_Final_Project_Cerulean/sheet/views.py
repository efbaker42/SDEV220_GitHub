from django.shortcuts import render
from django.utils import timezone
from .models import Sheet

def character_list(request):
    characters = Sheet.objects.filter(last_saved__lte=timezone.now()).order_by('last_saved')
    return render(request, 'sheet/character_list.html', {'characters':characters}) #requests character list template