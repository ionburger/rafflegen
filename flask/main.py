import random
from pscript import py2js
def main(file_path):
    csv = open(file_path,"r").read() #open and read csv file
    #print(csv)
    data = []
    keys = []
    values = []


    split = csv.splitlines() #splitlines to seperate keys and values then split to seperate each str into its own list
    for i in range(len(split)):
        keys.append(split[i].split(",")[0])
        values.append(split[i].split(",")[1])


    keys = [int(x) for x in keys] #convert str lists to int lists
    values = [int(x) for x in values]

    for i in range(len(keys)): #iterates once for every entry
        for value in range((values[i])): #iterates once for every time the entry has skiied
            data.append(keys[i]) #adds to list
    return str(random.choice(data)) #chooses random entry weighted by number of times skied



    

