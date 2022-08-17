import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import _pickle as cp

# Task 1.1
# Come up with a strategy to have a good dataset consisting of 5000 rows

# TODO AK: build messy dataset with 5000 + rows (3000 clean, 2000 missing, rest total mess) 
# pandas filter 
# check them for duplicates
# dataset prep to work with
df = pd.read_csv (r'/Users/anki/Documents/Uni_Zurich/IVDA_teaching/covid_impact.csv', sep=";")
print (df[:10])

#check for missing data we find a lot 
df.columns[df.isnull().any()]


#filter data which has missing values in Q1 - Q9, Q25, Q17
# TODO AK: can we make it nicer and loop through it? 
#for x in ("Q1"):
 #   df=df[df[x].notnull()]

df_clean = df
df_clean = df_clean[df_clean["Q1"].notnull()]
df_clean = df_clean[df_clean["Q3"].notnull()]
df_clean = df_clean[df_clean["Q4"].notnull()]
df_clean = df_clean[df_clean["Q5"].notnull()]
df_clean = df_clean[df_clean["Q6"].notnull()]
df_clean = df_clean[df_clean["Q7"].notnull()]
df_clean = df_clean[df_clean["Q8"].notnull()]
df_clean = df_clean[df_clean["Q9"].notnull()]
df_clean = df_clean[df_clean["Q17"].notnull()]
df_clean = df_clean[df_clean["Q25a"].notnull()]
df_clean = df_clean[df_clean["Q25b"].notnull()]
df_clean = df_clean[df_clean["Q25c"].notnull()]
df_clean = df_clean[df_clean["Q25d"].notnull()]
df_clean = df_clean[df_clean["Q25e"].notnull()]
df_clean = df_clean[df_clean["Q25f"].notnull()]
df_clean = df_clean[df_clean["Q25g"].notnull()]
df_clean = df_clean[df_clean["Q25h"].notnull()]
df_clean = df_clean[df_clean["Q25i"].notnull()]
df_clean = df_clean[df_clean["Q25j"].notnull()]
# 11237 rows left

#shuffle data and reduce to 3000 rows
df_shuffled = df_clean.sample(frac=1, random_state=222)
print(df_shuffled.shape)

df_clean=df_shuffled[:3000]

# select 2000 rows with a few missing data
# TODO AK: but only checked specific row for missing data
df_missing_Q1 = (df[df["Q1"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q3 = (df[df["Q3"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q4 = (df[df["Q4"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q5 = (df[df["Q5"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q6 = (df[df["Q6"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q7 = (df[df["Q7"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q8 = (df[df["Q8"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q9 = (df[df["Q9"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q17 = (df[df["Q17"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q25a = (df[df["Q25a"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q25b = (df[df["Q25b"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q25c = (df[df["Q25b"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q25d = (df[df["Q25b"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q25e = (df[df["Q25b"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q25f = (df[df["Q25b"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q25g = (df[df["Q25b"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q25h = (df[df["Q25b"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q25i = (df[df["Q25b"].isnull()]).sample(frac=1, random_state=222)[:100]
df_missing_Q25j = (df[df["Q25b"].isnull()]).sample(frac=1, random_state=222)[:100]


# put them together
frames = [df_missing_Q1, df_missing_Q3, df_missing_Q4]
result = pd.concat(frames)



# Task 1.2 
# Inspect your final dataset, you chose to work with 
# TODO AK: Do we include more summary statistics?
# show column header names in a list
data_top = df_work.columns.values
data_top

# check the size of the data
print("The dataset contains {} data records and {} features.".format(df_work.shape[0], df_work.shape[1]))
# TODO AK: more if theese if possible with blank behind

# show the first 10 rows: 
print (df_work[:10])
# convert dataframe to NumPy Array
df_work.to_numpy()



# Task 2.1: Visualize what countries and how often they are represented in your dataset using a piechart.
# For now, do not clean up your data yet.
c = list(df_work["Q1"])
def counting_as_dict(c):
    countries = {}
    for country in c:
        #country = country.lower() not possible with none value
        # TODO: do we want to include spelling mistakes and lower/upper case issues? nope -- string parsing? 
        countries[country] = countries.get(country, 0) + 1
    return countries

counting_as_dict(c)

def plot_pie(dictionary):
    labels = []
    sizes = []

    for x, y in dictionary.items():
        labels.append(x)
        sizes.append(y)

    # Plot
    plt.pie(sizes, labels=labels)

    plt.axis('equal')
    return (plt.show())

plot_pie(counting_as_dict(c))




# Task 2.2 (cleaned): 
# Visualize again what countries and how often they are represented in your dataset using a piechart.
# This time, encode the missing data in an appropriate way. 
# Furthermore, map the countries to their coresponding continent, using the provided table. 
# TODO AK: provide continent table


# filling a null values using fillna()
#data["Gender"].fillna("No Gender", inplace = True)




# Task 3.1: Visualize the age of the students in your dataset with an appropriate boxplot. 
# What issue do you encounter here while still having missing data in your dataset? 
# In case you need to filter out misisng data, you can use isnan()
age = list(df_work["Q7"])
# Filter data using np.isnan
filtered = []
for x in age:
    if np.isnan(x): continue
    if int(x): filtered.append(x)

plt.boxplot(filtered)
plt.show()




# Task 3.2 (cleaned): Visualize again the age of the students in your dataset with an appropriate boxplot.
# This time do not ignore missing values, but think about how you can treat them. Explain your decision. 
# Take also into account the context your working with. --> 3 options



# Task 4.1: Visualize the perception on how the workload changed before/after on-site classes were cancelled, depending whether the student is a full-time/part-time student. 
# Use an appropriate stacked bar chart for this. The associated questions in the questionaire are Q17 and Q4.
# How are you handling missing data here? Again, generate two plots, before and after data cleaning. 
# Explain your choice.
 


# Task 5.1 Build an emotional satisfaction score using the data from Q25. emotions: stacked bar chart
# For this, group the data in positive and negative feelings and  normalize them to scale between 0 and 1. 
# Then use an appropriate plot to show differences between BA, MAster and PhD students using Q5. 






