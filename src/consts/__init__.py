from .default_messages import DEFAULT_MESSAGES

# Param and statements
OPTION_SINTAX = "-" or "--"
DEFAULT_OUTPUT_STATE = ["-o", "--output"]
STATES = {
    "DEFAULT" : ["default"],
    "OUTPUT"  : DEFAULT_OUTPUT_STATE
}
ALL_PARAMS = [*DEFAULT_OUTPUT_STATE]

# Default 
DEFAULT_OUTPUT_FILENAME =  "default.pdf"
USER_INPUT_START = 1