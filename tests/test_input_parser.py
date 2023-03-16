import pytest
import sys
sys.path.append('pdf_join')

from pdf_join.utils import input_parser
from pdf_join.exceptions import *
from pdf_join.consts import *

class TestInputExtractor:

    def test_extract_join_command_from_args(self):
        user_inputs = ["join", "-i", "inputFileTest.pdf"]

        expect = {
                    "command": "join",
                    "inputs": {"inputFileTest.pdf"},
                    "output": DEFAULT_OUTPUT_FILENAME
                }
        
        result = input_parser(user_inputs)
        
        assert expect == result
        ...
        

    def test_if_can_parse_the_input_args_to_aplication_format(self):
        user_inputs = ["join", "-i", "inputFileTest.pdf", "-o", "myOutputFile.pdf"]
        
        expect = {
                    "command": "join",
                    "inputs": {"inputFileTest.pdf"},
                    "output": "myOutputFile.pdf"
                }

        result = input_parser(user_inputs)

        assert expect == result
        ...


    def test_if_dont_have_inputs(self):
        user_inputs = []
        
        expect = {"command": None, "inputs": {}, "output": "default.pdf"}
        result = input_parser(user_inputs)
        
        assert expect == result
        ...


    def test_if_extendend_sintax_of_options(self):
        user_inputs = ["--output", "myOutputFile.pdf"]

        expect = {"command": None, "inputs": {}, "output": "myOutputFile.pdf"}
        result = input_parser(user_inputs)
        
        assert expect == result
        ...


    def test_if_dont_have_inputs_and_output_file_was_defined(self):
        user_inputs = ["-o", "myOutputFile.pdf"]

        expect = {"command": None, "inputs": {}, "output": "myOutputFile.pdf"}
        result = input_parser(user_inputs)
        
        assert expect == result
        ...


    def test_if_can_parse_space_scaped_by_terminal(self):
        user_inputs = ["-i", "assets/a4 1.pdf"]
        expect = {"command": None, "inputs": {"assets/a4 1.pdf"}, "output": "default.pdf"}
        
        result = input_parser(user_inputs)

        assert  result == expect
        ...