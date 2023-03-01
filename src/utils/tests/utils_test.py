from utils import input_extractor

def test_input_extractor():
    terminalArgs = ['pythonFile.py', 'inputFileTest.pdf', '-o', 'myOutputFile.pdf']
    expect = {'inputs': ['inputFileTest.pdf'], 'output': 'myOutputFile.pdf'}
    result = input_extractor(terminalArgs)

    assert expect == result
    ...

