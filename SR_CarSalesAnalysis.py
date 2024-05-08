#!/usr/bin/env python
# coding: utf-8

# Car Sales Analysis Using Python

# 

# In[52]:


#Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[53]:


#import dataset

Car_data = pd.read_csv(r'C:\Users\Sudharshan Ravikumar\Downloads\archive (2)\CARS.csv')


# In[54]:


Car_data.head()


# In[55]:


Car_data.shape


# In[56]:


Car_data.columns


# In[57]:


Car_data.info()


# #### Data Cleaning
# 
# * Find Null values in the dataset

# In[58]:


Car_data.isnull()


# In[59]:


# Find the no. of null values and the column
Car_data.isnull().sum()


# In[60]:


Car_data['Cylinders'].fillna(Car_data['Cylinders'].mean(), inplace =True)


# In[61]:


Car_data.isnull().sum()


# #### What are the different types of car make in our dataset and how many times did each make occur

# In[62]:


Car_data.head(1)


# In[63]:


Car_Makecount=Car_data['Make'].value_counts()
print(Car_Makecount)


# In[64]:


plt.figure(figsize=(10,5))
Car_data['Make'].value_counts().plot(kind='bar', color='red')
plt.title('Number of Cars by Make')
plt.xlabel('Make')
plt.ylabel('Number of Cars')
plt.show()


# ##### Show all records where the origin are in Europe or Asia

# In[65]:


Car_data.head(1)


# In[66]:


Car_data [Car_data ['Origin'].isin (['Asia', 'Europe']) ] 


# In[67]:


filtered_data = Car_data[Car_data['Origin'].isin(['Asia', 'Europe'])]
filtered_data['Origin'].value_counts().plot(kind='bar', color='red')
plt.title('Number of Cars by Origin')
plt.xlabel('Origin')
plt.ylabel('Number of Cars')
plt.show()


# In[68]:


#Creates a new column and separate the dollar sign
Car_data['Price'] = Car_data['Invoice'].str.replace('$','')
Car_data.head()


# In[69]:


Car_data.dtypes


# ##### Remove all records where weight is above 4000

# In[70]:


Car_data.head(1)


# In[71]:


Car_data [Car_data['Weight'] > 4000 ] #show data in relations to weight greater than 4000


# In[72]:


# ~ this symbol is used to remove the values greater than 40000
Car_data [~(Car_data['Weight'] > 4000) ]


# In[73]:


Car_data .shape


# ##### Increase all the values of _'MPG_City' by 3 columns

# In[74]:


Car_data['MPG_City'] =  Car_data['MPG_City'].apply(lambda x:x+3)


# In[75]:


Car_data


# In[76]:


Car_data.shape


# In[77]:


# Remove non-numeric characters from 'Price' column
Car_data['Price'] = Car_data['Price'].str.replace(",","").replace(" ","")

# Convert 'Price' column to integer
Car_data['Price'] = Car_data['Price'].astype(int)

# check the data type of 'Price' column
print(Car_data['Price'].dtype)


# In[78]:


#create a figure with larger size
plt.figure(figsize=(12,8))

# calculate the average price for cars from Asia and Europe
avg_price = Car_data[Car_data['Origin'].isin(['Asia', 'Europe'])]['Price'].mean()

# create line plot for cars from Asia and Europe
sns.lineplot(x='Make', y='Price', data=Car_data[Car_data['Origin'].isin(['Asia', 'Europe'])], color='blue', marker='o',hue='Origin')

# add a horizontal line to indicate the average price
plt.axhline(y=avg_price, color='red', linestyle='dashed')

#set labels and title
plt.title('Average Car Prices by Make (Asia and Europe)', fontsize=20)
plt.xlabel('Make',fontsize=14)
plt.ylabel('Price',fontsize=14)
plt.legend(loc='upper left',fontsize=14)
plt.show()


# In[79]:


# Sort the dataframe by Price in descending order
Car_data = Car_data.sort_values(by='Price',ascending=False)

# Select the top 15 car types
Car_data = Car_data.head(15)

# Create a bar plot
sns.barplot(x = 'Make', y = 'Price', data = Car_data, hue = 'Origin',palette='Reds')


# Set labels and titles
plt.title("Price Distribution of Top 7 Car Types by Make and Origin", fontsize=20)
plt.xlabel("Make",fontsize=14)
plt.ylabel("Price",fontsize=14)
plt.xticks(rotation=90)
plt.legend(loc='upper left',fontsize=14)
plt.show()


# In[80]:


sns.set_style("whitegrid")
# create a bar plot with larger size
plt.figure(figsize=(13,7))
sns.barplot(x = Car_data['Make'], y = 'Price', data = Car_data, hue = 'Origin', palette='Reds')

#set labels and titles
plt.title("Price Distribution by No. of Make", fontsize=16)
plt.xlabel("Make",fontsize=8)
plt.ylabel("Price",fontsize=8)



# * There is a positive relationship between weight and horsepower, meaning that as the weight of a car increases, so does its horsepower.
# * Some European car manufacturers have models that defy the trend of the relationship between weight and horsepower, as they have cars that weigh less than 4500 pounds and have a horsepower of nearly 500.

# In[81]:


#group the data by car type and calculate the average cylinder size
car_data_grouped = Car_data.groupby('Make').mean()[['Cylinders']]

#sort the data by average cylinder size in descending order
car_data_grouped.sort_values(by='Cylinders', ascending=False, inplace=True)

#select the top 10 car types by average cylinder size
top_10_car_types = car_data_grouped.head(10)
#plot size
plt.figure(figsize=(12,8))
#create a bar plot of the average cylinder size by top 10 car types
sns.barplot(x=top_10_car_types.index, y='Cylinders', palette='Reds', data=top_10_car_types)

#set the title and labels
plt.title("Average Cylinder Size by Top 10 Car Types", fontsize=16)
plt.xlabel("Car Type")
plt.ylabel("Average Cylinder Size")
plt.xticks(rotation=45) # to rotate x_axis label by 45 degrees
plt.show()


# * The chart shows that Hummer has the highest amount of car cylinder 
# * This seems very likely as Hummer are larger Cars and can contain an average of 8 cylinders in a car
# * Cadillac and Lincoln follow 2nd and 3rd with close average of 7.8 and 7.5 

# In[82]:


#Plot size
plt.figure(figsize=(14,8))

#create a scatter plot of engine size vs horsepower
sns.scatterplot(x='EngineSize', y='Horsepower', data=Car_data, hue='Origin', palette = 'Reds')

#set the title, labels and size of the title
plt.title("Relation between Engine Size and Horsepower by Origin", fontsize=15)
plt.xlabel("Engine Size", fontsize=12)
plt.ylabel("Horsepower", fontsize=12)
plt.legend(loc='upper left') # to set location of legend
plt.show()


# In[84]:


#plot size
plt.figure(figsize=(30,20))

sns.lmplot(x='EngineSize', y='Horsepower', data=Car_data, hue='Origin',palette = 'Reds', fit_reg=True)
#set the title and labels
plt.title("Relation between EngineSize and Horsepower by Origin", fontsize=16)
plt.xlabel("Engine Size")
plt.ylabel("Horsepower")
plt.show()


# * This chart shows a correlation between Engine size and Horsepower and also similarities in the Origins.
# * This trend seems to follow through perfectly with the USA 
# * In Europe we can see that some cars have smaller engine Sizes but very high horsepower

# ~Mary O Anene
