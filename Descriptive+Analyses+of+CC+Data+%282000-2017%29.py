
# coding: utf-8

# This notebook contains code and output of descriptive analyses for the 2000-2017 CC dataset after cleaning

# # Setting up the Python environment
# Ensure that the following packages have been installed using "pip install <packagename>" from the python command line before running the next chunk:
# - pandas
# - gsspread
# - oauth2client.service_account
# 
# **Note: This chunk takes a while to execute.**

# In[1]:

# import gspread

# from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
#Magic to make plots display
# get_ipython().magic('matplotlib notebook')
import matplotlib.pyplot as plt

# use creds to create a client to interact with the Google Drive API
#scope = ['https://spreadsheets.google.com/feeds']
#creds = ServiceAccountCredentials.from_json_keyfile_name('TD_client.json', scope)
#client = gspread.authorize(creds)


# Now we read the data in from Google Sheets

# In[2]:

#data = client.open("cleaned CC data 2000-2017.csv").sheet1
#df=pd.DataFrame(data.get_all_records())
df = pd.DataFrame("Descriptive Analyses of CC Data (2000-2017).csv")

# Here we remove unnecessary columns from df.

# In[3]:

print(df.columns)
df = df[['autotomized','date','location','mass','meters','misc','new.recap','paint.mark','painted','rtl','sex','sighting','species','svl','tl','toes','vial','year']]
print(df.columns)


# Here we need to force svl, tl, rtl and mass to numeric variables

# In[ ]:




# The following tables exclude non-ideal values for the variables in question, but once the columns are cleaned in the source file, this won't be an issue.

# Drop data for species other than 'j' and 'v'.

# In[4]:

print(df.shape)
species2keep=['j','v']
df = df.loc[df.species.isin(species2keep)]
print (df.shape)


# Dropping non-ideal data for sex.

# In[5]:

print(df.shape)
sex2keep=['m','f']
df = df.loc[df.sex.isin(sex2keep)]
print (df.shape)


# In[6]:

df.groupby(['species','sex'])['autotomized'].count()


# In[7]:

df.groupby(['species','sex','autotomized'])['new.recap'].count()


# In[8]:

plt.figure()
df.svl.plot.box


# In[9]:

plt.figure()
df.tl.plot.box


# In[10]:

plt.figure()
df.rtl.plot.box


# In[11]:

plt.figure()
df.mass.plot.box


# Add groupby arguments that include species ageclass and sex for all summaries
#     - consider adding year
# Types of visualizations:
# - tables (autotomy, new/recap (1st sightings only)
# - boxplots (svl, tl, rtl, mass)
# - histograms (age class (svl), meters (location))

# For inferential stats
# - differences:
#     - between seasons within years 
#     - between years (weather and fire)
#     - population density (revist how to calculate this)
#         - ran study until flatline
#         - do we need to account for person-hours still?

# In[12]:

plt.figure()
df.rtl.plot.hist


# In[13]:

plt.figure()
df.svl.plot.hist


# In[14]:

plt.figure()
df.meters.plot.hist


# In[ ]:



