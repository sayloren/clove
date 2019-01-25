from sort import sort_algs
import numpy as np

x = np.array([1,4,2,5])
test_empty = np.array([])
test_zero = np.array([0])
test_neg = np.array([2,1,0,-1,-2])

collect_test = [test_empty,test_zero,test_neg,x]

# could test the number of expected conditionals, assignments?
# all(l[i] <= l[i+1] for i in range(len(l)-1)) # check that a list is sorted

def test_pointless_sort():
    assert np.array_equal(sort_algs.pointless_sort(x), np.array([1, 2, 3]))

def test_bubblesort():
    sort_algs.run_bubble_sort(x)
    for i in collect_test:
        assert np.array_equal(sort_algs.bubble_sort(i), np.array(sorted(i)))


def test_quicksort():
    sort_algs.run_quick_sort(x)
    for i in collect_test:
        assert np.array_equal(sort_algs.quick_sort(i), np.array(sorted(i)))
