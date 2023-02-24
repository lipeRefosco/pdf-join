from sys import argv

from inputExtractor import inputExtractor
from exceptions.InputFilesExceptions import InputFilesExceptions

if __name__ == "__main__":
    try:
        userInput = inputExtractor(argv)
        
        if len(userInput.get("inputs")) == 0:
            raise InputFilesExceptions("Insert files to join PDF's")
        
        print(userInput)

    except InputFilesExceptions as exception:
        print(exception.message)
        
