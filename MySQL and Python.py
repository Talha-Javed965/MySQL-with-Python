#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install mysql-connector-python')


# In[28]:


import mysql.connector


# In[35]:


# Connecting to sakila database in MySql workbench
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Pakistan121&",
  database = "sakila"
)

print(mydb)


# In[36]:


# SELECT Statement in SQL

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM actor")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# In[37]:


mycursor.execute("SELECT * FROM actor")
myresult = mycursor.fetchone()

print(myresult)


# In[61]:


# WHERE Statement in SQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Pakistan121&",
  database = "sakila"
)

print(mydb)


mycursor = mydb.cursor()
sql = "SELECT * FROM actor WHERE first_name = 'JOHN'"
mycursor.execute(sql)
result = mycursor.fetchall()
for x in result:
    print(x)


# In[69]:


# Using WildCard with WHERE Statement in SQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Pakistan121&",
  database = "sakila"
)

print(mydb)


mycursor = mydb.cursor()
sql = "SELECT * FROM actor WHERE first_name LIKE '%%CH%%'"
mycursor.execute(sql)
result = mycursor.fetchall()
for x in result:
    print(x)


# In[71]:


#Escape query values by using the placholder %s method:
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Pakistan121&",
  database = "sakila"
)

print(mydb)


mycursor = mydb.cursor()
sql = "SELECT * FROM actor WHERE first_name = %s"
f_name = ("CHRIS",)
mycursor.execute(sql,f_name)
result = mycursor.fetchall()
for x in result:
    print(x)


# In[108]:


# Using OrderBy Statement in Query
sql = "SELECT * FROM actor ORDER BY first_name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# In[109]:


import csv


# In[111]:



# Assuming myresult contains the data retrieved from MySQL

# Open the CSV file in text mode (no need for 'wb' mode in Python 3+)
with open("temp_Mysql.csv", "w", newline='', encoding='utf-8') as file:
    # Create a CSV writer object
    myFile = csv.writer(file)
    
    # Write the rows to the CSV file
    myFile.writerows(myresult)


# In[135]:


# import pandas with shortcut 'pd' 
import pandas as pd 

# read_csv function which is used to read the required CSV file 
data = pd.read_csv('temp_Mysql.csv') 

# display 
print("Original 'input.csv' CSV Data: \n") 
print(data) 

# drop function which is used in removing or deleting rows or columns from the CSV files 
# axis define whether the operation will be on rows or column
data = data.drop(data.columns[3], axis=1) 

# display 
print("\nCSV Data after deleting the column 'year':\n") 
print(data)


# In[141]:


sql = "SELECT * FROM country FULL JOIN actor "
mycursor.execute(sql)
count_reslt = mycursor.fetchall()

for x in count_reslt:
    print (x)


# In[ ]:




