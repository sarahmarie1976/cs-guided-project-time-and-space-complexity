"""
def do_couple_of_things(n):
    my_list = []
    my_second_list = [0] + 26

    for _ in range(n):
        my_list.append("lambda")
        print(my_second_list[n % 25])

    return my_list   


A- O(2n)

B- O(1)

C- O(n)

D- O(n^2)


Answer is:

c - O(n)

"""