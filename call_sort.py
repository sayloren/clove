"""
Wren Saylor
Jan 2018
Script to call the sorting functions
on randomly generated lists,
return the time it took
and graphs
"""
# argparse
# random lists
# graphs
# directory org
# tests

import argparse
import time
import random
import bubble_sort
import quick_sort

def get_args():
    parser = argparse.ArgumentParser(description="Description")
    # parser.add_argument("-r", "--random", type=int, default="100", help='number of random lists to generate')
    return parser.parse_args()

def main():
    args = get_args()
    # random.sample(range(30), args.random)
    temp = [2,8,8,1,4,3,6,7,9]
    n = len(temp)

    quick_start = time.time()
    out_bubble,conditionals_quick = quick_sort.run_quick_sort(temp)
    quick_end = time.time()

    quick_time = quick_end - quick_start

    bubble_start = time.time()
    out_bubble,assignments_bubble,conditionals_bubble = bubble_sort.run_bubble_sort(temp)
    bubble_end = time.time()

    bubble_time = bubble_end - bubble_start
    print(quick_time,bubble_time)


if __name__ == "__main__":
	main()
