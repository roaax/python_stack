from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker


def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"all_teams_in_atlantic_soccer":Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"current_players_in_boston":Player.objects.filter(curr_team__location="Boston", curr_team__team_name="Penguins"),
		'players_in_icbc':Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"), # all (current) players in the International Collegiate Baseball Conference
		'players_in_acaf_with_lname_lopez':Player.objects.filter(curr_team__league__name="American Conference of Amateur Football", last_name="Lopez"), # all (current) players in the American Conference of Amateur Football with last name "Lopez"
		'football_players':Player.objects.filter(curr_team__league__sport="Football"), # all football players
		'teams_with_curr_player_sophia':Team.objects.filter(curr_players__first_name="Sophia"), # all teams with a (current) player named "Sophia"
		'leagues_with_curr_player_sophia':League.objects.filter(teams__curr_players__first_name="Sophia"), # all leagues with a (current) player named "Sophia"
		'players_lname_flores_not_with_wr':Player.objects.filter(last_name="Flores").exclude(curr_team__location="Washington" , curr_team__team_name="Roughriders"), # everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
		'samuel_evans_teams':Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"), # all teams, past and present, that Samuel Evans has played with
		'manitoba_tiger_cats_players':Player.objects.filter(all_teams__location="Manitoba" , all_teams__team_name="Tiger-Cats"),  # all players, past and present, with the Manitoba Tiger-Cats
		'players_not_curr_with_wv':Player.objects.filter(all_teams__location="Wichita" , all_teams__team_name="Vikings").exclude(curr_team__location="Wichita" , curr_team__team_name="Vikings"),  # all players who were formerly (but aren't currently) with the Wichita Vikings
		'jacob_gray_teams':Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(team_name="Colts") , # every team that Jacob Gray played for before he joined the Oregon Colts
		'joshua_in_atlantic':Player.objects.filter(first_name="Joshua",all_teams__league__name="Atlantic Federation of Amateur Baseball Players"), # everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
		# all teams that have had 12 or more players, past and present.
		'teams_have_had_12players':
		Team.objects.annotate(had_players=Count('all_players')).filter(had_players__gte=12) 
		or 
		Team.objects.annotate(have_players=Count('curr_players')).filter(have_players__gte=12),
		
		# all players and count of teams played for, sorted by the number of teams they've played for
		'players_and_teams_number': Player.objects.annotate(num_teams=Count("all_teams")).order_by("num_teams"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")