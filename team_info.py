import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib, json, ast


def team_Information_Function():
    ### Pull information from API
    url_Team_Information = "https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster"
    response = urllib.urlopen(url_Team_Information)
    teamData = json.loads(response.read())

    ####################
    ### Build out Team Information

    ### Create empty lists to store json information
    team_FranchiseID=[]
    TeamName=[]
    City=[]
    TimeZone=[]
    FirstYearOfPlay=[]
    Division=[]
    Conference=[]
    PlayerID=[]

    ### Populate lists for each column based on JSON information
    for id_team in range(0,31):
        team_FranchiseID.append(teamData['teams'][id_team]['id'])
        TeamName.append(teamData['teams'][id_team]['name'])
        City.append(teamData['teams'][id_team]['venue']['city'])
        TimeZone.append(teamData['teams'][id_team]['venue']['timeZone']['tz'])
        FirstYearOfPlay.append(teamData['teams'][id_team]['firstYearOfPlay'])
        Division.append(teamData['teams'][id_team]['division']['name'])
        Conference.append(teamData['teams'][id_team]['conference']['name'])

        ### Save off Player ID's into a list for each player on Actvie Rosters
        for id_player in range(1,len(teamData['teams'][id_team]['roster']['roster'])):
            PlayerID.append(teamData['teams'][id_team]['roster']['roster'][id_player]['person']['id'])

    ### Create DataFrame of team information
    teams = {'FranchiseID': team_FranchiseID,
            'TeamName': TeamName,
            'City': City,
            'TimeZone': TimeZone,
            'FirstYearOfPlay': FirstYearOfPlay,
            'Division': Division,
            'Conference': Conference
    }

    teams_pd = pd.DataFrame(teams)

    del(url_Team_Information, response, teamData, 
        team_FranchiseID, TeamName,City,TimeZone,FirstYearOfPlay,Division,
        Conference, url_Team_Information, response, teamData)

    ### END: Build out Team Information
    ####################


    return teams_pd, PlayerID
