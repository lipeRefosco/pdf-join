import pytest
import sys
sys.path.append('src')

from src.utils import input_parser
from src.exceptions import InputFilesException
from src.consts import *

class TestInputExtractor:

    def test_extract_join_command_from_args(self):
        terminalArgs = ["pythonFile.py", "join", "inputFileTest.pdf"]

        expect = {
                    "commands": "join",
                    "inputs": ["inputFileTest.pdf"],
                    "output": DEFAULT_OUTPUT_FILENAME
                }
        
        result = input_parser(terminalArgs)
        
        assert expect == result
        ...
        

    def test_if_can_parse_the_input_args_to_aplication_format(self):
        terminalArgs = ["pythonFile.py", "join", "inputFileTest.pdf", "-o", "myOutputFile.pdf"]
        
        expect = {
                    "commands": "join",
                    "inputs": ["inputFileTest.pdf"],
                    "output": "myOutputFile.pdf"
                }

        result = input_parser(terminalArgs)

        assert expect == result
        ...


    def test_if_dont_have_inputs(self):
        terminalArgs = ["pythonFile.py"]
        
        expect = {"commands": None, "inputs": [], "output": "default.pdf"}
        result = input_parser(terminalArgs)
        
        assert expect == result


    def test_if_extendend_sintax_of_options(self):
        terminalArgs = ["pythonFile.py", "--output", "myOutputFile.pdf"]

        expect = {"commands": None, "inputs": [], "output": "myOutputFile.pdf"}
        result = input_parser(terminalArgs)
        
        assert expect == result
        ...


    def test_if_dont_have_inputs_and_output_file_was_defined(self):
        terminalArgs = ["pythonFile.py", "-o", "myOutputFile.pdf"]

        expect = {"commands": None, "inputs": [], "output": "myOutputFile.pdf"}
        result = input_parser(terminalArgs)
        
        assert expect == result
        ...

    
    def test_non_expected_option(self):
        with pytest.raises(Exception) as e_info:
            terminalArgs = ["pythonFile.py", "-a", "myOutputFile.pdf"]
            input_parser(terminalArgs)
        
        assert str(e_info.value).__contains__(DEFAULT_MESSAGES.get("INVALID_OPTION"))
        ...
    
    def test_bad_option_inserted(self):
        with pytest.raises(Exception) as e_info:
            terminalArgs = ["pythonFile.py", "-output", "myOutputFile.pdf"]
            input_parser(terminalArgs)

        assert str(e_info.value).__contains__(DEFAULT_MESSAGES.get("INVALID_OPTION"))
        ...