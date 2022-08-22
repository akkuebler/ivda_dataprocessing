import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import _pickle as cp
import sklearn as sk
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler


url = 'https://raw.githubusercontent.com/akkuebler/ivda_dataprocessing/main/preppedStudentCovidData.csv'
df = pd.read_csv (url, sep="," , index_col = [0])
# TODO: shall we give them the index_col as a hint? otherwise it looks kinda messy/weird if there is another index starting with 0, 1, 2...


# Task 1.1
# A: check the size of the data
print("The dataset contains {} data records and {} features.".format(df.shape[0], df.shape[1]))
# Check the tasks and define the questions in the questionaire which are particularly important for your data analysis. 
# B: Give basic summary statistics for them. Which attribute has the most missing data? --> answer: Q17
df.Q1.describe() # reports the count of non-missing values
df.Q3.describe()
df.Q4.describe()
df.Q5.describe()
df.Q6.describe()
df.Q9.describe()
df.Q17.describe()
df.Q25a.describe()
df.Q25b.describe()
df.Q25c.describe()
df.Q25d.describe()
df.Q25e.describe()
df.Q25f.describe()
df.Q25g.describe()
df.Q25h.describe()
df.Q25i.describe()
df.Q25j.describe()



# C: When working with data, not only missing data can be an issue, but also duplicates. 
# So now, heck for duplicates, delete them but keep the first entry. Hint: The index works as a unique student number for every student. 
# Here, index = std number --> so drop duplicates by this
df_work = df[~df.index.duplicated(keep='first')]

df_wrong = df.drop_duplicates(keep ='first') #By default, it removes duplicate rows based on all columns, but does not take index into account! 
# TODO: possible question for students could be: why can you not simply use df.drop_duplicates(keep ='first'? What would happen here?

print("The dataset now contains {} data records and {} features.".format(df_work.shape[0], df_work.shape[1]))


# D: Visualize what countries and how often they are represented in your dataset using a piechart.
# For now, do not clean up your data yet.
c = list(df_work["Q1"])
def counting_as_dict(c):
    countries = {}
    for country in c:
        countries[country] = countries.get(country, 0) + 1
    return countries

def plot_pie(dictionary):
    labels = []
    sizes = []

    for x, y in dictionary.items():
        labels.append(x)
        sizes.append(y)

    # Plot
    plt.pie(sizes, labels=labels , autopct='%1.1f%%')

    plt.axis('equal')
    return (plt.show())

counting_as_dict(c)
plot_pie(counting_as_dict(c))


# As you can see, the plot is very cluttered. Try to map the countries to the respective continents using the continent.csv file and plot it again. 
url2 = 'https://raw.githubusercontent.com/akkuebler/ivda_dataprocessing/main/continents.csv' 
continents = pd.read_csv (url2, sep="," , index_col = None)
mapping = dict(continents[['country', 'continent']].values)
df_work['continent'] = df_work.Q1.map(mapping)

con = list(df_work["continent"])
counting_as_dict(con)
plot_pie(counting_as_dict(con))

# inspect the pie chart and dataframe: why do we have about 5% missing values? Where does this come from? 
df_work.continent.describe()
missing = pd.DataFrame(df.Q1[df_work.continent.isnull()])
print(missing.Q1.unique())
# United States vs United States of America
# Phillipines vs. The Phillipines
# nothing vs. Palestinian State
# DR Congo vs. Democratic Rep. of Congo
# The Netherlands vs. Netherlands
# TODO: should students change that per hard-coding? Learning would be: always check the data you use for mapping! 



# Task 1.2 
# Visualize the age of the students in your dataset with an appropriate boxplot. 
# What issue do you encounter here while still having missing data in your dataset? 
# Hint: In case you need to filter out missing data, you can use isnan()
# Describe the boxplot. What can you infer from it? Max 100 words. 
# TODO: state required outcome
age = list(df_work["Q7"])
# Filter data using np.isnan
filtered = []
for x in age:
    if np.isnan(x): continue
    if int(x): filtered.append(x)

plt.boxplot(filtered)
plt.show()




# Task 2
# Inspect your dataset again. We still have missing data, which we simply ignored in task 1.2 
# TODO: this gives a hint for the task before --> do we want that? 
# Now come up with a strategy to have a good dataset with less missing values to further work with. 
# You only need to treat the columns you are going to use for the rest of the tasks (the one you defined in 1.1 B)
# Hint: In general there are 3 different ways to handle missing data: 
    # 1. ignoring on purpose
    # 2. deleting entire row/column with missing data or deleting entire row/column when missing data reachs a certain threshold
    # 3. imputing missing data with e.g. mean/ median/ treat as seperate category when data is categorical etc. 
# All of them are data type and context-dependent!


# Task 2.1: Drop rows where all data is missing
# Important: as the index is the unique student number, we should NOT reset the index here!
print("The dataset contains {} data records and {} features.".format(df_work.shape[0], df_work.shape[1]))
df_work = df_work.dropna(how='all') #if index filled, it will delete row as well when else is nan
print("The DataFrame after removing rows with NaN value in All Columns contains {} data records and {} features.".format(df_work.shape[0], df_work.shape[1]))
# there is no row with all missing data
# TODO: shall I build one artificially to then be removed?


# Task 2.2: Keep only rows with at least 100 non-NA values 
print("The dataset contains {} data records and {} features.".format(df_work.shape[0], df_work.shape[1]))
df_work = df_work.dropna(thresh=100) #if index filled, it will delete row as well when else is nan
print("The DataFrame after removing rows with NaN value in All Columns contains {} data records and {} features.".format(df_work.shape[0], df_work.shape[1]))



# Task 2.3: Q7 (Age): Impute with mean 
print("Original Data : \n", df_work.Q7.describe())
imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')
df_work.Q7 = imputer.fit_transform(df_work['Q7'].values.reshape(-1,1))[:,0]
# Note: df_work.['Q7'].values.reshape(-1, 1) # extracts a numpy array with the values of the pandas Series object and then reshapes it to a 2D array.--> need to do this bc pandas Series objects are by design one dimensional.
print("Imputed Data : \n", df_work.Q7.describe())


# Visualize again the age of the students in your dataset with an appropriate boxplot. 
plt.boxplot(df_work.Q7)
plt.show()
 # Has the boxplot changed? If so, explain why. 
 # --> more data to plot now in general, outlier same. Inpute with mean leads only std to change, middle quartile up. Due to reduced std, the upper whisker is shorter
# TODO: give plot headers to differ when saved


# Task 2.4: Q4 (Student Status): form new category for missing data --> 3 in total then)
# TODO: another option in general would be to fill it with the most frequent categ value like df = df.fillna(df[‘column’].value_counts().index[0]) --> doesnt make sense here, shall we still show it to them? 
# TODO: instead of df_work.Q4.describe(), we can also show the students this:
freq = df_work.groupby(['Q4']).count() 
print(freq)
df_work.Q4.fillna(99, inplace=True)
freq = df_work.groupby(['Q4']).count() 
print(freq)


# Task 3.1: Visualize the perception on how the workload changed before/after on-site classes were cancelled, depending whether the student is a full-time/part-time student. 
# Use an appropriate stacked bar chart for this. The associated questions in the questionaire are Q17 and Q4.
# How are you handling missing data here?
# Hint: Group your data before plotting, including appropriate index and columns names. This will help you with labelling.
# Explain your choice.
 
# We dealt with missing data in Q4 in task 2.4 already --> won't take into account missing data here --> neglect category
# Q17: inspect the data again or use freq from above 
# How many full/part time student have answered question Q17?  --> we see that 5219 full-time students and 603 part time students have answered it. + 89 which have not answered Q4 = 5911
df_work.Q17.describe()

# Build a frequency table as basis for the chart
table=pd.crosstab(df_work.Q4,df_work.Q17, normalize='index').round(2)*100 #use percentages over rows! Bc missing values (99) are dropped after
table
# delete the row with "missing" data, named 99
table = table.drop(99.0)
table


#Rename Dataframe for an appropriate plot
table = table.rename(columns={1.0: 'significantly smaller' , 2.0: 'smaller' , 3.0: 'the same' , 4.0: 'larger' , 5.0: 'significantly larger'}, index={1.0: 'full-time', 2.0: 'part-time', })
# form into int
table = table.astype(int)
print(table)



#Build the stacked bar chart
# TODO: took that from online source --> do we need to mention that. Plus: still no int in plot
pl = table.plot(kind='bar', stacked=True, figsize=(8, 4), rot=0, xlabel='Class', ylabel='Count')
pl.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
          fancybox=True, shadow=True, ncol=5)

# Shrink current axis's height by 10% on the bottom
box = pl.get_position()
pl.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

for c in pl.containers:

    # Optional: if the segment is small or 0, customize the labels
    labels = [v.get_height() if v.get_height() > 0 else '' for v in c]
    
    # remove the labels parameter if it's not needed for customized labels
    pl.bar_label(c, labels=labels, label_type='center')

# What simple grafical element could help you with comparing the two bar charts more easily? 
# Answer: add lines between stacked columns bar 
# TODO: --> possible to code, but time consuming 


# Task 4.1: Build an emotional satisfaction score using the data from Q25. 
# For this, group the data in positive and negative feelings, summarize the specific columns and normalize them to scale between 0 and 1. 
# Afterwards calculate the balance.
# Then use an appropriate plot to show differences between BA, Master and PhD students using Q5. 
# Hint: We use the value for the given categorical data item as a measure of emotion intensity (e.g. 'Never': 1 and 'Always': 5)
# TODO: Assumptions --> positive emotions balance out negative ones


# Group data
# positive: Q25a, Q25b, Q25c, Q25h
# negative: Q25d, Q25e, Q25f, Q25g, Q25i, Q25j


# How to deal with missing data here? 
# all students which are taken into account for this analysis, should have answered all 9 subquestions in Q25 and as well as in Q5. 
df_work_emotion = df_work
# drop rows where data is missing in specific columns
print("The dataset contains {} data records and {} features.".format(df_work_emotion.shape[0], df_work_emotion.shape[1]))

df_work_emotion = df_work_emotion.dropna(subset=['Q5', 'Q25a', 'Q25b', 'Q25c', 'Q25h', 'Q25d', 'Q25e', 'Q25f', 'Q25g', 'Q25i', 'Q25j' ]) #per default drop rows

print("The DataFrame after removing rows with NaN value in the specified columns contains {} data records and {} features.".format(df_work_emotion.shape[0], df_work_emotion.shape[1]))

df_work_emotion['pos_emot_count'] = df_work_emotion.loc[:, ['Q25a', 'Q25b', 'Q25c', 'Q25h']].sum(axis=1)
df_work_emotion['neg_emot_count'] = df_work_emotion.loc[:, ['Q25d', 'Q25e', 'Q25f', 'Q25g', 'Q25i', 'Q25j']].sum(axis=1)


# normalize new columns to compare them to each other for intensity score
cols_to_norm = ['pos_emot_count', 'neg_emot_count']
scaler = MinMaxScaler(feature_range=(0, 1)) #by default always 0 and 1
df_work_emotion[cols_to_norm] = scaler.fit_transform(df_work_emotion[cols_to_norm])

# calculate final emotional satisfaction score
df_work_emotion['neg_emot_count'] = df_work_emotion['neg_emot_count'] * -1
df_work_emotion['balance'] = df_work_emotion.loc[:, ['pos_emot_count','neg_emot_count']].sum(axis=1)


# Group by Q5, calculate average 
# TODO: use reset_index() here --> otherwise issues later with renaming
compare = df_work_emotion.groupby('Q5')['balance'].mean().reset_index()

#rename index column and plot
compare.insert(0, "studentstatus", ['Bachelor', 'Master', 'PhD'], True)
compare.plot.bar(y = "balance", x = "studentstatus", rot=0)







