import json

def readJsonFile(fileName) -> str:
    data: str | None = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data