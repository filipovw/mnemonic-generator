import random
import os


def getDirectory():
    return os.getcwd()


def filenameCheck():
    directory = getDirectory()
    a = 0
    if(os.path.isfile(directory + "\seed_phrases.txt")):
        a = 1
    while os.path.isfile(directory + "\seed_phrases" + str(a) + ".txt"):
        a += 1
    return a


directory = getDirectory()
filename = filenameCheck()


def readWordList():
    directory = getDirectory()
    f = open(directory + "\wordlist.txt")
    content = f.read()
    f.close()
    list = content.split(" ")
    return list

def getRandomWords(list):
    list1 = [] 
    for i in range(12):
        randomWord = random.choice(list)
        if randomWord in list1:
            list1.append(random.choice(list))
            continue
        list1.append(randomWord)
    return list1     

def lineToString(line):
    string = " ".join(line)
    string = string.strip()
    string = string.lstrip(" ")
    string = string.rstrip(" ")
    string = string + "\n"
    return string

def writeToFile(row):
   
    if filename == 0:
        f = open(directory + "\seed_phrases.txt", "a")
    else:
        f = open(directory + "\seed_phrases" + str(filename) + ".txt", "a")
    
    f.write(row + "\n")
    f.close()

def loop(n):
    count = 0
    for i in range(n):
        list = readWordList()
        line = getRandomWords(list)
        row = lineToString(line)
        row = row.strip("\n")
        writeToFile(row)
        count += 1
        print("Current loop: " + str(count))

a = input("How many sets of 12 phrase mnemonics should be generated?")
n = int(a)
loop(n)