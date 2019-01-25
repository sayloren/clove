# clove

[![Build
Status](https://travis-ci.org/sayloren/clove.svg?branch=master)](https://travis-ci.org/sayloren/clove)

[Travis Build Results](https://travis-ci.org/sayloren/clove)

:see_no_evil: :hear_no_evil: :speak_no_evil:

## UCSF BMI 203 Algorithms Homework 2018

#### Set up

To use the package, first make a new conda environment and activate it

```
conda create -n homeworkone python=3
source activate homeworkone
```

to install all the requirements run

```
conda install --yes --file requirements.txt
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

| Sort | Theoretical | Coefficient |
| ---------- |:----------:|:----------:|
| Bubble Sort | ![a](/images/nsquared.gif) | ~30000 |
| Quick Sort | ![a](/images/nlogn.gif) | ~100000 |
