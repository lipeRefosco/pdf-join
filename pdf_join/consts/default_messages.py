from .commands import VALID_COMMANDS
from .options import INPUT_OPTION, OUTPUT_OPTION

help_message =  "[COMMAND] [--OPTION] file1 file2 ... fileN\n\n" + \
                "Commands: {}\n".format(VALID_COMMANDS) + \
                "Options:\n" + \
                "   {}: Insert file path for all files.\n".format(', '.join(INPUT_OPTION)) + \
                "   {}: Path for the output. Default is the same path of program.".format(', '.join(OUTPUT_OPTION))

DEFAULT_MESSAGES = {
    "NO_INPUT_FILES": "Insert files to join PDF's \n" + help_message,
    "INVALID_OPTION": "Invalid option! \n" + help_message,
    "HELP": help_message,
    "NO_COMMAND": "With out command! \n" + help_message
}