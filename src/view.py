from team_service import *
import fixtures_service
import difficulty_service


def print_fixtures(fixtures):
    for fixture in fixtures:
        team_h = get_team_from_id(fixture.get("team_h"))
        team_a = get_team_from_id(fixture.get("team_a"))
        print(f"{team_h.get('name')} v {team_a.get('name')}")


while True:
    print("1. View team information")
    print("2. View team home fixtures")
    print("3. View team away fixtures")
    print("4. View team all fixtures")
    print("5. View a team's difficulty")
    print("6. View all team's difficulty")
    selection = input("Input choice: ")
    if selection.isnumeric():
        selection = int(selection)

    if selection == 0:
        break
    if selection == 1:
        team_name = input("Input team name: ")
        print(get_team_from_name(team_name))
    elif selection == 2:
        team_name = input("Input team name: ")
        starting_gw = int(input("Input start gameweek: "))
        ending_gw = int(input("Input ending gameweek: "))
        team_id = get_team_from_name(team_name).get("id")
        print_fixtures(fixtures_service.get_team_home_fixtures(team_id, starting_gw, ending_gw))
    elif selection == 3:
        team_name = input("Input team name: ")
        starting_gw = int(input("Input start gameweek: "))
        ending_gw = int(input("Input ending gameweek: "))
        team_id = get_team_from_name(team_name).get("id")
        print_fixtures(fixtures_service.get_team_away_fixtures(team_id, starting_gw, ending_gw))
    elif selection == 4:
        team_name = input("Input team name: ")
        starting_gw = int(input("Input start gameweek: "))
        ending_gw = int(input("Input ending gameweek: "))
        team_id = get_team_from_name(team_name).get("id")
        print_fixtures(fixtures_service.get_team_fixtures(team_id, starting_gw, ending_gw))
    elif selection == 5:
        team_name = input("Input team name: ")
        starting_gw = int(input("Input start gameweek: "))
        ending_gw = int(input("Input ending gameweek: "))
        team_id = get_team_from_name(team_name).get("id")
        print(difficulty_service.calculate_all_difficulty(team_id, starting_gw, ending_gw))
    elif selection == 6:
        starting_gw = int(input("Input start gameweek: "))
        ending_gw = int(input("Input ending gameweek: "))
        print(difficulty_service.rank_team_difficulty(starting_gw, ending_gw))

