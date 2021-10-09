import requests
import json

from os.path import exists

FPLBASEURL = "https://fantasy.premierleague.com/api/"

FPLDATAENDPOINT = f"{FPLBASEURL}bootstrap-static/"
FPLFIXTURESENDPOINT = f"{FPLBASEURL}fixtures/"

def get_fixtures ():
    file_exists = exists("./fplfixtures.json")
    if not file_exists:
        response = requests.get(url = FPLFIXTURESENDPOINT, params=None)
        with open("./fplfixtures.json", "w", encoding="utf-8") as outfile:
            outfile.write(response.text)

    with open("./fplfixtures.json", "r", encoding="utf-8") as infile:
        fplfixturedata = json.loads(infile.read())

    return fplfixturedata


def get_fpldata():
    file_exists = exists("./fpldata.json")
    if not file_exists:
        response = requests.get(url=FPLDATAENDPOINT, params=None)
        with open("./fpldata.json", "w", encoding="utf-8") as outfile:
            outfile.write(response.text)

    with open("./fpldata.json", "r", encoding="utf-8") as infile:
        fpldata = json.loads(infile.read())

    return fpldata

