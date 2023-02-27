from sys import argv

from input_extractor import input_extractor
from exceptions.InputFilesExceptions import InputFilesExceptions
from exceptions.default_messages import *

if __name__ == "__main__":
    try:
        userInput = input_extractor(argv)
        
        have_input_files = len(userInput.get("inputs")) > 0

        if not have_input_files:
            raise InputFilesExceptions(DEFAULT_MESSAGES.get("NO_INPUT_FILES"))
        
        # TODO: Verify if the output file inserted by user, already exist on file system
        print(userInput)

    except InputFilesExceptions as exception:
        print(exception.message)
        
