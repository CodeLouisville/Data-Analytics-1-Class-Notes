import pandas as pd
from matplotlib import pyplot as plt

#pandas is actual magic
df = pd.read_csv("glassdoor_pay_gap.csv")

title, gender, age, perf_eval, education, dept, seniority, base_pay, bonus = [df[key] for key in df.columns]
#the above comprehension is equivalent to
columns = []
for key in df.columns:
    # add each series to the list
    columns.append(df[key])

# use iterable unpacking to assign each column to its own variable
title, gender, age, perf_eval, education, dept, seniority, base_pay, bonus = columns

# lets check our max and min values for `PerfEval` and `Seniority`
perf_eval.min() # -> 1
perf_eval.max() # -> 5
seniority.min() # -> 1
seniority.max() # -> 5

# as we suspected both are a 1 to 5 scale

# Trying to answer our first question. What is the total compensation distribution by gender?
# pandas makes combining like columns easy
df["total_comp"] = base_pay + bonus
total_comp = df["total_comp"]

plt.scatter(gender, total_comp, alpha=.5)
plt.title("Total Comp by gender")
plt.ylabel("Gender")
plt.xlabel("Total Comp")

# plt.show()
#NOTE: after setting up a plot obj (`plt`) you need to call `plt.show()`

# Although a difference is immediately noticeable, this isn't completely useful on its own.
# We can easily apply this to other features

plt.scatter(title, total_comp, alpha=.5)
plt.title("Total Comp by title")
plt.ylabel("Title")
plt.xlabel("Total Comp")
# plt.show()

# Lets take on a slightly more complex column creation.
# We will try to make a viz of Distribution of percent of total compensation represented by bonus
# For this we need percent of total compensation represented by bonus

df["bonus_perc"] = bonus / total_comp
bonus_perc = df["bonus_perc"].apply(lambda x: round(x * 100))

# quick aside on lambda. It would be equivalent to this:
def transform_percentage(x):
    return round(x * 100)

bonus_perc = df["bonus_perc"].apply(transform_percentage)

# Lets try a new type of plot.
# It might be interesting to see the compensation broken down by education
# For that a histogram might be better than a scatterplot

# First we need to filter our dataframe by only rows where the entry has a PhD
# Thankfully pandas makes this very straightforward

filtered_df_for_phd = df[df.Education == "PhD"]
phd_age = filtered_df_for_phd["total_comp"]

plt.hist(phd_age)
plt.xlabel("PhD total comp")
# plt.show()


# Lets make a more interesting histogram. Lets do a side by side binning
# in the same histogram by total compensation

#setup our filtered dfs
male_total_comp = df[df.Gender == "Male"]["total_comp"]
female_total_comp = df[df.Gender == "Female"]["total_comp"]

n_bins = 15

plt.hist(
    [male_total_comp, female_total_comp],
    n_bins,
    color=["Blue", "Orange"],
    histtype='bar',
    label=["Male", "Female"]
)
plt.legend()
# plt.show()