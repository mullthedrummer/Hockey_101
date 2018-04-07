import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib, json, ast


def team_Roster_Function(PlayerID):
    ####################
    ### Build out Roster Information

    ### Pull information from API, requires to be run for each player loop
    url_Team_Information = "https://statsapi.web.nhl.com/api/v1/people/"


    ### Create empty lists to store json information
    First_Name = []
    Last_Name = []
    DOB = []
    Age = []
    BirthPlace = []
    BirthCountry = []
    Nationality = []
    Height = []
    Weight = []
    Active = []
    alternateCaptain = []
    Captain = []
    Rookie = []
    ShootsCatches = []
    Team_ID = []
    Team_name = []
    Number = []
    Position = []
    Position_Type = []
    Position_Abb = []

    ### Populate lists for each column based on JSON information
    for id_Player in PlayerID:
        ### Loop through each player ID and adjust url to point at right page
        url_Team_Information_modded = url_Team_Information+str(id_Player)
        response = urllib.urlopen(url_Team_Information_modded)
        peopleData = json.loads(response.read())

        ### Populate lists for each column based on JSON information
        First_Name.append(peopleData['people'][0]['firstName'])
        Last_Name.append(peopleData['people'][0]['lastName'])
        DOB.append(peopleData['people'][0]['birthDate'])
        Age.append(peopleData['people'][0]['currentAge'])
        BirthPlace.append(peopleData['people'][0]['birthCity'])
        BirthCountry.append(peopleData['people'][0]['birthCountry'])
        Nationality.append(peopleData['people'][0]['nationality'])
        Height.append(peopleData['people'][0]['height'])
        Weight.append(peopleData['people'][0]['weight'])
        Active.append(peopleData['people'][0]['active'])
        alternateCaptain.append(peopleData['people'][0]['alternateCaptain'])
        Captain.append(peopleData['people'][0]['captain'])
        Rookie.append(peopleData['people'][0]['rookie'])
        ShootsCatches.append(peopleData['people'][0]['shootsCatches'])
        Team_ID.append(peopleData['people'][0]['currentTeam']['id'])
        Team_name.append(peopleData['people'][0]['currentTeam']['name'])
        try:
            Number.append(peopleData['people'][0]['primaryNumber'])
        except:
            Number.append(00)
        Position.append(peopleData['people'][0]['primaryPosition']['name'])
        Position_Type.append(peopleData['people'][0]['primaryPosition']['type'])
        Position_Abb.append(peopleData['people'][0]['primaryPosition']['abbreviation'])


    ### Create DataFrame of roster information
    rosters = {
                'First_Name' : First_Name,
                'Last_Name' : Last_Name,
                'DOB' : DOB,
                'Age' : Age,
                'BirthPlace' : BirthPlace,
                'BirthCountry' : BirthCountry,
                'Nationality' : Nationality,
                'Height' : Height,
                'Weight' : Weight,
                'Active' : Active,
                'alternateCaptain' : alternateCaptain,
                'Captain' : Captain,
                'Rookie' : Rookie,
                'ShootsCatches' : ShootsCatches,
                'Team_ID' : Team_ID,
                'Team_name' : Team_name,
                'Number' : Number,
                'Position' : Position,
                'Position_Type' : Position_Type,
                'Position_Abb' : Position_Abb
                }

    rosters_pd = pd.DataFrame(rosters)

    ### Clean up un-needed lists
    del(url_Team_Information, response, teamData, 
        First_Name, Last_Name, DOB, Age, BirthPlace, BirthCountry, Nationality, Height, Weight,
        alternateCaptain, Captain, Rookie, ShootsCatches, Team_ID, Team_name, Position, Position_Type,
        Position_Abb)

    ### END: Build out Roster Information
    ####################

    return rosters_pd
