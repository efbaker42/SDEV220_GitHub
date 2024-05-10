from django.shortcuts import render
from django.utils import timezone
from .models import Sheet
from .forms import SheetForm
from django.shortcuts import redirect


#may change later; still need way to list character sheets and edit sheets
def character_sheet(request):
    form = SheetForm()
    return render(request, 'sheet/character_sheet.html', {'form': form})

#doesn't save yet; sheet_detail.html not fleshed out
def character_sheet_new(request):
    if request.method == "POST":
        form = SheetForm(request.POST)
        if form.is_valid():
            sheet = form.save(commit=False)
            sheet.author = request.user
            sheet.last_saved = timezone.now()
            sheet.save()
            return redirect('sheet_detail', pk=sheet.pk) #this doesn't do anything yet because no sheet_detail page yet
    else:
        form = SheetForm()
    return render(request, 'sheet/character_sheet.html', {'form': form})

"""def sheet_detail(request):
    form = SheetForm()
    return render(request, 'sheet/sheet_detail/', {'form': form})"""