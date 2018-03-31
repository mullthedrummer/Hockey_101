###############################
###############################
###
### Where we live
### Andrew Cullen 4 February 2018
###
###############################
###############################

### Import Libraries
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib, json, ast

####################
####################
### Team Information and Rosters

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
### Create lists for each column based on JSON information
for id in range(1,31):
    team_FranchiseID.append(teamData['teams'][id]['franchise']['franchiseId'])
    TeamName.append(teamData['teams'][id]['name'])
    City.append(teamData['teams'][id]['venue']['city'])
    TimeZone.append(teamData['teams'][id]['venue']['timeZone']['tz'])
    FirstYearOfPlay.append(teamData['teams'][id]['firstYearOfPlay'])
    Division.append(teamData['teams'][id]['division']['name'])
    Conference.append(teamData['teams'][id]['conference']['name'])

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

### Clean up un-needed lists
del(team_FranchiseID, TeamName,City,TimeZone,FirstYearOfPlay,Division,Conference)

### END: Build out Team Information
####################
