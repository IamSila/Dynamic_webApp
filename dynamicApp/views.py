from django.shortcuts import render
from .models import Team
from .models import Analytic
# Create your views here.
def index(request):
    context = {}
    analytics = Analytic.objects.all()
    teams = Team.objects.all()
    context['teams'] = teams
    context['analytics'] = analytics
    return render(request, 'index.html', context)