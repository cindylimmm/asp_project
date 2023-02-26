

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_excel(r"./Project_File.xlsx")


# dimension of dataset
dataset_dim = dataset.shape


# renaming the first column to date
dataset_rename= dataset.rename(columns={dataset.columns[0]:'year_month'})
print(dataset_rename)

# split the year_month to year and month columns
dataset_rename["year"] = dataset_rename["year_month"].str.split().str[0]
dataset_rename["month"] = dataset_rename["year_month"].str.split().str[1]

print(dataset_rename)

# creating region
region_asia_df = dataset_rename[['year', ' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
       ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
       ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
       ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']]


# cast to integer
region_asia_df = region_asia_df.astype({'year':'int'})


# filtering to year
years_df = region_asia_df[(region_asia_df["year"] >= 2008) & (region_asia_df["year"] <= 2017)]

years_df = years_df.astype('int')

print(years_df.dtypes)
# sum
total_sum_df = years_df.sum()

print(total_sum_df)

# remove year column
total_sum_df = total_sum_df.drop('year', axis = 0)

print(total_sum_df)
# plot
ps = total_sum_df[:].sort_values()
index = np.arange(len(ps.index))
plt.xlabel("Country")
plt.ylabel("total sum")
plt.xticks(index, ps.index, fontsize=12, rotation=90)
plt.title("visitor by country")
plt.bar(ps.index, ps.values)
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.show()


# top 3
total_sum_df = total_sum_df.sort_values(ascending=False)
print(total_sum_df.head(3))




