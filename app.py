import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w): 
    w = w.lower()
    if w in data: 
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        answer = input("Did you mean %s instead? Y for yes, N for No. " % get_close_matches(w, data.keys())[0])
        if answer == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif answer == "N":
            return "The word doesn't exist. Please double check"
        else: 
            return "We didn't understand your query."
    else:
        return "The word doesn't exist. Please double check"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output: 
        print(item)
else:
    print(output)