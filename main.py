import random
data = []

csv = open("test.csv","r").read() #open and read csv file
keys = csv.splitlines()[0].split(",") #splitlines to seperate keys and values then split to seperate each str into its own list
values = csv.splitlines()[1].split(",")
keys = [int(x) for x in keys] #convert str lists to int lists
values = [int(x) for x in values]

for i in range(len(keys)): #iterates once for every entry
    print(i,"added to list",values[i],"times") #debugging
    for value in range((values[i])): #iterates once for every time the entry has skiied
        data.append(keys[i]) #adds to list
print("\n") #newline for clean output
print(random.choice(data))

    

