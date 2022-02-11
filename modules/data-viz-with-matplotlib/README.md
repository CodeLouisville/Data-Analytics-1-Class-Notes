# Basic Data Visualization with matplotlib

1. [Overview](#overview)
2. [Dimensions](#dimensions)
3. [Questions](#questions)
4. [Demo Prereqs](#demo-prereqs)
5. [Demo Time](#demo-time)
6. [Additional Resources](#additional-resources)

## Overview
In this demo we will take a dataset of surveyed salary information from glassdoor.com and try to use data visualizations to identify patterns.

The dataset does indicate a few important notes. Base pay and Bonuses are given as annual. Additionally this data was captured in 2019. Always important to note with survey data is that it is self-reported.

## Dimensions
Firstly, we should think about what dimensions our data contains. Here is the header and a few rows of our primary dataset.

```csv
JobTitle, Gender, Age, PerfEval, Education, Dept, Seniority, BasePay, Bonus
Graphic Designer, Female, 18, 5, College, Operations, 2, 42363, 9938
Software Engineer, Male, 21, 5, College, Management, 5, 108476, 11128
Warehouse Associate, Female, 19, 4, PhD, Administration, 5, 90208, 9268
Software Engineer, Male, 20, 5, Masters, Sales, 4, 108080, 10154
Graphic Designer, Male, 26, 5, Masters, Engineering, 5, 99464, 9319
IT, Female, 20, 5, PhD, Operations, 4, 70890, 10126
```

A brief evaluation allows us to elimate certain sets of questions. For instance, we have no time data so we could not answer a question like "How has the gender pay gap changed over time?". We do have a base salary and bonus. We don't have any sort of indication of other quantifiable benefits, which is a potentially notable missing data point.

Two other columns of note could be `PerfEval` and `Seniority`. These appear to be number values. The provider of the data does not indicate the min/max values. We could assume that those are 1 to 5 based on what we see here, but determining the max and min values could prove useful.

## Questions

##### Ideas
After briefly considering our dimensions what questions could we ask of this data?
  - Total compensation distribution by gender
  - Total compensation distribution by job title
  - Total compensation distribution by age
  - Distribution of percent of total compensation represented by bonus
  - Average age of all participants
  - Average total compensation

We could also choose to weight a certain dimension by another. E.g. Total compensation distribution by gender weighting for `PerfEval` or `Education`

#### What other questions could you try to answer with this data?

## Demo Prereqs
- python environment with an interactive shell or the ability to execute a python file
- a virtual environment with `matplotlib` and `pandas` installed.
  - `pip install matplotlib pandas`
- the csv `glassdoor_pay_gap.csv` included in this repository

## Demo Time
See `pay_viz.py`

## Additional Resources
[Pandas data frame docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
[matplotlib docs](https://matplotlib.org/stable/)