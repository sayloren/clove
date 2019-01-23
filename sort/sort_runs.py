"""
Wren Saylor
Jan 2018
Script to call the sorting functions on randomly generated lists,
return the time it took and graphs
"""

import time
import random

from .sort_algs import run_bubble_sort,run_quick_sort

import pandas as pd
import numpy as np
import sympy

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def run_graphing(total,max,element):

    # empty lists to collect data from loop
    bubble_times,quick_times = [],[]
    number_elements = []
    quick_cond,quick_assi,bubble_cond,bubble_assi = [],[],[],[]
    quick_lists,bubble_lists = [],[]

    # make the random lists
    random_lists = [[random.randrange(max) for _ in range(random.randrange(element))] for __ in range(total)]

    # iterate through the random lists
    for r in random_lists:
        number_elements.append(len(r))

        # run quick sort
        quick_start = time.time()
        out_quick,assignments_quick,conditionals_quick = run_quick_sort(r)
        quick_end = time.time()

        # run bubble sort
        bubble_start = time.time()
        out_bubble,assignments_bubble,conditionals_bubble = run_bubble_sort(r)
        bubble_end = time.time()

        # collect the times it took for each sort
        quick_lists.append(out_quick)
        bubble_lists.append(out_bubble)
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
    # change to share y axis, next to eachother
    gs = gridspec.GridSpec(1,2,height_ratios=[1],width_ratios=[1,1])
    plt.figure(figsize=(10,5))
    ax0 = plt.subplot(gs[:,0])
    ax0.ticklabel_format(style='sci')
    ax1 = plt.subplot(gs[:,1],sharey=ax0)
    # kind of sloppy line of best fit
    # should get this in terms of N
    # ax0.plot(np.unique(pd_lists['bubble']), np.poly1d(np.polyfit(pd_lists['bubble'], pd_lists['n'], 2))(np.unique(pd_lists['bubble'])),c='black',alpha=.5)
    # ax1.plot(np.unique(pd_lists['quick']), np.poly1d(np.polyfit(pd_lists['quick'], pd_lists['n'], 1))(np.unique(pd_lists['quick'])),c='black',alpha=.5)
    # ax0.plot(pd_lists['n'],c='black',alpha=.5)
    # ax1.plot(pd_lists['n'],c='black',alpha=.5)
    # add theoretical O(n2) and O(nlog(n))
    # quick sort on log(n) plot - will look like line
    sns.scatterplot(x="bubble", y="n", size="b_conditional", hue="b_assignment", data=pd_lists,ax=ax0)
    sns.scatterplot(x="quick", y="n", size="q_conditional", hue="q_assignment",data=pd_lists,ax=ax1)
    x = sympy.symbols("x")
    bubble_fit = np.polyfit(pd_lists['bubble'], pd_lists['n'], 2)
    quick_fit = np.polyfit(pd_lists['quick'], pd_lists['n'], 1)
    bubble_poly = sum(sympy.S("{:6.2f}".format(v))*x**i for i, v in enumerate(bubble_fit[::-1]))
    quick_poly = sum(sympy.S("{:6.2f}".format(v))*x**i for i, v in enumerate(quick_fit[::-1]))
    bubble_latex = sympy.printing.latex(bubble_poly)
    quick_latex = sympy.printing.latex(quick_poly)
    ax0.set_title("Bubble Sort, ${0}$".format(bubble_latex))
    ax0.set_ylabel("N")
    ax0.set_xlabel("Time Complexity")
    ax1.set_title("Quick Sort, ${0}$".format(quick_latex))
    ax1.set_ylabel("N")
    ax1.set_xlabel("Time Complexity")
    ax0.legend(loc='lower right')
    ax1.legend(loc='lower right')
    sns.despine()
    plt.savefig("Sorting_graphs.png",format='png')
    return quick_lists,bubble_lists,bubble_latex[0],quick_latex[0]

if __name__ == "__main__":
	main()
