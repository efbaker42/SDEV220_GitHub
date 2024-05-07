from django.shortcuts import render

# Create your views here.
from .models import Sheet,SheetForm
#view function to create a form and render the template
def character_sheet(request):

    if request.method == "POST":
        form = SheetForm(request.POST) #create form with data from the request
        if form.is_valid():
            form.save()
            form = SheetForm() #if a successful sheet was saved, return empty form probably want to change this to show the original again
    else:
        form = SheetForm()
    
    #return the html while passing in the form object
    return render(request, "charactersheet.html",{"form":form})