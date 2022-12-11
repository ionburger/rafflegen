import random
import logging
import argparse
import tkinter as tk
from tkinter import filedialog

parser = argparse.ArgumentParser(prog="raffle", description="raffle -f <file location>")
parser.add_argument("-f", "--file", help="file location")
parser.add_argument("-d", "--debug", help="debug mode", action="store_true")
args = parser.parse_args()

logger = logging.getLogger()
if args.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

if args.file:
    filename = args.file
else:
    filename = selected_file = filedialog.askopenfilename()
    if filename == "":
        filename = "test.csv" #default to test.csv if no input
        logger.info(" using default file location: test.csv")

csv = open(filename,"r").read() #open and read csv file
data = []

keys = csv.splitlines()[0].split(",") #splitlines to seperate keys and values then split to seperate each str into its own list
values = csv.splitlines()[1].split(",")
keys = [int(x) for x in keys] #convert str lists to int lists
values = [int(x) for x in values]

for i in range(len(keys)): #iterates once for every entry
    logger.debug(" "+str(keys[i])+" added to list "+str(values[i])+" times") #debugging
    for value in range((values[i])): #iterates once for every time the entry has skiied
        data.append(keys[i]) #adds to list
result = str(random.choice(data)) #chooses random entry weighted by number of times skied
logger.info("result: "+result) #displays result to cli
tk.messagebox.showinfo("result", result) #displays result


    

