import requests
import json
import math
from pprint import pprint as pp

# obtain schedule info from API & convert to json for iterating through
r = requests.get("https://vlrgg-scraper.herokuapp.com/matches/schedule")
res = r.json()
#pp(res)

# fills up the following datasets
uniqueTours = []
dates = []
tours = []
stages = []
team1 = []
team2 = []
dts = []

for i in range(len(res)):
    if res[i]['event']['name'] not in uniqueTours:
        uniqueTours.append(res[i]['event']['name'])
    dates.append(res[i]['date'])
    tours.append(res[i]['event']['name'])
    stages.append(res[i]['event']['stage'])
    team1.append(res[i]['team1']['name'])
    team2.append(res[i]['team2']['name'])
    dts.append(res[i]['date'][5:] + ": " + res[i]['event']['name'] + ": " + res[i]['event']['stage'])

# stageObj(name of tournament, name of stage, date of stage, team1 for stage, team2 for stage)
class stageObj:
    def __init__(self, tour, names, dates, team1, team2):
        self.tour = tour
        self.names = names
        self.dates = dates
        self.team1 = team1
        self.team2 = team2

# valStages is a list of stagesObj
valStages = []
for i in range(len(res)):
    valStages.append(stageObj(tours[i], stages[i], dates[i], team1[i], team2[i]))

# tourObj(name of the tournament, stage obj, date for grand final)
class tourObj:
    # name: str
    # stages = [stageObj]
    # grandFinal: str
    def __init__(self, name, stages: list[stageObj], grandFinal):
        self.name = name
        self.stages = stages
        self.grandFinal = grandFinal

# getSummary(tourObj) --> prints the name, beginning date, and date for grand final
def getGF(tourObj):
    print(f'{tourObj.name} is going until {tourObj.grandFinal}')

# getStages(tourObj) --> prints the date and name of every stage for a tournament
def getStages(tourObj):
    print (f'{tourObj.name} \n')
    for i in tourObj.stages:
        print(f'{i.dates} : {i.names}')

# valTours is a list of toursObj
valTours = []
for i in range(len(uniqueTours)):
    tempStages = []
    tempGFDate = "TBD"
    for j in range(len(res)):
        if uniqueTours[i] == tours[j]:
            tempStages.append(valStages[j])
            if stages[j][-11:] == "Grand Final":
                tempGFDate = dates[j]
    valTours.append(tourObj(uniqueTours[i], tempStages, tempGFDate))

print('helpers loaded')

# TESTING AREA
# print(uniqueTours[0], uniqueTours[1], uniqueTours[2])
#getStages(valTours[2])
#getStages(valTours[1])

# for i in range(len(valTours)):
#     for j in range(len(valTours[i].stages)):
#         print(f'{valTours[i].name}: {valTours[i].stages[j]} is on {valTours[i].dates[j]}')
        
# print(f'{tourObj.name} is going from {tourObj.dates[0]} to {tourObj.grandFinal}')
# print("\n".join(["".join(i) for i, j in zip(valTours[i].dates[j], valTours[i].stages[j])]))
# print("\n".join(["".join(i) for i in valTours: "".join(j) for j in valTours[i].dates))

# print("\n".join(["".join(j) for j in valTours[j].dates] + ": " + ["".join(j) for j in valTours[j].stages]))


# for i in range(len(res)):
#     for j in range(len(res)):
#         if tours[i] == tours[j]:

#     if(tours[i] == )
#pp(date)
#find end dates of each tournament
# tourEndDates = [len(uniqueTours)]
# finalStages = [len(uniqueTours)]
# for i in range(len(uniqueTours)):
#     for j in range(len(tours)):
#         if(tours[j] == uniqueTours[i]):
#             tourEndDates[i] = date[j]
#             finalStages[i] = stages[j]
#             print(tourEndDates[i])


# output = []
# for i in range(len(uniqueTours)):
#     output.append(tourEndDates[i][5:] + ": " + uniqueTours[i] + "(Stage: " + finalStages[i] + ")")
# print(output)

# test functions 


'''

tourEndDates = []

for i in range(len(res)):
    if(stages[i][11:] == "Grand Final"):
        print(dts[i])
        tourEndDates.append(date[i])
----
tourStages = set()
dateTourStages = {}

tourStages = dict.fromkeys(tours,stages)
dateTourStages = dict.fromkeys(date, tourStages)
print(tourStages)
print(dateTourStages)

----

for i in range(len(tourStages)):
    # removes the day from the date list
    print(date[i][5:] + ": " + tourStages[i])
'''
