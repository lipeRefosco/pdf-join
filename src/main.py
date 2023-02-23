from sys import argv

PARAMS = ["-o"]

def extractFromInput(inputsUser) -> dict:
    inputFiles = []
    outputFile = "default.pdf"
    state = "default"

    for input in inputsUser[1:]:
        
        if PARAMS.__contains__(input):
            state = input
            continue

        match (state):
            case "-o":
                outputFile = input
                state = "default"
                break
        
        inputFiles.append(input)
    
    return {
        "inputs" : inputFiles,
        "output" : outputFile,
    }
    ...

if __name__ == "__main__":

    userInput = extractFromInput(argv)
    print(userInput)
    print(type(PARAMS))