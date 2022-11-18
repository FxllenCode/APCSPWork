If you are reading this in 2022, hi Coach Heying! Please give me a good grade:)

If you're reading this in 2023 or later, hi from the future! I accidently made an input command parser using classes in python. Basically, a CLI parser, but not a CLI because... well, I had to use input in the project. This is a monorepo from my main GitHub repo, and the framework isn't really documented outside of here. You'll have to copy the code, basically. It isn't that good, but you might find it useful!

## Dependency requirements

`colorama==0.4.4`

That's it! :tada:

## Setup 

```py
from termcolor import cprint

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


# Two example commands - you can make your own commands from here!

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
        Command("help", "Displays g his help menu", [], lambda: help_s(commands))
    )

    return commands

# Parse arguments
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


# Run heart loop

while True:
    parse_args(input("Enter a command: "))

```

This is about it! Pretty cool, right ;)

I don't know how this will ever be useful, but it's a good way to learn object oriented programming, I guess.