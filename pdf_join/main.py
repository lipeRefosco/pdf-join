from sys import argv

from consts import DEFAULT_MESSAGES, USER_INPUT_START, EXEC_COMMAND
from exceptions import *
from utils import input_parser

def main(user_args):
        user_input = input_parser(user_args[USER_INPUT_START:])
        
        has_command = user_input["command"] != None
        if not has_command:
            raise NoCommandException(DEFAULT_MESSAGES.get("NO_COMMAND"))
        
        has_inputs_files = len(user_input["inputs"]) > 0
        if not has_inputs_files:
             raise NoInputFilesException(DEFAULT_MESSAGES.get("NO_INPUT_FILES"))

        # TODO: Verify if the output file inserted by user, already exist on file system
        EXEC_COMMAND[user_input.get("command")](user_input)


if __name__ == "__main__":
    try:
        main(argv)
    except Exception as exception:
        print(exception.message)
        
