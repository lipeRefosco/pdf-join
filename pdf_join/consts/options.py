from exceptions import * 
from .default_messages import *

# Param and statements
OPTION_SINTAX = "-" or "--"
OUTPUT_OPTION = ["-o", "--output"]
INPUT_OPTION = ["-i", "--input"]


def help_handler() -> None:
    raise Exception(DEFAULT_MESSAGES.get("help"))


def output_handler(next_inputs: list, parsed_input: dict) -> None:
    parsed_input["output"] = next_inputs[0]
    return


def input_handler(next_inputs: list, parsed_input: dict) -> None:
    for next_input in next_inputs:
        if next_input.__contains__(OPTION_SINTAX):
            break
        parsed_input["inputs"].add(next_input)
    return


# First indice is the short name and the second 
OPTIONS_HANDLER = {
    INPUT_OPTION[0]: input_handler,
    INPUT_OPTION[1]: input_handler,
    OUTPUT_OPTION[0]: output_handler,
    OUTPUT_OPTION[1]: output_handler,
    "-h": help_handler,
    "--help": help_handler
}
