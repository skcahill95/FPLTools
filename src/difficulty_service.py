import team_service, fixtures_service


def calculate_home_difficulty(team_id, starting_gw, ending_gw):
    difficulty = 0
    fixtures = fixtures_service.get_team_home_fixtures(team_id, starting_gw, ending_gw)

    for fixture in fixtures:
        difficulty += fixture.get("team_h_difficulty")

    return difficulty


def calculate_away_difficulty(team_id, starting_gw, ending_gw):
    difficulty = 0
    fixtures = fixtures_service.get_team_away_fixtures(team_id, starting_gw, ending_gw)

    for fixture in fixtures:
        difficulty += fixture.get("team_a_difficulty")

    return difficulty


def calculate_all_difficulty(team_id, starting_gw, ending_gw):
    return calculate_home_difficulty(team_id, starting_gw, ending_gw) + \
           calculate_away_difficulty(team_id, starting_gw, ending_gw)


def rank_team_difficulty(starting_gw, ending_gw):
    teams = team_service.get_teams()
    team_difficulties = []

    for team in teams:
        difficulty = calculate_all_difficulty(team.get("id"), starting_gw, ending_gw)
        team_difficulties.append((team.get("name"), difficulty))

    return sorted(team_difficulties, key=lambda kv: kv[1])

