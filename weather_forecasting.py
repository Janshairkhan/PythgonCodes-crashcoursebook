#!/usr/bin/env python
# coding: utf-8

# In[2]:


name = "Pakistani"
dob = 1947
print(f" I am {name} and it came into being {dob}.")


# In[8]:


bicycele = ['Yamaha','civic','honda','redline','specialized']
message = "My first bicycele was " + bicycele[0].title() + "."
print(message)


# In[6]:


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."


# In[7]:


print(message)


# In[13]:


list1 = ["apple","banana","cherry","mango"]
message = "My favaourite fruit is "  +  list1[-1].title() +"."
print(message)


# In[ ]:





# In[15]:


pip install requests
import requests


# In[21]:


city = input('input the city name')
print(city)
#city = 'Karachi'
print('Displaying Weather report for: ' + city)
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)
print(res.text)


# In[32]:


name  = "PAKISTAN"
for i in name [::-1]:
    print(i, end = "")


# In[33]:


lst = [1,2,3,4,5]
print(lst[::-1])


# In[34]:


lst[1]


# In[39]:


lst1 = ["Hassan","javaid","Uzair"]
lst2= ["Ali","Iqbal","Khan"]


# In[42]:


for name in lst1:
    for sirname in lst2:
        print(f"{name}{sirname}")


# In[46]:


#ZIP FUNCTION TO PRINT FIRST AND LAST NAME
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)


# In[47]:


print(tuple(x))


# In[48]:


import numpy


# In[56]:


#NUMPY FUNCTION

box = [22,33,44,66,77,88,66,90,13]
x = numpy.all(box)
print(x)


# In[79]:


lst1 =['kamran','usama','ahsan','imad']
lst2 = ['bukhari','ali','aijaz','khan']
for name in lst1:
    print(f"{name} {lst2[lst1.index(name)]}",end = " ")
    


# In[61]:


num = [1,2,3,4,5]
alp = ['a','b','c','d','e']
print(tuple(zip(num,alp)))


# In[ ]:




