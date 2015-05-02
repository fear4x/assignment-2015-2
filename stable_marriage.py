import json
import sys
from pprint import pprint

def GaleShapely(men, women):
    state = {}
    for man in men:
        state[man] = {}
        state[man]["free"] = 1
        state[man]["last_proposed"] = 0;
    for woman in women:
        state[woman] = {}
        state[woman]["free"] = 1
    
    free_men = len(men)
    while (free_men > 0):
        for man in men:
            if (state[man]["free"] == 1):
                woman = men[man][state[man]["last_proposed"]]
                state[man]["last_proposed"] += 1
                if (state[woman]["free"] == 1):
                    state[man]["free"] = 0
                    state[woman]["free"] = 0
                    state[woman]["partner"] = man
                    free_men -= 1
                elif (women[woman].index(man) < women[woman].index(state[woman]["partner"])):
                    state[state[woman]["partner"]]["free"] = 1
                    state[woman]["partner"] = man
                    state[man]["free"] = 0
    result = {}
    for man in men:
        for woman in women:
            if (state[woman]["partner"] == man):
               result[man] = woman; 
    return result

if (len(sys.argv) > 2):
    input_file = open(sys.argv[2])
    data = json.load(input_file)
    if (sys.argv[1] == "-m"):
        result = GaleShapely(data["men_rankings"], data["women_rankings"])
    elif (sys.argv[1] == "-w"):
        result = GaleShapely(data["women_rankings"], data["men_rankings"])
    else:
        print("Input Error")
        exit
    if (len(sys.argv) > 3):
        output_file = open(sys.argv[3], 'w')
        json.dump(result, output_file)
        output_file.close()
        pprint(result)
    else:
        pprint(result)
else:
    print("Not enough command line arguments.")
