# Creating File Handlers and Modules for Retrieving Information about Insulin
# Create a module
# Open a file and load the JSON data it contains using the built-in JSON module of Python
# Parse the JSON structure to access insulin data
# Calculate the rough molecular weight of human insulin using given code (similar to the lab Working with the String Sequence and Numeric Weight of Insulin in Python)

# Exercise 1: Creating the JSON molecules data file

# Exercise 2: Creating the JSON file handler module

# import json

# def readJsonFile(fileName):
#     data = ""
#     try:
#         with open(fileName) as json_file:
#             data = json.load(json_file)
#     except IOError:
#         print("Could not read file")
#     return data
    

# Exercise 3: Creating the main program
import lab14_jsonFileHandler
data: str = lab14_jsonFileHandler.readJsonFile('python-lab/files/insulin.json')

if data != "" :
    bInsulin: str = data['molecules']['bInsulin']
    aInsulin: str = data['molecules']['aInsulin']
    insulin: str = bInsulin + aInsulin
    molecularWeightInsulinActual: float = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
    # Calculating the molecular weight of insulin  
    # Getting a list of the amino acid (AA) weights  
    aaWeights: float = data['weights']
    # Count the number of each amino acids  
    aaCountInsulin: dict = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
    # Multiply the count by the weights  
    molecularWeightInsulin: float = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
    print("The rough molecular weight of insulin: " +
    str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))   
else:
    print("Error. Exiting program")


    
# <output>
# bInsulin: fvnqhlcgshlvealylvcgergffytpkt
# aInsulin: giveqcctsicslyqlenycn
# molecularWeightInsulinActual: 5807.63
# The rough molecular weight of insulin: 6696.420000000001
# Percent error: 15.30383306099047

