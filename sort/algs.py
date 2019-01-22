"""
Wren Saylor
Jan 2018
Script to implement bubble sort and quick sort
"""

import argparse

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

def run_bubble_sort(bubble_list):
    global count_conditionals
    global count_assignments
    count_assignments,count_conditionals = 0,0
    out_list = bubble_sort(bubble_list)
    return out_list,count_assignments,count_conditionals

def quick_sort(quick_list):
    global count_assignments,count_conditionals
    count_conditionals += 1
    if len(quick_list) <= 1:
        return quick_list
    else:
        # for each value in the list except the first, which is the pivot
        # if the value is less than the pivot, recursively put through function
        # add to the list of values that are larger than the pivot,
        # recursively put through the function
        count_conditionals += 1
        count_assignments += 1 # not sure if putting value into list is assignment
        return quick_sort([x for x in quick_list[1:]
            if x < quick_list[0]]) + [quick_list[0]] + \
            quick_sort([x for x in quick_list[1:]
            if x >= quick_list[0]])

def run_quick_sort(quick_list):
    global count_conditionals
    global count_assignments
    count_assignments,count_conditionals = 0,0
    out_list = quick_sort(quick_list)
    return out_list,count_assignments,count_conditionals-1


if __name__ == "__main__":
	main()
