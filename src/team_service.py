from src import get_fpldata


def get_teams():
    return get_fpldata().get("teams")

def get_team_from_name(team_name):
    teams = get_teams()

    for team in teams:
        if team.get("name").upper() == team_name.upper():
            return team

def get_team_from_id(team_id):
    teams = get_teams()

    for team in teams:
        if team.get("id") == team_id:
            return team

