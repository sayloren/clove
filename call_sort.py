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
    parser = argparse.ArgumentParser(description="Graph time complexity for bubble and quick sort")
    parser.add_argument("-r", "--random", type=int, default="100", help='number of random lists to generate')
    return parser.parse_args()





def main():
	args = get_args()
    random.sample(range(30), 4)


if __name__ == "__main__":
	main()
