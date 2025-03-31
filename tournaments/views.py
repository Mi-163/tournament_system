from django.shortcuts import render

# Create your views here.
from .models import Tournament

def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournaments/tournaments.html', {'tournaments': tournaments})