from django.shortcuts import render
from django.utils import timezone
from .models import Sheet
from .forms import SheetForm

"""def character_sheet_new(request):
    form = SheetForm()
    characters = Sheet.objects.filter(last_saved__lte=timezone.now()).order_by('last_saved')
    return render(request, 'sheet/character_sheet.html', {'form':form})""" #url chosen since this should reference the character sheet

def character_sheet(request):
    form = SheetForm()
    return render(request, 'sheet/character_sheet.html', {'form': form}) #form in curly brackets refers to form variable defined in line above