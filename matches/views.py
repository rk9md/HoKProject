from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Match
from .forms import MatchModelForm
from django.views.generic.base import TemplateView

class MatchView(generic.ListView):
    template_name = 'matches/match.html'
    context_object_name = 'matches_list'

    def get_queryset(self):
        return Match.objects.order_by('-pub_date')

class MatchDetailView(generic.DetailView):
    model = Match
    template_name = 'matches/matchdetail.html'

class MatchCreateView(generic.CreateView):
    form_class  = MatchModelForm
    template_name = 'matches/matchpost.html'
    queryset = Match.objects.all()

class HomePageView(TemplateView):
    template_name = "matches/home.html"