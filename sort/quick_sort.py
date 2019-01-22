"""
Wren Saylor
Jan 2018
Script to implement quick sort
"""
import argparse

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
