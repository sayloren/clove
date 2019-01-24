# clove

[![Build
Status](https://travis-ci.org/sayloren/clove.svg?branch=master)](https://travis-ci.org/sayloren/clove)

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

![a](/images/Sorting_time_complexity.png)

| Sort | Theoretical | N |
| ---------- |:----------:|:----------:|
| Bubble Sort | ![a](/images/nsquared.gif) | ~30000000 |
| Quick Sort | ![a](/images/nlogn.gif) | ~200000 |
