from sort import sort_algs
import numpy as np

x = np.random.rand(10)
test_empty = np.array([])
test_char = np.array(['a','b','c'])
test_random = np.array(np.random.RandomState(17))
test_zero = np.array([0])
test_neg = np.array([2,1,0,-1,-2])

collect_test = [test_empty,test_char,test_random,test_zero,test_neg]

# could test the number of expected conditionals, assignments?
# all(l[i] <= l[i+1] for i in range(len(l)-1)) # check that a list is sorted

def test_pointless_sort():
    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.run_bubble_sort(x), np.array([1,2,3]))

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # for now, just attempt to call the bubblesort function, should
    # actually check output
    algs.run_bubble_sort(x)

    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?
    for i in collect_test:
        assert np.array_equal(algs.run_bubble_sort(i)[0], sorted(w))


def test_quicksort():

    # for now, just attempt to call the quicksort function, should
    # actually check output
    algs.run_quick_sort(x)

    for i in collect_test:
        assert np.array_equal(algs.run_quick_sort(i, 0, len(i)-1, 0, 0)[0], sorted(i))
