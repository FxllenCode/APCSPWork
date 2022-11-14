import csv
from termcolor import cprint
from prettytable import PrettyTable

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
# TODO: Rewrite using classes


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


# Create a function that will be called inside the Command class that uses PrettyTable to display the data in a table that was given to the user through the arguments of the Command class
def search(field: str, value: str):
    table = PrettyTable()
    table.field_names = rows[0].keys()
    for row in rows:
        if row[field.lower()] == value:
            table.add_row(row.values())
    print(table)


# Create a function that will be called inside the Command class, for a command that will find the average number of fatalities in a given year
def average_fatalities(year: str):
    total_fatalities = 0
    total_incidents = 0
    for row in rows:
        if row["date"][0:4] == year:
            total_incidents += 1

            if row["fatal"] != "" or row["fatal"] != "0":
                total_fatalities += int(row["fatal"])

    print(
        f"Average fatalities per incident in {year}: {total_fatalities / total_incidents}"
    )


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
            "search",
            "Searches for a value in a field",
            ["field", "value"],
            search,
        )
    )
    commands.append(
        Command(
            "average_fatalities",
            "Finds the average number of fatalities in a given year",
            ["year"],
            average_fatalities,
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
    parse_args(input("Enter a command: <command> <value?> <flag?> "))
