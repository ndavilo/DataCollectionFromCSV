#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from sqlalchemy import create_engine


# In[10]:


user = 'postgres'
port = '5432'
db = 'may'
host = 'localhost'
pwd = '****'


# In[11]:


engine = create_engine(f"postgresql://{user}:{pwd}@{host}:{port}/{db}")


# In[24]:


order_sql = "SELECT make, model, price FROM car;"
cars = pd.read_sql_query(order_sql, engine)
print(cars)


# In[22]:


df = pd.DataFrame(cars)
df.to_csv (r'/Users/chukwunonsodavid/Downloads/car.csv', index = False)


# In[25]:


import csv


# In[26]:


with open('/Users/chukwunonsodavid/Downloads/car.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


# In[27]:


data


# In[28]:


with open('/Users/chukwunonsodavid/Downloads/car.csv', newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]


# In[29]:


data


# In[37]:


with open('/Users/chukwunonsodavid/Downloads/car.csv', newline='') as f:
    data = [dict(i) for i in csv.DictReader(f)]


# In[48]:


data


# In[111]:


make=[]
model=[]
price=[]
with open('/Users/chukwunonsodavid/Downloads/car.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for d in data:
    make.append(d[0])
    model.append(d[1])
    price.append(d[2])

cars = zip(make, model, price)

for m, mo, p in cars:
    print(f'car: \t'+ m + '\t' + mo +'\t' + p)


# In[104]:


cars_pd = pd.read_csv('/Users/chukwunonsodavid/Downloads/car.csv')


# In[105]:


cars_pd


# In[135]:


import matplotlib.pyplot as plt
plt.close("all")
import numpy as np


# In[124]:


cars_pd.head(5).plot(x="make", y="price");


# In[127]:


cars_pd.head(5).plot.bar(x="make", y="price");


# In[ ]:





# In[140]:


np.random.rand(10, 4)


# In[148]:


int_price = []
price.pop(0)
for p in price:
    int_price.append(float(p))


# In[156]:


ts = pd.Series(int_price, make[2:])
ts = ts.cumsum()
ts.plot();


# In[ ]:




