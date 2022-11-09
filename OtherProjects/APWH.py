# Choose your adventure game for APWH!

score = 0 # For every "wrong" answer, you get 0 points. For every "right" answer, you get 1 point. For the "okay" answer, you get 0.5 points.

print("Welcome to the Choose Your Adventure Game for APWH!")
print("You will be given a scenario and you will have to choose what you would do in that situation.")
country_name = input("What is your country's name? ")
print("Your country is " + country_name + ". You are the leader of this maritime empire. It is up to you to make decisions that will affect your country's future. You will be given a scenario and you will have to choose what you would do in that situation. You will be given three choices. You will get 1 point for every right answer and 0.5 points for every okay answer. You will get 0 points for every wrong answer. You will get a total of 5 points. Good luck!")
print("Question 1: The first step to building a maritime empire is to choose the type of ship you will get. Let's start out with the basic design. Will your ship be just for trading (1), just for fighting (2), or convertible (3)?")
answer1 = input("What is your answer? (1/2/3)")
if answer1 == "1":
    print("You chose just for trading. You will get 1 point.")
    score = score + 1
elif answer1 == "2":
    print("You chose just for fighting. You will get 0 points.")
    score = score + 0
elif answer1 == "3":
    print("You chose convertible. You will get 0.5 points.")
    score = score + 0.5
else: 
    print("You did not enter a valid answer. You will get 0 points.")
    score = score + 0
print("Question 2: Now that the basic structure has been designed, it's time to choose a type of sail. Will your ship have a square sail (1), a lateen sail (2), or a triangular sail (3)?")
answer2 = input("What is your answer? (1/2/3)")
if answer2 == "1":
    print("You chose square sail. You will get 0 points.")
    score = score + 0
elif answer2 == "2":
    print("You chose lateen sail. You will get 1 point.")
    score = score + 1
elif answer2 == "3":
    print("You chose triangular sail. You will get 0.5 points.")
    score = score + 0.5
else:
    print("You did not enter a valid answer. You will get 0 points.")
    score = score + 0
print("Question 3: You now have a fleet of ships, ready to sail the oceans! But first, you must decide why you are sailing. Will you sail to trade (1), to fight (2), or to explore (3)?")
answer3 = input("What is your answer? (1/2/3)")
if answer3 == "1":
    print("You chose to trade. You will get 1 point.")
    score = score + 1
elif answer3 == "2":
    print("You chose to fight. You will get 0 points.")
    score = score + 0
elif answer3 == "3":
    print("You chose to explore. You will get 0.5 points.")
    score = score + 0.5
print("Question 4: With the reason for sailing decided, you need to figure out who will pay for it. Will you set up a fund for other wealthy owners to help fund exploration (1), will you tax your country's citizens (2), or will the state sponsor the exploration (3)?")
answer4 = input("What is your answer? (1/2/3)")
if answer4 == "1":
    print("You chose to set up a fund. You will get 0.5 points.")
    score = score + 0.5
elif answer4 == "2":
    print("You chose to tax your country's citizens. You will get 0 points.")
    score = score + 0
elif answer4 == "3":
    print("You chose to have the state sponsor the exploration. You will get 1 point.")
    score = score + 1

print("Question 5: You have now set up your fleet and you are ready to sail! But first, you must figure out how to navigate the oceans. Will you use the a compass (1), an astrolabe (2), or an estimated guess (3)?")
answer5 = input("What is your answer? (1/2/3)")
if answer5 == "1":
    print("You chose to use a compass. You will get 0.5 points.")
    score = score + 0.5
elif answer5 == "2":
    print("You chose to use an astrolabe. You will get 1 point.")
    score = score + 1
elif answer5 == "3":
    print("You chose to use an estimated guess. You will get 0 points.")
    score = score + 0

print("Question 6: Now, it is time to figure out what you will do when you reach your destination. Will you establish trading posts with the natives (1), fight with the natives (2), or explore the land (3)?")
answer6 = input("What is your answer? (1/2/3)")
if answer6 == "1":
    print("You chose to establish trading posts with the natives. You will get 1 point.")
    score = score + 1
elif answer6 == "2":
    print("You chose to fight with the natives. You will get 0 points.")
    score = score + 0
elif answer6 == "3":
    print("You chose to explore the land. You will get 0.5 points.")
    score = score + 0.5

print("Question 7: You have now reached your destination. You have explored the land and have established trading posts with the natives. But now, you must decide what to do next. Will you return home (1), force them to pay tribute (2), or enslave them and send them to the Americas (3)?") # DISCLAIMER: I DO NOT CONDONE THIS, THIS IS HISTORICALLY ACCURATE HOWEVER :(
answer7 = input("What is your answer? (1/2/3)")
if answer7 == "1":
    print("You chose to return home. You will get 0 points.")
    score = score + 0
elif answer7 == "2":
    print("You chose to force them to pay tribute. You will get 0.5 points.")
    score = score + 0.5
elif answer7 == "3":
    print("You chose to enslave them and send them to the Americas. You will get 1 point.")
    score = score + 1



if score == 7:
    print("You got a perfect score! You are a great leader!")
elif score >= 5:
    print("You did pretty well! You are a good leader!")
elif score >= 3:
    print("You did okay. You are an okay leader.")
elif score >= 1:
    print("You did not do very well. You are a bad leader.")
