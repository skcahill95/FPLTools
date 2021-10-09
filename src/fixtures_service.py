from src import get_fixtures


def get_team_home_fixtures(team_id, starting_gw, ending_gw):
    fixtures = get_fixtures()
    home_fixtures = []
    for fixture in fixtures:
        if fixture.get("team_h") == team_id and starting_gw <= fixture.get("event") <= ending_gw:
            home_fixtures.append(fixture)

    return home_fixtures


def get_team_away_fixtures(team_id, starting_gw, ending_gw):
    fixtures = get_fixtures()
    away_fixtures = []
    for fixture in fixtures:
        if fixture.get("team_a") == team_id and starting_gw <= fixture.get("event") <= ending_gw:
            away_fixtures.append(fixture)

    return away_fixtures


def get_team_fixtures(team_id, starting_gw, ending_gw):
    fixtures = get_fixtures()
    team_fixtures = []
    for fixture in fixtures:
        if (fixture.get("team_h") == team_id or fixture.get("team_a") == team_id) \
                and starting_gw <= fixture.get("event") <= ending_gw:
            team_fixtures.append(fixture)

    return team_fixtures


