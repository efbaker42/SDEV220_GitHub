from django.shortcuts import render
from django.utils import timezone
from .models import Sheet
from .forms import SheetForm
from django.contrib import messages
from django.shortcuts import redirect


#may change later; still need way to list character sheets and edit sheets
def character_sheet(request):
    form = SheetForm()
    return render(request, 'sheet/character_sheet.html', {'form': form})

#doesn't save yet; sheet_detail.html not fleshed out
def character_sheet_new(request):
    request.method == "GET"
    form = SheetForm(request.GET)
    return render(request, 'sheet/character_sheet.html', {'form': form})
    if request.method == "POST":
        form = SheetForm(request.POST)
        if form.is_valid():
            sheet = form.save(commit=False)
            #sheet.author = request.user #there is no author field required in my form, which may impact whether the form is valid
            sheet.last_saved = timezone.now()
            sheet.save()
            return redirect('sheet/character_sheet.html') #redirect uses name of url pattern #this is a stand-in because sheet_detail doesn't work yet
            #return redirect('sheet_detail', pk=sheet.pk) #eventually, this should display the completed character sheet; this doesn't do anything yet because no sheet_detail page yet
        else:
            #messages.error(request, "Error making sheet") #when the no HTTPresponse error is resolved, I expect to use this for testing
            form = SheetForm()
            return render(request, 'sheet/character_sheet.html', {'form': form}) #user will get same screen whether the sheet saves or not"""

def sheet_detail(request,):
    form = SheetForm()
    return render(request, 'sheet/sheet_detail.html', {'form': form})