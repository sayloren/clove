"""
Wren Saylor
Jan 2018
Script to implement quick sort
"""

import time
count_conditionals = 0

def quick_sort(quick_list):

    global count_conditionals

    count_conditionals += 1
    if len(quick_list) <= 1:
        return quick_list
    else:
        # for each value in the list except the first, which is the pivot
        # if the value is less than the pivot, recursively put through function
        # add to the list of values that are larger than the pivot,
        # recursively put through the function
        count_conditionals += 1
        return quick_sort([x for x in quick_list[1:]
            if x < quick_list[0]]) + [quick_list[0]] + \
            quick_sort([x for x in quick_list[1:]
            if x >= quick_list[0]])

quick_list = [2,8,8,1,4,3,6,7,9]
start = time.time()
print(quick_sort(quick_list))
end = time.time()
print(count_conditionals-1)
print(end - start)

n = len(quick_list)
duration = end - start
