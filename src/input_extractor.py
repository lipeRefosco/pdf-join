from consts import *
from exceptions.default_messages import *
from exceptions.InputFilesExceptions import InputFilesExceptions


def input_extractor(inputsUser: list) -> dict:
    inputFiles = []
    outputFile = DEFAULT_OUTPUT_FILENAME
    state = STATES.get("DEFAULT")

    for input in inputsUser[USER_INPUT_START:]:

        if input_is_option(input) and not options_is_valid(input):
            raise InputFilesExceptions(DEFAULT_MESSAGES.get("INVALID_OPTION"))

        if options_is_valid(input):
            state = input
            continue

        if DEFAULT_OUTPUT_STATE.__contains__(state):
            outputFile = input
            state = STATES.get("DEFAULT")
            continue

        inputFiles.append(input)
        continue

    return {
        "inputs" : inputFiles,
        "output" : outputFile,
    }

def input_is_option(input: str) -> bool:
    return input.__contains__(OPTION_SINTAX)

def options_is_valid(input: str) -> bool:
    return ALL_PARAMS.__contains__(input)
