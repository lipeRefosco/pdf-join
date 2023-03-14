from sys import argv

from consts import DEFAULT_MESSAGES
from exceptions import *
from utils import input_parser

def main(user_args):
        user_input = input_parser(user_args)
        
        has_command = user_input["commands"] != None
        if not has_command:
            raise NoCommandException(DEFAULT_MESSAGES.get("NO_COMMAND"))
        
        not_has_inputs_files = len(user_input["inputs"]) == 0
        if not_has_inputs_files:
             raise InputFilesException(DEFAULT_MESSAGES.get("NO_INPUT_FILES"))

        # TODO: Verify if the output file inserted by user, already exist on file system
        print(user_input)

if __name__ == "__main__":
    try:
        main(argv)
    except InputFilesException as exception:
        print(exception.message)
    
    except NoCommandException as exception:
        print(exception.message)
        
