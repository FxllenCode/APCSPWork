import requests

API_KEY = "343ec4d6edfff95dd5a8466f3e4837d5"
flightNumber = input(
    "Welcome to the flight lookup tool! What's the flight number you want to lookup? (ex: DAL23) "
)

isFlying = input("Okay. Is the flight currently active? (y/n) ")

if isFlying == "y":
    print("Roger, standby. We are looking this up in our database...")
    response = requests.get(
        "http://api.aviationstack.com/v1/flights?access_key="
        + API_KEY
        + "&flight_icao="
        + flightNumber
    )
    data = response.json()
    if data["pagination"]["total"] == 0:
        print("Sorry! There is not a flight with the number " + flightNumber + "!")
    elif data["data"][0]["live"] is None:
        print(
            "Okay. We've found some information for that flight, but we cannot figure out what aircraft it's using.\n\nThat flight is currently "
            + data["data"][0]["flight_status"]
            + " on "
            + data["data"][0]["flight_date"]
            + ". It is departing from "
            + data["data"][0]["departure"]["airport"]
            + ". Its arrival is "
            + data["data"][0]["arrival"]["airport"]
            + "."
        )

    elif data["data"][0]["aircraft"] is None:
        print(
            "Okay. We've found some information for that flight, but we cannot figure out what aircraft it's using.\n\nThat flight is currently "
            + data["data"][0]["flight_status"]
            + " on "
            + data["data"][0]["flight_date"]
            + ". It is departing from "
            + data["data"][0]["departure"]["airport"]
            + ". Its arrival is "
            + data["data"][0]["arrival"]["airport"]
            + "."
        )

    else:
        picture = input(
            "Okay, we've found a flight with that information. Do you want to see a picture of the aircraft? (y/n)"
        )
        if picture == "y":

            URL = str(
                "https://api.planespotters.net/pub/photos//hex/"
                + data["data"][0]["aircraft"]["icao24"]
                + "?reg="
                + data["data"][0]["aircraft"]["registration"]
            )
            print(
                "Okay. We've found some information for that flight.\n\nThat flight is currently "
                + data["data"][0]["flight_status"]
                + " on "
                + data["data"][0]["flight_date"]
                + ". It is departing from "
                + data["data"][0]["departure"]["airport"]
                + ". Its arrival is "
                + data["data"][0]["arrival"]["airport"]
                + ". We've also found a picture of that aircraft. You can find a planespotting photo at\n\n"
                + URL
            )

        if picture == "n":
            print(
                "Okay. We've found some information for that flight.\n\nThat flight is currently "
                + data["data"][0]["flight_status"]
                + " on "
                + data["data"][0]["flight_date"]
                + ". It is departing from "
                + data["data"][0]["departure"]["airport"]
                + ". Its arrival is "
                + data["data"][0]["arrival"]["airport"]
                + ". We know what kind of aircraft that is, but you do not want a photo."
            )
else:
    print("Sadly, we cannot track that aircraft right now.")
