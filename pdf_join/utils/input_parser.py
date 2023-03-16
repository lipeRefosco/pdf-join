from consts import *
from exceptions import *


def input_parser(input_users: list) -> dict:
    parsed = {
        "command" : None,
        "inputs" : set(),
        "output" : DEFAULT_OUTPUT_FILENAME
    }

    for idx, input_user in enumerate(input_users):
        if input_is_command(input_user):
            parsed["command"] = input_user
            continue
        
        if input_is_option(input_user):
            if not valid_option(input_user):
                raise InvalidOptionException(DEFAULT_MESSAGES.get("INVALID_OPTION"))
            
            next_inputs = idx + 1
            has_more_inputs = len(input_users[next_inputs:]) > 0
            
            if has_more_inputs:
                option_handler = OPTIONS_HANDLER.get(input_user)
                option_handler(input_users[next_inputs:], parsed)
            continue
        ...

    parsed["inputs"] = parsed["inputs"] if len(parsed["inputs"]) > 0 else {}
    
    return parsed


def input_is_option(input_user: str) -> bool:
    return input_user.__contains__(OPTION_SINTAX)


def valid_option(option: str) -> bool:
    return VALID_OPTIONS.__contains__(option)


def input_is_command(input_user: str) -> bool:
    return COMMANDS.__contains__(input_user)