import pytest

from utils import input_extractor
from exceptions import InputFilesExceptions

class TestInputExtractor:


    def test_if_can_parse_the_input_args_to_aplication_format(self):
        terminalArgs = ['pythonFile.py', 'inputFileTest.pdf', '-o', 'myOutputFile.pdf']
        
        expect = {'inputs': ['inputFileTest.pdf'], 'output': 'myOutputFile.pdf'}
        result = input_extractor(terminalArgs)

        assert expect == result
        ...


    def test_if_dont_have_inputs(self):
        terminalArgs = ['pythonFile.py']
        
        expect = {'inputs': [], 'output': 'default.pdf'}
        result = input_extractor(terminalArgs)
        
        assert expect == result


    def test_if_extendend_sintax_of_options(self):
        terminalArgs = ['pythonFile.py', '--output', 'myOutputFile.pdf']

        expect = {'inputs': [], 'output': 'myOutputFile.pdf'}
        result = input_extractor(terminalArgs)
        
        assert expect == result


    def test_if_dont_have_inputs_and_output_file_was_defined(self):
        terminalArgs = ['pythonFile.py', '-o', 'myOutputFile.pdf']

        expect = {'inputs': [], 'output': 'myOutputFile.pdf'}
        result = input_extractor(terminalArgs)
        
        assert expect == result
    
    
    def test_non_expected_option(self):
        with pytest.raises(InputFilesExceptions):
            terminalArgs = ['pythonFile.py', '-a', 'myOutputFile.pdf']
            input_extractor(terminalArgs)
    
    
    def test_bad_option_inserted(self):
        with pytest.raises(InputFilesExceptions):
            terminalArgs = ['pythonFile.py', '-output', 'myOutputFile.pdf']
            input_extractor(terminalArgs)

        