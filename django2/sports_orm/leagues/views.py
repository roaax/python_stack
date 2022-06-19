from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		'baseball_leagues':League.objects.filter(sport='Baseball'), 
		'women_leagues':League.objects.filter(name__contains='Womens'), 
		'hockey_leagues':League.objects.filter(sport__contains='hockey'),
		'leagues_are_not_football':League.objects.exclude(sport='Football'), 
		'conferences_leagues':League.objects.filter(name__contains='Conference'), 
		'atlantic_leagues':League.objects.filter(name__contains='Atlantic'), 
		'dallas_teams':Team.objects.filter(location='Dallas'),
		'raptors':Team.objects.filter(team_name='Raptors'),
		'cities_teams':Team.objects.filter(location__contains='City'), 
		'teams_start_with_t':Team.objects.filter(team_name__startswith='T'), 
		'ordered_teams_by_location':Team.objects.all().order_by('location'),
		'ordered_teams_by_name_reverse':Team.objects.all().order_by('-team_name'),
		'players_with_lname_cooper':Player.objects.filter(last_name='Cooper'),
		'players_with_fname_joshua':Player.objects.filter(first_name='Joshua'),
		'players_with_lname_cooper_without_joshua':Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua'),
		'alexander_or_wyatt':Player.objects.filter(first_name__in=['Alexander','Wyatt']), 
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")