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
from team_info import team_Information_Function
from roster_information import team_Roster_Function


####################
### Team Information and Player ID's used for Rosters and Stats

team_Information, PlayerID = team_Information_Function()

### END: Team Information and Player ID's used for Rosters and Stats
####################

####################
### Team Rosters

roster_Information = team_Roster_Function(PlayerID)

### END: Team Rosters
####################
