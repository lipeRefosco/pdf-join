"""Commands executions"""
from commands import join


JOIN_CMD = join.__name__
VALID_COMMANDS = [JOIN_CMD]

EXEC_COMMAND = {
    JOIN_CMD: join
}
