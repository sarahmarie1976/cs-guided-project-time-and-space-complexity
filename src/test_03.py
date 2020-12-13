"""
Given a sorted array (in ascending order) of integers and a target, write a function that finds the two integers that add up to the target.
def csSortedTwoSum(numbers, target):

Examples:

csSortedTwoSum([3,8,12,16], 11) -> [0,1]
csSortedTwoSum([3,4,5], 8) -> [0,2]
csSortedTwoSum([0,1], 1) -> [0,1]
Notes:

Each input will have exactly one solution.
You may not use the same element twice.
[execution time limit] 4 seconds (py3)

[input] array.integer numbers

[input] integer target

[output] array.integer

"""

def csSortedTwoSum(numbers, target):
    
    # consider each element except last element
    for i in range(len(numbers) - 1):

        # start from i'th element till last element
        for j in range(i + 1, len(numbers)):

            # if desired sum is found, print it and return
            if numbers[i] + numbers[j] == target:
                return [i, j]
              

    # No pair with given sum exists in the list
    # print("Pair not found")
    


# if __name__ == '__main__':

#     numbers = [8, 7, 2, 5, 3, 1]
#     target = 10

   


print(csSortedTwoSum([3,8,12,16], 11))
print(csSortedTwoSum([3,4,5], 8))
print(csSortedTwoSum([0,1], 1))