"""
Wren Saylor
Jan 2018
Script to call the sorting functions on randomly generated lists,
return the time it took and graphs
"""
# directory organization
# tests
# markdown

import argparse
import time
import random

import bubble_sort
import quick_sort

import pandas as pd

import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def get_args():
    parser = argparse.ArgumentParser(description="Description")
    parser.add_argument("-t", "--total", type=int, default="100", help='number of random lists to generate')
    parser.add_argument("-m", "--max", type=int, default="10", help='the largest number in the random lists')
    parser.add_argument("-e", "--element", type=int, default="100", help='the population from which to draw the random number of elements per list')
    return parser.parse_args()

def main():
    args = get_args()

    # empty lists to collect data from loop
    bubble_times,quick_times = [],[]
    number_elements = []

    # still need to collect conditional and assignment counts

    # make the random lists
    random_lists = [[random.randrange(args.max) for _ in range(random.randrange(args.element))] for __ in range(args.total)]

    # iterate through the random lists
    for r in random_lists:
        number_elements.append(len(r))

        # run quick sort
        quick_start = time.time()
        out_bubble,conditionals_quick = quick_sort.run_quick_sort(r)
        quick_end = time.time()

        # run bubble sort
        bubble_start = time.time()
        out_bubble,assignments_bubble,conditionals_bubble = bubble_sort.run_bubble_sort(r)
        bubble_end = time.time()

        # collect the times it took for each sort
        quick_times.append(quick_end - quick_start)
        bubble_times.append(bubble_end - bubble_start)

    # make data frame for out lists
    pd_lists = pd.DataFrame(list(zip(bubble_times,quick_times,number_elements)),columns=['bubble','quick', 'n'])

    # graph
    pp = PdfPages('Sorting_graphs.pdf')
    sns.set_style('ticks')
    sns.set_palette("husl")
    gs = gridspec.GridSpec(2,1,height_ratios=[1,1],width_ratios=[1])
    gs.update(hspace=.8)
    plt.figure(figsize=(10,10))
    ax0 = plt.subplot(gs[0,:])
    ax1 = plt.subplot(gs[1,:],sharex=ax0)
    sns.scatterplot(x="bubble", y="n", data=pd_lists,ax=ax0)
    sns.scatterplot(x="quick", y="n", data=pd_lists,ax=ax1)
    ax0.set_title("Bubble Sort")
    ax1.set_title("Quick Sort")
    sns.despine()
    plt.savefig(pp,format='pdf')
    pp.close()

if __name__ == "__main__":
	main()
