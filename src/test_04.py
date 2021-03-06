"""
You are given two strings, str_1 and str_2, where str_2 is generated by randomly shuffling str_1 and then adding one letter at a random position.

Write a function that returns the letter that was added to str_2.

Examples:

csFindAddedLetter(str_1 = "bcde", str_2 = "bcdef") -> "f"
csFindAddedLetter(str_1 = "", str_2 = "z") -> "z"
csFindAddedLetter(str_1 = "b", str_2 = "bb") -> "b"
csFindAddedLetter(str_1 = "b", str_2 = "bb") -> "b"
Notes:

str_1 and str_2 both consist of only lowercase alpha characters.
[execution time limit] 4 seconds (py3)

[input] string str_1

[input] string str_2

[output] string

"""

def csFindAddedLetter(str_1, str_2):

    smallStr = "" 
    largeStr = "" 
      
    # Determine string with extra character 
    if(len(str_1) > len(str_2)): 
        smallStr = str_2 
        largeStr = str_1 
    else: 
        smallStr = str_1
        largeStr = str_2
    smallStrCodeTotal = 0
    largeStrCodeTotal = 0
    i = 0
      
    # Add Character codes of both the strings 
    while(i < len(smallStr)): 
        smallStrCodeTotal += ord(smallStr[i]) 
        largeStrCodeTotal += ord(largeStr[i]) 
        i += 1
      
    # Add last character code of large string 
    largeStrCodeTotal += ord(largeStr[i]) 
      
    # Minus the character code of smaller string  
    # from the character code of large string 
    # The result will be the extra character code 
    intChar = largeStrCodeTotal - smallStrCodeTotal    
    return chr(intChar) 

    print(csFindAddedLetter(bcde, str_2 = "bcdef"))
    # print(csFindAddedLetter(str_1 = "", str_2 = "z"))
    # print(csFindAddedLetter(str_1 = "b", str_2 = "bb"))
    # print(csFindAddedLetter(str_1 = "b", str_2 = "bb"))
