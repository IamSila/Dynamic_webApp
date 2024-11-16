from django.shortcuts import render
from .models import Team

# Create your views here.
def index(request):
    context = {}
    teams = Team.objects.all()
    context['teams'] = teams
    return render(request, 'index.html', context)