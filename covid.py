#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:13:44 2020

@author: jamesdchu
"""

import requests
import matplotlib.pyplot as plt
import numpy as np

##input statements
state = input("Which State? (pls use correct abbreivation): ")
historical_data = input("Would you like to see current or historical data: ")

##functions 
def current(state):
    #Retrieving the data
    current_data_states = requests.get("https://covidtracking.com/api/v1/states/current.json").json()
    
    #Printing the information for the chosen state
    for state_data in current_data_states:
        if state.upper() == state_data["state"]:
            print("Date Updated", str(state_data["date"]))
            print("Positive", state_data["positive"])
            print("Negative", state_data["negative"])
            print("Deaths", state_data["death"])

def historical(state):
    #Retrieving the data
    state_historical_data = requests.get("https://covidtracking.com/api/v1/states/" + state.lower() + "/daily.json").json()
    #Making the arrays for x and y axis
    cases_data = np.array([])
    dates_data = np.array([])
    for i in range(len(state_historical_data)):
        cases_data = np.append(cases_data, (state_historical_data[i]['positive']))
        dates_data = np.append(dates_data, len(state_historical_data)-i)
    
    #Making the plot
    plt.plot(dates_data, cases_data)
    plt.title(state.upper() + " COVID-19 Cases vs Time")
    plt.ylabel("Total # of Cases")
    plt.xlabel("Days since First Confirmed Case")
    plt.show()
    
    
##Checking for errors and running functions
if(historical_data.lower() == "current"):
    current(state)
elif(historical_data.lower() == "historical"):
    historical(state)
else: 
    print("You made a typo")