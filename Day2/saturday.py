# Saturday Project (messy if-statement hell)

tempature = int(input("How hot in degrees (F) is it? "))
weatherConditions = input("Is there a risk of a rainstorm today? Yes or No? ")

OUTPUT = "this should never happen"  # if this happens your code is broken


if tempature >= 95:
    OUTPUT = "Stay inside and watch a movie! It's too hot."
elif tempature >= 80 and tempature <= 95:
    OUTPUT = "Go swimming. That should keep you cool."
elif tempature >= 65 and tempature <= 80:
    OUTPUT = "It's not too hot. You can go play tennis safely"
elif tempature >= 40 and tempature <= 65:
    OUTPUT = "It's a little chilly. You should go play golf while it's not freezing."
elif tempature >= 20 and tempature <= 40:
    OUTPUT = "It's really cold! You should go skiing!"
else:
    OUTPUT = "It's way too cold to do this! Go inside and sit by a warm fire."

if weatherConditions.lower() == "yes":
    OUTPUT = "It's not safe to go outside right now. Let's stay inside until it's safer! How about you go read a book?"

if weatherConditions.lower() != "yes" and weatherConditions.lower() != "no":
    print(
        "Read the text next time. :D. It says yes OR no, what you said was neither. >:("
    )
print(OUTPUT)


# python needs match statements
