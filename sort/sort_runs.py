"""
Wren Saylor
Jan 2018
Script to call the sorting functions on randomly generated lists,
return the time it took and graphs
"""

import time
import random
import pathlib

from .sort_algs import run_bubble_sort,run_quick_sort

import pandas as pd
import numpy as np
import sympy
from math import log

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
    pd_lists = pd.DataFrame(list(zip(bubble_times,quick_times,number_elements,quick_cond,quick_assi,bubble_cond,bubble_assi)),columns=['b_time','q_time', 'n',"q_conditional","q_assignment","b_conditional","b_assignment"])

    # graph formatting
    sns.set_style('ticks')
    sns.set_palette("husl")
    gs = gridspec.GridSpec(3,2,height_ratios=[1,1,1],width_ratios=[1,1])
    gs.update(hspace=.8)
    fig = plt.figure(figsize=(10,10))
    fig.text(0.5, 0.04, 'N (number of elements)', ha='center', va='center', fontsize=18)
    fig.text(0.03, 0.5, 'Time', ha='center', va='center', rotation='vertical', fontsize=18)
    ax0 = plt.subplot(gs[0,0])
    ax1 = plt.subplot(gs[0,1])#,sharex=ax0
    ax2 = plt.subplot(gs[2,0])#,sharex=ax0
    ax3 = plt.subplot(gs[1,0])#,sharex=ax0
    ax4 = plt.subplot(gs[2,1])
    ax5 = plt.subplot(gs[1,1])#,sharex=ax4
    ax0.ticklabel_format(style='sci')

    ax0.set(xscale="log", yscale="log")
    ax1.set(xscale="log", yscale="log")
    ax2.set(xscale="log", yscale="log")
    ax3.set(xscale="log", yscale="log")
    ax4.set(xscale="log", yscale="log")
    ax5.set(xscale="log", yscale="log")

    # scatter plots for actual data
    sns.scatterplot(x="n", y="b_time", size="b_conditional", hue="b_assignment", data=pd_lists,ax=ax0)
    sns.scatterplot(x="n", y="q_time", size="q_conditional", hue="q_assignment",data=pd_lists,ax=ax1)
    sns.scatterplot(x="n", y="b_conditional", size="b_assignment", hue="b_time", data=pd_lists,ax=ax2)
    sns.scatterplot(x="n", y="b_assignment", size="b_conditional", hue="b_time",data=pd_lists,ax=ax3)
    sns.scatterplot(x="n", y="q_conditional", size="q_assignment", hue="q_time", data=pd_lists,ax=ax4)
    sns.scatterplot(x="n", y="q_assignment", size="q_conditional", hue="q_time",data=pd_lists,ax=ax5)

    # kind of sloppy line of best fit
    # ax0.plot(np.unique(pd_lists['n']), np.poly1d(np.polyfit(pd_lists['n'],pd_lists['b_time'], 2))(np.unique(pd_lists['n'])),c='black',alpha=.5)
    # ax1.plot(np.unique(pd_lists['n']), np.poly1d(np.polyfit(pd_lists['n'],pd_lists['q_time'], 2))(np.unique(pd_lists['n'])),c='black',alpha=.5)
    # ax2.plot(np.unique(pd_lists['n']), np.poly1d(np.polyfit(pd_lists['n'],pd_lists['b_conditional'], 2))(np.unique(pd_lists['n'])),c='black',alpha=.5)
    # ax3.plot(np.unique(pd_lists['n']), np.poly1d(np.polyfit(pd_lists['n'],pd_lists['b_assignment'], 2))(np.unique(pd_lists['n'])),c='black',alpha=.5)
    # ax4.plot(np.unique(pd_lists['n']), np.poly1d(np.polyfit(pd_lists['n'],pd_lists['q_conditional'], 3))(np.unique(pd_lists['n'])),c='black',alpha=.5)
    # ax5.plot(np.unique(pd_lists['n']), np.poly1d(np.polyfit(pd_lists['n'],pd_lists['q_assignment'], 3))(np.unique(pd_lists['n'])),c='black',alpha=.5)

    n_val = range(1,element)
    n_squ = [i ** 2 for i in n_val]
    n_log = [i*log(i,10) for i in n_val]
    ax3.plot(n_val,n_squ,c='purple',alpha=.5,linestyle='-.')
    ax2.plot(n_val,n_squ,c='purple',alpha=.5,linestyle='-.')
    ax4.plot(n_val,n_log,c='purple',alpha=.5,linestyle='-.')
    ax5.plot(n_val,n_log,c='purple',alpha=.5,linestyle='-.')

    # get and format the big o notation info
    x = sympy.symbols("x")
    bubble_fit = np.polyfit(pd_lists['b_time'], pd_lists['n'], 2)
    quick_fit = np.polyfit(pd_lists['q_time'], pd_lists['n'], 1)
    bubble_poly = sum(sympy.S("{:6.2f}".format(v))*x**i for i, v in enumerate(bubble_fit[::-1]))
    quick_poly = sum(sympy.S("{:6.2f}".format(v))*x**i for i, v in enumerate(quick_fit[::-1]))
    bubble_latex = sympy.printing.latex(bubble_poly)
    quick_latex = sympy.printing.latex(quick_poly)
    bubble_ass_fit = np.polyfit(pd_lists['b_conditional'], pd_lists['n'], 2)
    bubble_con_fit = np.polyfit(pd_lists['b_assignment'], pd_lists['n'], 2)
    quick_ass_fit = np.polyfit(pd_lists['q_conditional'], pd_lists['n'], 1)
    quick_con_fit = np.polyfit(pd_lists['q_assignment'], pd_lists['n'], 1)

    # in terms of N
    bubble_o = int(abs(bubble_fit.flat[0]))
    quick_o = int(abs(quick_fit.flat[0]))
    bubble_ass_o = int(abs(bubble_fit.flat[0]))
    bubble_con_o = int(abs(bubble_fit.flat[0]))
    quick_ass_o = int(abs(quick_fit.flat[0]))
    quick_con_o = int(abs(quick_fit.flat[0]))

    # # labeling and formating for graphs
    ax2.set_title("Bubble Sort, Conditionals")#, ${0}$".format(bubble_latex)
    ax3.set_title("Bubble Sort, Assignments")#, ${0}$".format(quick_latex)
    ax4.set_title("Quick Sort, Conditionals")#, ${0}$".format(bubble_latex)
    ax5.set_title("Quick Sort, Assignments")#, ${0}$".format(quick_latex)
    ax0.set_title("Bubble Sort, Time {0}".format(bubble_o))#, ${0}$".format(bubble_latex)
    ax1.set_title("Quick Sort, Time {0}".format(quick_o))#, ${0}$".format(quick_latex)
    ax0.set_ylabel("Seconds")
    ax1.set_ylabel("Seconds")
    ax0.legend(loc='upper left',frameon=False,fontsize='xx-small')
    ax1.legend(loc="upper left",frameon=False,fontsize='xx-small')
    axes = [ax2,ax3,ax4,ax5]
    for ax in axes:
        ax.set_ylabel("Complexity")
        ax.legend(loc='upper left',frameon=False,fontsize='xx-small')
    sns.despine()

    outdir = pathlib.Path('images')
    outfile = outdir / "Sorting_time_complexity.png"
    outdir.mkdir(parents=True, exist_ok=True)
    plt.savefig(str(outfile),format='png')
    plt.close()

    return quick_lists,bubble_lists,bubble_fit.flat[0],quick_fit.flat[0]

if __name__ == "__main__":
	main()
