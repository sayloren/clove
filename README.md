# clove

[![Build
Status](https://travis-ci.org/sayloren/example.svg?branch=master)](https://travis-ci.org/sayloren/example)

[Travis Build Results](https://travis-ci.org/sayloren/clove)

:see_no_evil: :hear_no_evil: :speak_no_evil:

## UCSF BMI 203 Algorithms Homework 2018

#### Set up

To use the package, first make a new conda environment and activate it

```
conda create -n exampleenv python=3
source activate exampleenv
```

then run

```
conda install --yes --file requirements.txt
```

to install all the dependencies in `requirements.txt`. Then the package's
main function (located in `example/__main__.py`) can be run as follows

```
python -m example
```

#### Bubble and Quick Sort Jan 25

##### To run sort
```
python -m sort -t -a -e
```

-t number of lists  
-a maximum value for list items  
-e range from which to draw the number of elements in a list  

##### To run sort tests
```
python -m pytest
```

![a](/Sorting_graphs.png)

| Sort | Theoretical | N |
| ---------- |:----------:|----------:|
| Bubble Sort | O(N2) | 32299880 |
| Quick Sort | O(n log(n)) | 222570 |
