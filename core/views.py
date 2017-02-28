from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import models
import datetime

from leagues.models import Player
from leagues.models import League
from leagues.models import Game
from leagues.models import Season
# Create your views here.

def home(request):
    context = {}
    # context["season"] = Season.objects.get(is_current_season=1)
    context["season"] = Season.objects.all()
    context["players"] = Player.objects.all()
    context["league"] = League.objects.all()
    context["game"] = Game.objects.all()
    
    # now = datetime.datetime.now().date
    # print now

    # next_game = Game.objects.filter(date__gt=datetime.date.today()).order_by("time")[0]
    # print next_game
    # previous_game = Game.objects.filter(date__lt=now).order_by(time)[0]
    
    # context["next_game"] = next_game
    # context["previous_game"] = previous

    return render(request, "core/home.html", context=context)

def leagues(request):
    return render(request, "leagues/index.html")