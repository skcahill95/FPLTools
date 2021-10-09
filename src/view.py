from team_service import *

while True:
    print("1. View team information")
    selection = input("Input choice: ")
    if selection.isnumeric():
        selection = int(selection)

    if selection == 0:
        break
    if selection == 1:
        team_name = input("Input team name: ")
        print(get_team_from_name(team_name))