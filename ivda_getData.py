import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import _pickle as cp


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
 # pandas iterable?
 # for colimn in dataframe --> do it to whole column
# and then list 
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



# 100 randomly selected rows
df_random = df.sample(frac=1, random_state=333)[:5100]

 
# put them together and shuffling it again 
frames = [df_missing_Q1, df_missing_Q3, df_missing_Q4, df_missing_Q5,df_missing_Q6, df_missing_Q7, 
          df_missing_Q8,df_missing_Q9, df_missing_Q17,df_missing_Q25a, df_missing_Q25b, df_missing_Q25c, df_missing_Q25d,
          df_missing_Q25e, df_missing_Q25f, df_missing_Q25g, df_missing_Q25h, df_missing_Q25i, df_missing_Q25j,
          df_clean, df_random]
result = (pd.concat(frames)).sample(frac=1, random_state=444)



# duplicates --> we want to have some in it 
# Select duplicate rows except first occurrence based on all columns
duplicatedRows = result[result.duplicated()]

# Export it to cvs
result.to_csv('/Users/anki/Documents/Uni_Zurich/IVDA_teaching/preppedStudentCovidData.csv'
              ,sep=',' , float_format='%.0f')




