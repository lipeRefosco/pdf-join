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


OPTIONS_HANDLER = {
    "-i": input_handler,
    "--input": input_handler,
    "-o": output_handler,
    "--output": output_handler,
    "-h": help_handler,
    "--help": help_handler
}
