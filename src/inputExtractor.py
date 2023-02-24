from exceptions.InputFilesExceptions import InputFilesExceptions
from consts import *


def inputExtractor(inputsUser: list) -> dict:
    inputFiles = []
    outputFile = DEFAULT_OUTPUT_FILENAME
    state = STATES.get("DEFAULT")

    for input in inputsUser[USER_INPUT_START:]:

        if isOption(input):
            if validOption(input):
                state = input
                continue
            else: raise InputFilesExceptions("Invalid option!")

        if DEFAULT_STATE.__contains__(state):
            outputFile = input
            state = STATES.get("DEFAULT")
            continue

        inputFiles.append(input)
        continue

    return {
        "inputs" : inputFiles,
        "output" : outputFile,
    }

def isOption(input: str) -> bool:
    return input.__contains__(OPTION_SINTAX)

def validOption(input: str) -> bool:
    return PARAMS.__contains__(input)