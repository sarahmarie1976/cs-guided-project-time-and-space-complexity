"""
Using Big O notation, what is the correct classification of time complexity for the function below?

def do_lots_of_things(items):
    last = len(items) - 1
    print(items[last])

    middle = len(items) / 2 
    i = 0
    while i < middle:
        i += 1

    for num in range(100): 
        print(num)    


A - O(n^2)

B- O(n)

C- O(1)

D- O(log n)


Answer is:

B - O(n)
"""