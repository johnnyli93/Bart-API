
# coding: utf-8

# In[10]:

#        **** ALL CREDIT GOES TO BART FOR PROVIDING A FREE API****

#bringing in the libraries
import json
import requests as req
from datetime import datetime, date
import pandas as pd

#bringing in a csv that contains all the stations and the abbreviations.
#MUST BE IN THE SAME DIRECTORY (LOCATION) AS THIS CODE. so if this ipynb file is in your desktop
#make sure the csv is in the same place

bart_reader = pd.read_csv("bartstations.csv")
api = "ZWZD-5B96-9H2T-DWE9"

#asks user for date
today = input("What's todays date? Please input in MM-DD-YYYY format: ")
#converts into datetime format
todayformatted = datetime.strptime(today, "%m-%d-%Y").strftime("%m/%d/%Y")
#shows users the abbreviated name of each station and their respective station name
print(bart_reader)

#asks user origin and destination
origin = input("Where are you coming from? Input the 4-character abbreviation ")
dest = input("Where do you want to go? Input the 4-character abbreviation " )
direction = input("North or southbound? (n or s)")

#creates a url for api that is used to get the price of the trip
url = "http://api.bart.gov/api/sched.aspx?cmd=fare&orig=%s&dest=%s&date=%s&json=y&key=%s" % (origin, dest, todayformatted, api)
#creates a url for api that is used to get the schedule of the train(s) the user will take
url2 = "http://ord3-dev.sfbart.org/api/etd.aspx?cmd=etd&orig=%s&dir=%s&json=y&key=%s" % (origin, direction, api)


# In[11]:

#requesting the api thing
get_url = req.get(url).json()
get_url2 = req.get(url2).json()
price = get_url["root"]["trip"]["fare"]

#shows user the time and price of trip
print("The time now is "+ str(datetime.now()))
print("The one-way trip will cost you $" + str(price) + ".\n")

#shows the next three trains for all trains that will take user to destination
for x in range(len(get_url2["root"]["station"][0]["etd"])):
    train_name = get_url2["root"]["station"][0]["etd"][x]["destination"]
    for y in range(len(get_url2["root"]["station"][0]["etd"][x]["estimate"])):
        train_time = get_url2["root"]["station"][0]["etd"][x]["estimate"][y]["minutes"]
        train_length = get_url2["root"]["station"][0]["etd"][x]["estimate"][y]["length"]
        if train_time == "Leaving":
            print("The " + train_name + " train is already leaving.")
        elif int(train_time) < 5:
            print("The next "+ train_length+ "-car " + train_name + " train comes in " + train_time + " minutes. RUN!!!") 
        else:
            print("The next "+ train_length+ "-car " + train_name + " train comes in " + train_time + " minutes.")


# In[12]:

#in case you want to check the api in json format. copy and paste the url without the quotes
url2


# In[ ]:



