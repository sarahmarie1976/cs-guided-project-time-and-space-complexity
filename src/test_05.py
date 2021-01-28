"""
Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.

Examples:

csFirstUniqueChar(input_str = "lambdaschool") -> 2
csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
csFirstUniqueChar(input_str = "vvv") -> -1
Notes:

input_str will only contain lowercase alpha characters.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] integer

"""

def csFirstUniqueChar(input_str):
    check = {}
    for i in input_str:
        check[i] = check.get(i, 0) +1
    for i, j in enumerate(input_str):
        if check[j] == check[j] == 1:
            return i

print(csFirstUniqueChar(input_str = "lambdaschool"))  
print(csFirstUniqueChar(input_str = "ilovelambdaschool"))   
print(csFirstUniqueChar(input_str = "vvv"))
