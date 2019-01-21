"""
Wren Saylor
Jan 2018
Script to implement bubble sort
"""

import time
count_assignments,count_conditionals = 0,0

def bubble_sort(bubble_list):
    global count_assignments,count_conditionals
    count_assignments += 1
    test_order = 0

    # iterate over the length of the list minus one
    for i in range(len(bubble_list)-1):

        # if that value is greater than the next one
        if bubble_list[i] > bubble_list[i + 1]:

            # switch the values
            bubble_list[i], bubble_list[i+1] = bubble_list[i+1], bubble_list[i]

            count_conditionals += 1
            count_assignments += 2
            test_order += 1

    count_conditionals += 1
    if test_order == 0:
        return bubble_list
    else:
        return bubble_sort(bubble_list)

bubble_list = [2,8,8,1,4,3,6,7,9]
start = time.time()
print(bubble_sort(bubble_list))
end = time.time()
print(count_assignments,count_conditionals)
print(end - start)

n = len(bubble_list)
duration = end - start
