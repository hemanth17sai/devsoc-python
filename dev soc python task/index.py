#Print result after every function to check 
#Read the info in every functions to get the proper understanding of desired output

import json
from multiprocessing.sharedctypes import Value
filepaths='data.json'

def read_data(filepaths):
    with open(filepaths, "r") as json_file:
      data = json.load(json_file)
    return data
    # Read data from filepaths

data = read_data(filepaths)
# print(data)
# print("\n\n\n")

def get_oldest(data):
     max=0
     c=0
     oldest=[]

     for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] >max):
            max=data["AVENGERS"][i]['age']
            oldest=data["AVENGERS"][i]

        if data["AVENGERS"][i]['age'] == max:
            oldest[c]=data["AVENGERS"][i]
            c+=1

     for i in data["DC"]:
        if (data["DC"][i]['age'] >max):
            max=data["DC"][i]['age']
            oldest=data["DC"][i]

        if data["DC"][i]['age'] == max:
            oldest[c]=data["DC"][i]
            c+=1
    # Return all info of the oldest superheroes
    # Return all info of the oldest superheroes
     return oldest

# returns info: Thor and Wonder Woman
# b=get_oldest(data)
# print(b)
# print("\n\n\n")


def get_oldest_avenger(data):
   max=0
   for j in data["AVENGERS"]:
        if (data["AVENGERS"][j]['age'] >max):
            max=data["AVENGERS"][j]['age']
            oldest_avenger=data["AVENGERS"][j]

    # Return all info of the oldest avenger
   return oldest_avenger
# a=get_oldest_avenger(data)
# print(a)
# returns info: Thor 


def get_total_points(data):
    total_points={}
    for i in data["AVENGERS"]:
        key=data["AVENGERS"][i]["name"]
        total_points[key] = 0
        for j in data["AVENGERS"][i]['points']:
          total_points[key]+=data["AVENGERS"][i]['points'][j]
    for i in data["DC"]:
        key=data["DC"][i]["name"]
        total_points[key] = 0
        for j in data["DC"][i]['points']:
          total_points[key]+=data["DC"][i]['points'][j]
    # Return a dictionary
    # Key: superhero name
    # Value: total points
    return total_points
# c=get_total_points(data)
# print(c)

# returns info: Dict of superhero name and total points

def get_more_than_average(data):
    more_than_average=[]
    
    avg_mcu=0
    avg_dc=0
    for i in data["AVENGERS"]:
        avg_mcu+=data["AVENGERS"][i]["points"]["stealth"]
    avg_mcu=avg_mcu/len(data["AVENGERS"])
    c=0
    for i in data["AVENGERS"]:
        if(data["AVENGERS"][i]['points']['stealth']>avg_mcu):
            more_than_average.append(data["AVENGERS"][i])
            c+=1
    for i in data["DC"]:
      avg_dc+=data["DC"][i]['points']['strength']
    avg_dc=avg_dc/len(data["DC"])
    for i in data["DC"]:
        if(data["DC"][i]['points']['strength']>avg_dc):
            more_than_average.append(data["DC"][i])
            c+=1
    '''
    Return list of superheroes with stealth more than average in MCU 
    and list of superheroes with strength more than average in DCEU
    '''
    return more_than_average
# d=get_more_than_average(data)
# print(d)

  #returns info: Steve Rogers and Superman

def get_names(data):
    names=[]
    for i in data["AVENGERS"]:
        names.append(i)
    for j in data["DC"]:
        names.append(j)
    # Return a list of superhero names
    return names
e=get_names(data)
print(e)

#returns a list 
