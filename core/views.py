from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import models
import datetime
from datetime import timedelta
from django.views.generic.list import ListView
from django.utils import timezone
from django.utils import formats
from django.db.models.functions import Lower

from leagues.models import Season
from leagues.models import MatchUp
from leagues.models import Stat
from leagues.models import Roster
from leagues.models import Team_Stat
# Create your views here.

def home(request):
    context = {}
    # context["season"] = Season.objects.get(is_current_season=1)
    context["season"] = Season.objects.all()
    context["matchup"]  = MatchUp.objects.filter(week__date__range=(datetime.date.today(), datetime.date.today() + timedelta(days=9)))

    return render(request, "core/home.html", context=context)

def leagues(request):
    return render(request, "leagues/index.html")


class MatchUpDetailView(ListView):
    context_object_name = 'matchup_list'

    def get_queryset(self):
        return MatchUp.objects.order_by('time')

    def get_context_data(self, **kwargs):
        context = super(MatchUpDetailView, self).get_context_data(**kwargs)
        context["season"] = Season.objects.all()
        context["roster"] = Roster.objects.order_by(Lower('player__last_name'))
        context["stat"] = Stat.objects.all()

        return context

class TeamStatDetailView(ListView):
    context_object_name = 'team_list'

    def get_queryset(self):
        return Team_Stat.objects.order_by('-win','loss','-tie')

    def get_context_data(self, **kwargs):
        context = super(TeamStatDetailView, self).get_context_data(**kwargs)
        # context["season"] = Season.objects.all()
        # context["roster"] = Roster.objects.order_by(Lower('player__last_name'))
        # context["stat"] = Stat.objects.all()

        return context
