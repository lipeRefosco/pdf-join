class InputFilesExceptions(Exception):

    def __init__(self, message: str) -> None:
        self.message = message