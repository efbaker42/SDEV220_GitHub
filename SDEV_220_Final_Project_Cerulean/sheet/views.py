from django.shortcuts import render
from django.utils import timezone
from .models import Sheet
from .forms import SheetForm

"""def character_sheet_new(request):
    form = SheetForm()
    return render(request, 'sheet/character_sheet.html', {'form':form})""" #url chosen since this should reference the character sheet

def character_sheet(request):
    characters = Sheet.objects.filter(last_saved__lte=timezone.now()).order_by('last_saved')
    return render(request, 'sheet/character_sheet.html', {'form': form}) #requests character sheet template