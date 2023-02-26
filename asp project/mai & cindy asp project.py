import pandas as pd
import numpy as np
import matplotlib as plt
import openpyxl as pyx

asia = [' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
       ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
       ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
       ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']

europe = [' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ',
       ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ',
       ' Scandinavia ', ' CIS & Eastern Europe ']

other = [' USA ', ' Canada ',
       ' Australia ', ' New Zealand ', ' Africa ']

# read dataset
visit_raw_df = pd.read_excel(r'Project_File.xlsx')

# give a name for 1st column
visit_raw_df.columns.values[0] = "period_year"
#visit_raw_df = visit_raw_df.rename(columns={'   ': 'date'})
print(visit_raw_df.columns)

'''
# replace na to nan
data2 = visit_raw_df.replace(" na ", np.nan)
print(data2)
print(data2.dropna())
'''

# split period_year into year only
visit_raw_df["year"] = visit_raw_df["period_year"].str.split().str[0]
print(visit_raw_df.head())
print(visit_raw_df.dtypes)

# cast the year column to integer
visit_raw_df = visit_raw_df.astype({'year':'int'})
print(visit_raw_df.dtypes)

# filter row by year 2008 to 2017


# cast all column to integer
visit_raw_df = visit_raw_df.astype({'   ':'int'})
print(visit_raw_df.dtypes)

# select the column according to region asia


# sum + sort value in descending order



# plot the graph, bar graph





