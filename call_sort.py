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
import numpy as np

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
    quick_cond,bubble_cond,bubble_assi = [],[],[]

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
        quick_cond.append(conditionals_quick)
        bubble_cond.append(conditionals_bubble)
        bubble_assi.append(assignments_bubble)

    # make data frame for out lists
    pd_lists = pd.DataFrame(list(zip(bubble_times,quick_times,number_elements,quick_cond,bubble_cond,bubble_assi)),columns=['bubble','quick', 'n',"q_conditional_count","b_conditional_count","b_assignment_count"])

    # get line of best fit for sorts
    # https://stackoverflow.com/questions/22239691/code-for-line-of-best-fit-of-a-scatter-plot-in-python
    # bubble_fit = np.polyfit(x=bubble_times, y=number_elements, deg=2,full=True)
    # quick_fit = np.polyfit(x=quick_times, y=number_elements, deg=2,full=True)

    # graph
    pp = PdfPages('Sorting_graphs.pdf')
    sns.set_style('ticks')
    sns.set_palette("husl")
    gs = gridspec.GridSpec(2,1,height_ratios=[1,1],width_ratios=[1])
    plt.figure(figsize=(10,10))
    ax0 = plt.subplot(gs[0,:])
    ax0.ticklabel_format(style='sci')
    ax1 = plt.subplot(gs[1,:],sharex=ax0)
    sns.scatterplot(x="bubble", y="n", size="b_conditional_count", hue="b_assignment_count", data=pd_lists,ax=ax0)
    sns.scatterplot(x="quick", y="n", size="q_conditional_count",data=pd_lists,ax=ax1)
    ax0.set_title("Bubble Sort")
    ax0.set_ylabel("Size of N")
    ax0.set_xlabel("Time")
    ax1.set_title("Quick Sort")
    ax1.set_ylabel("Size of N")
    ax1.set_xlabel("Time")
    sns.despine()
    plt.savefig(pp,format='pdf')
    pp.close()

if __name__ == "__main__":
	main()
