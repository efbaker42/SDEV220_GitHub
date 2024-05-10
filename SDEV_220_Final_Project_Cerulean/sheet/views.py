from django.shortcuts import render
from django.utils import timezone
from .models import Sheet
from .forms import SheetForm
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404


#may change later; still need way to list character sheets and edit sheets
def character_sheet(request):
    form = SheetForm()
    return render(request, 'sheet/character_sheet.html', {'form': form})

#doesn't save yet; sheet_detail.html not fleshed out
def character_sheet_new(request):
    if request.method == "GET":
        form = SheetForm(request.GET)
        return render(request, 'sheet/character_sheet.html', {'form': form})
    elif request.method == "POST":
        form = SheetForm(request.POST)
        if form.is_valid():
            sheet = form.save() #removed commit=False to see if that would help
            #I excluded sheet.author because there is no author in the model, and it might interpret the form as invalid
            sheet.last_saved = timezone.now()
            sheet.save()
            return redirect('sheet_detail', pk=sheet.pk) #the sheet_detail view/page has issues, so if it saves correctly, I should get an error message
        else:
            form = SheetForm()
        return render(request, 'sheet/sheet_edit.html', {'form': form})
#    
#    if request.method == "POST":
#        form = SheetForm(request.POST)
#        if form.is_valid():
#            sheet = form.save(commit=False)
#            #sheet.author = request.user #there is no author field required in my form, which may impact whether the form is valid
#            sheet.last_saved = timezone.now()
#            sheet.save()
#            #return redirect(request, 'sheet/error_message.html')
#            return redirect('sheet/character_sheet.html') #redirect uses name of url pattern #this is a stand-in because sheet_detail doesn't work yet
#            #return redirect('sheet_detail', pk=sheet.pk) #eventually, this should display the completed character sheet; this doesn't do anything yet because no sheet_detail page yet
#        else:
#            #return redirect(request, 'sheet/success_message.html') #when the no HTTPresponse error is resolved, I expect to use this for testing
#            form = SheetForm()
#            return render(request, 'sheet/character_sheet.html', {'form': form}) #user will get same screen whether the sheet saves or not"""

def sheet_detail(request,pk):
    sheet = get_object_or_404(Sheet, pk=pk)
    return render(request, 'sheet/sheet_detail.html', {'form': form})

#def sheet_list(request):
#    sheets = Sheet.objects.filter(last_saved__lte=timezone.now()).order_by('character_name')
#    return render(request, 'sheet/sheet_list.html', {'sheets': sheets})