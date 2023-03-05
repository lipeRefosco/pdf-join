from consts import *

from exceptions import InputFilesException


def input_parser(inputs_user: list) -> dict:
    commands = None
    output_files = DEFAULT_OUTPUT_FILENAME
    input_files = []
    state = STATES.get("DEFAULT")

    for user_input in inputs_user[USER_INPUT_START:]:

        if input_is_command(user_input):
            commands = user_input
            continue

        if input_is_option(user_input):
            if not options_is_valid(user_input):
                raise InputFilesException(DEFAULT_MESSAGES.get("INVALID_OPTION") + ": " + user_input)

            if options_is_valid(user_input):
                state = user_input
                continue

        if OUTPUT_OPTIONS.__contains__(state):
            output_files = user_input
            state = STATES.get("DEFAULT")
            continue

        input_files.append(user_input)
        continue

    return {
        "commands": commands,
        "inputs": input_files,
        "output": output_files
    }

def input_is_option(input: str) -> bool:
    return input.__contains__(OPTION_SINTAX)


def input_is_command(input_user: str):
    return COMMANDS.__contains__(input_user)


def options_is_valid(input: str) -> bool:
    return ALL_PARAMS.__contains__(input)

