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
from sympy import S, symbols

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def get_args():
    parser = argparse.ArgumentParser(description="Description")
    parser.add_argument("-t", "--total", type=int, default="100", help='number of random lists to generate')
    parser.add_argument("-m", "--max", type=int, default="10", help='the largest number in the random lists')
    parser.add_argument("-e", "--element", type=int, default="1000", help='the population from which to draw the random number of elements per list')
    return parser.parse_args()

def main():
    args = get_args()

    # empty lists to collect data from loop
    bubble_times,quick_times = [],[]
    number_elements = []
    quick_cond,quick_assi,bubble_cond,bubble_assi = [],[],[],[]

    # make the random lists
    random_lists = [[random.randrange(args.max) for _ in range(random.randrange(args.element))] for __ in range(args.total)]

    # iterate through the random lists
    for r in random_lists:
        number_elements.append(len(r))

        # run quick sort
        quick_start = time.time()
        out_bubble,assignments_quick,conditionals_quick = quick_sort.run_quick_sort(r)
        quick_end = time.time()

        # run bubble sort
        bubble_start = time.time()
        out_bubble,assignments_bubble,conditionals_bubble = bubble_sort.run_bubble_sort(r)
        bubble_end = time.time()

        # collect the times it took for each sort
        quick_times.append(quick_end - quick_start)
        bubble_times.append(bubble_end - bubble_start)
        quick_cond.append(conditionals_quick)
        quick_assi.append(assignments_quick)
        bubble_cond.append(conditionals_bubble)
        bubble_assi.append(assignments_bubble)

    # make data frame for out lists
    pd_lists = pd.DataFrame(list(zip(bubble_times,quick_times,number_elements,quick_cond,quick_assi,bubble_cond,bubble_assi)),columns=['bubble','quick', 'n',"q_conditional","q_assignment","b_conditional","b_assignment"])

    # graph
    sns.set_style('ticks')
    sns.set_palette("husl")
    gs = gridspec.GridSpec(2,1,height_ratios=[1,1],width_ratios=[1])
    plt.figure(figsize=(10,10))
    ax0 = plt.subplot(gs[0,:])
    ax0.ticklabel_format(style='sci')
    ax1 = plt.subplot(gs[1,:],sharex=ax0)
    # kind of sloppy line of best fit
    ax0.plot(np.unique(pd_lists['bubble']), np.poly1d(np.polyfit(pd_lists['bubble'], pd_lists['n'], 2))(np.unique(pd_lists['bubble'])),c='black',alpha=.5)
    ax1.plot(np.unique(pd_lists['quick']), np.poly1d(np.polyfit(pd_lists['quick'], pd_lists['n'], 1))(np.unique(pd_lists['quick'])),c='black',alpha=.5)
    sns.scatterplot(x="bubble", y="n", size="b_conditional", hue="b_assignment", data=pd_lists,ax=ax0)
    sns.scatterplot(x="quick", y="n", size="q_conditional", hue="q_assignment",data=pd_lists,ax=ax1)
    # x = symbols("x")
    # bubble_poly = sum(S("{:6.2f}".format(v))*x**i for i, v in enumerate(p[::-1]))
    # bubble_eq_latex = sympy.printing.latex(poly)
    ax0.set_title("Bubble Sort")
    ax0.set_ylabel("Size of N")
    ax0.set_xlabel("Time")
    ax1.set_title("Quick Sort")
    ax1.set_ylabel("Size of N")
    ax1.set_xlabel("Time")
    sns.despine()
    plt.savefig("Sorting_graphs.png",format='png')

if __name__ == "__main__":
	main()
