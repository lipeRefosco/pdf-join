import pytest

from pdf_join.consts import *
from pdf_join.exceptions import *
from pdf_join.utils import *
from pdf_join.main import main

class TestProgram:

    def test_when_dont_have_inputs(self):
        with pytest.raises(Exception) as e_info:
           terminal_argv = ["mainFile.py", "join"]
           a = main(terminal_argv)
           print(a)
        
        assert e_info.typename == (NoInputFilesException.__name__)
        ...


    def test_when_dont_have_command(self):
        with pytest.raises(Exception) as e_info:
           terminal_argv = ["mainFile.py", "-i", "file1.pdf", "file2.pdf"]
           main(terminal_argv)

        assert e_info.typename == NoCommandException.__name__
        ...


    def test_when_has_invalid_option(self):
        with pytest.raises(Exception) as e_info:
            terminal_argv = ["mainFile.py", "-i", "file1.pdf", "-a", "myOutput.pdf"]
            main(terminal_argv)

        assert e_info.typename == InvalidOptionException.__name__
        ...


    def test_non_expected_option(self):
        with pytest.raises(Exception) as e_info:
            terminal_argv = ["mainFile.py", "-a", "myOutputFile.pdf"]
            main(terminal_argv)
        
        assert e_info.typename == InvalidOptionException.__name__
        ...
    
    
    def test_bad_option_inserted(self):
        with pytest.raises(Exception) as e_info:
            terminal_argv = ["mainFile.py", "-output", "myOutputFile.pdf"]
            main(terminal_argv)

        assert e_info.typename == InvalidOptionException.__name__
        ...
    
    def test_when_has_help_option(self):
        with pytest.raises(Exception) as e_info:
            terminal_argv = ["mainFile.py", "-h"]
            main(terminal_argv)

        assert str(e_info.value).__contains__(DEFAULT_MESSAGES.get("HELP"))