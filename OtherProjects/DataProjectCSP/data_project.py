import csv
from termcolor import cprint
from prettytable import PrettyTable

# pip -r requirements.txt
# python3 data_project.py
reader = csv.DictReader(open("AviationData.csv"))
rows: list = []

for row in reader:
    rows.append(row)

# Setup different types of output colors and details using cprint and colored from termcolor


def normal_output(x):
    cprint(x, "white", "on_grey")


def warning_output(x):
    cprint(x, "yellow", "on_grey")


def error_output(x):
    cprint(x, "red", attrs=["bold", "reverse"])


def heading_output(x):
    cprint(x, "blue", attrs=["bold", "underline"])


def data_output(x):
    cprint(x, "green", attrs=["bold"])


def important_output(x):
    cprint(x, "blue", attrs=["bold", "reverse", "blink"])


# Argument parser to simply creation of "commands" and "flags" for the program
# TODO: Rewrite using classes done!


class Command:
    def __init__(self, name, description, args, func):
        self.name: str = name
        self.description: str = description
        self.args: list[str] = args
        self.func = func

    def help(self):
        heading_output(self.name)
        print(f"Description: {self.description.splitlines()[0]}")
        print(f"Arguments: {self.args} \n")


def help_s(commands: list[Command]):
    important_output("Commands: \n")
    for command in commands:
        command.help()


def fatalities(type: str, year: str):
    if type == "average":
        total = 0
        count = 0
        for row in rows:
            if row["date"][:4] == year:
                if row["fatal"] != "" and (
                    isinstance(row["fatal"], int) or row["fatal"].isnumeric()
                ):
                    total += int(row["fatal"])
                    count += 1
        data_output(
            f"Average fatalities per accident in {year}: {round(total / count, 2)}"
        )
    elif type == "total":
        total = 0
        for row in rows:
            if row["date"][:4] == year:
                if row["fatal"] != "" and (
                    isinstance(row["fatal"], int) or row["fatal"].isnumeric()
                ):
                    total += int(row["fatal"])
        data_output(f"Total fatalities in {year}: {total}")


def accidents(year: str):
    count = 0
    for row in rows:
        if row["date"][:4] == year:
            count += 1
    data_output(f"Number of accidents in {year}: {count}")


def registration(reg: str):
    table = PrettyTable()
    table.field_names = ["Date", "Location", "Aircraft", "Damage"]
    for row in rows:
        if row["registration"].lower() == reg:
            table.add_row(
                [
                    row["date"],
                    row["location"],
                    row["make"] + " " + row["model"],
                    row["damage"],
                ]
            )
    print(table)


def aircraft_manufacturer(make: str):
    table = PrettyTable()
    table.field_names = ["Make", "Number of Accidents"]
    number_of_accidents = 0
    for row in rows:
        if row["make"].lower() == make:
            number_of_accidents += 1

    table.add_row([make, number_of_accidents])

    print(table)


def register_commands():
    commands = []
    commands.append(
        Command(
            "exit",
            "Exits the program",
            [],
            lambda: warning_output("Exiting...") + exit(),
        )
    )
    commands.append(
        Command(
            "fatalities",
            "Finds the average number of fatalities in a given year",
            ["type", "year"],
            fatalities,
        )
    )
    commands.append(
        Command(
            "accidents",
            "Finds the number of accidents in a given year",
            ["year"],
            accidents,
        )
    )
    commands.append(
        Command(
            "registration",
            "Finds the type of damage and type of aircraft a certain registration was involved in",
            ["registration"],
            registration,
        )
    )
    commands.append(
        Command(
            "aircraft_manufacturer",
            "Finds the amount of accidents for each aircraft manufucturer",
            ["make"],
            aircraft_manufacturer,
        )
    )

    commands.append(
        Command("help", "Displays this help menu", [], lambda: help_s(commands))
    )

    return commands


def parse_args(input: str):
    cmds: list[Command] = register_commands()
    input = input.lower()
    args = input.split(" ")
    for cmd in cmds:
        if args[0] == (None or ""):
            return
        if cmd.name == args[0]:
            if len(args) - 1 == len(cmd.args):
                cmd.func(*args[1:])
            else:
                error_output("Invalid number of arguments")
                cmd.help()
            return


heading_output("Welcome to the NTSB lookup tool!")
normal_output("This tool will allow you to search for aviation accidents by keyword.")

while True:
    parse_args(input("Enter a command: "))
