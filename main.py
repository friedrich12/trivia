# Copyright 2021 Friedrich Doku

import json
import requests
import random
from art import *
from playsound import playsound


print(text2art('''SUPER TRIVIA F3''', font="small"))
playsound("smash.mp3")

url = input("Enter API URL:")
print("Got it loading.. " + url)


res = requests.get(url)

data = json.loads(res.text)

options = []
players = []

print("Enter Player Names type x to quit \n")
while True:
    name = input("Player: ")
    if name == "x":
        break
    players.append((name,0))

print(players[0])


def update_player_score():
    for i in range(len(players)):
        print(str(i) + ") " + players[i][0])


    j = 0;
    while True:
        try:
            who = input("Who got it right? (ENTER NUMBER)")
            if who == "q":
                break
            who = int(who)

            tmp = list(players[int(who)])

            tmp[1] += 20;
            players[int(who)] =  tuple(tmp)
        except ValueError:
            print("Please enter an integer!")
            j = j + 1
            if j >= 2:
                print('\a')
                print('\a')
                print('\a')
                print("Can you not count? What a clown!")



#print(res.text)

def player_scores():
    print("LOSERS...")
    for x in players:
        print(x[0] + "=" + str(x[1]) + "\n")



j = 0;
for d in data["results"]:
    for i in range(0,10):
        print("\n")
    question = d["question"]
    ans= d["correct_answer"]
    choices = d["incorrect_answers"]

    print(question)
    print("\n\n");

    options.append(ans)
    for x in choices:
        options.append(x)
    random.shuffle(options)

    for i in range(len(options)):
        print(str(i+1) + " " + options[i])

    q = input()
    if q == "q":
        break
    if q != "s":
        print("THE ANSWER WAS " + ans + "\n");

        update_player_score()
        j += 1 
        if j % 5 == 0:
            player_scores()

    options.clear()
    if j % 2 == 0:
        r = str(random.randint(1,51))
        playsound("adlib/" + r + ".wav")
    

print("\n\n\n\n\n\n\n")

print("THE WINNER IS.....")

st = ""
m = 0
for x in players:
    if x[1] > 0:
        m = x[1]
        st = x[0]

for i in range(0,100):
    print(st)

print(text2art(" THE WINNER IS " + st))
playsound("win.mp3")
player_scores()
playsound("loser.mp3")
