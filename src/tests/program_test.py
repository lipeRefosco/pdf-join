import pytest

from src.consts import *
from src.exceptions import InputFilesException
from src.utils import *
from main import main

class TestProgram:

    def test_when_dont_have_inputs_and_throw_InputFilesException(self):
        with pytest.raises(Exception) as e_info:
           user_inputs = ["mainFile.py", "join"]
           main(user_inputs)

        assert str(e_info.value).__contains__(DEFAULT_MESSAGES.get("NO_INPUT_FILES"))
        
    def test_when_dont_have_command(self):
        with pytest.raises(Exception) as e_info:
           user_inputs = ["mainFile.py", "file1.pdf", "file2.pdf"]
           main(user_inputs)

        assert str(e_info.value).__contains__(DEFAULT_MESSAGES.get("NO_COMMAND"))
        