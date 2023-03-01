from sys import argv

from consts import *
from exceptions import InputFilesExceptions
from input_extractor import input_extractor

if __name__ == "__main__":
    try:
        userInput = input_extractor(argv)
        
        has_input_files = len(userInput.get("inputs")) > 0

        if not has_input_files:
            raise InputFilesExceptions(DEFAULT_MESSAGES.get("NO_INPUT_FILES"))
        
        # TODO: Verify if the output file inserted by user, already exist on file system
        print(userInput)

    except InputFilesExceptions as exception:
        print(exception.message)
        
