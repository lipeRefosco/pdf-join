import pytest

from src.consts import *
from src.exceptions import *
from src.utils import *
from src.main import main

class TestProgram:

    def test_when_dont_have_inputs_and_throw_InputFilesException(self):
        with pytest.raises(Exception) as e_info:
           user_inputs = ["mainFile.py", "join"]
           main(user_inputs)

        assert e_info.typename.__contains__(InputFilesException.__name__)
        ...


    def test_when_dont_have_command(self):
        with pytest.raises(Exception) as e_info:
           user_inputs = ["mainFile.py", "file1.pdf", "file2.pdf"]
           main(user_inputs)

        assert e_info.typename.__contains__(NoCommandException.__name__)
        ...


    def test_when_has_invalid_option(self):
        with pytest.raises(Exception) as e_info:
            user_inputs = ["mainFile.py", "file1.pdf", "-a", "myOutput.pdf"]
            main(user_inputs)

        assert e_info.typename.__contains__(InvalidOptionException.__name__)
        ...
        