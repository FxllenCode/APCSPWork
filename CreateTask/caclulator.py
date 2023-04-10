from termcolor import cprint
import math

# Setup different types of output colors and details using cprint and colored from termcolor
# Feel free to change these to your liking!

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

# Command class - heart of the "framework"
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


# Convert 
def rectangular_to_polar(x, y):
    x = float(x)
    y = float(y)
    r = math.sqrt(x * x + y * y)
    theta = math.atan(y / x)

    if x > 0 and y > 0:
        theta = theta

    elif x < 0 and y > 0:
        theta = math.pi - theta
    
    elif x < 0 and y < 0:
        theta = math.pi + theta

    elif x > 0 and y < 0:
        theta = 2 * math.pi - theta

    # convert theta to degrees
    theta = math.degrees(theta)

    data_output(f"{round(r, 0)}(cos({int(round(theta, 2))}) + isin({round(theta, 2)}))")

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
        Command("help", "Displays this help menu", [], lambda: help_s(commands))
    )

    commands.append(
        Command("rect_to_polar", "Converts rectangular coordinates to polar coordinates", ["x", "y"], rectangular_to_polar)
    )

    return commands

# Parse arguments
def parse_args(input: str):
    cmds: list[Command] = register_commands()
    input = input.lower()
    args = input.split(" ")
    for cmd in cmds:
        if args[0] == (None or ""):
            return warning_output("No command entered.")
        elif not args[0] in [cmd.name for cmd in cmds]:
            return warning_output("Command " + "\"" + args[0] + "\"" + " not found!")
        elif cmd.name == args[0]:
            if len(args) - 1 == len(cmd.args):
                cmd.func(*args[1:])
            else:
                error_output("Invalid number of arguments")
                cmd.help()
            return


# Run heart loop

while True:
    parse_args(input("Enter a command: "))
