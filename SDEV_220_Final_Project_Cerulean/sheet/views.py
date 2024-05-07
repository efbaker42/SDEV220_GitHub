from django.shortcuts import render

def character_list(request):
    return render(request, 'sheet/character_list.html', {}) #requests character list template