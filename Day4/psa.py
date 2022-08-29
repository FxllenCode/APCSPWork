# Write a PSA on a random topic
# Screentime is our topic.

screenType: str = input("What kind of screntype are you using? ")
screenType = screenType.lower()


def get_bluelight_from_hours(type: str):
    hours: int = int(input("Okay. How many hours on average do you use it? "))
    if type == "PC":
        print(
            "You should spend no more than 7 hours on the computer. You are currently spending "
            + str(hours - 7)
            + " too many hours."
        )
    if type == "Tablet":
        print(
            "You should not spend more than 4 hours a day on this device. You are currently spending "
            + str(hours - 4)
            + " too many hours on your device."
        )

    if type == "Phone":
        print(
            "You should not spend more than 2 hours a day on this device. You are currently spending "
            + str(hours - 2)
            + " too many hours on this device."
        )


if screenType == "computer":
    get_bluelight_from_hours("PC")
elif screenType == "tablet":
    get_bluelight_from_hours("Tablet")
elif screenType == "phone":
    get_bluelight_from_hours("Phone")
else:
    print("Sorry. I don't know what that device is yet.")
    exit