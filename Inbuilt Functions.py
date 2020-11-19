#!/usr/bin/env python
# coding: utf-8

# In[2]:


mylist = [4,5,8,20]
max(mylist)


# In[6]:


mylist1 = [1,2,3]

list(enumerate(mylist1))


# In[8]:


mylist1 = [2,4,5,2]
mylist2 = [4,6,4]

list(zip(mylist1,mylist2))


# In[13]:


mystring = "Hello World"

x = mystring.count('o')

print(x)


# In[14]:


mystring.find("World")


# In[15]:


mystring.index("World")


# In[20]:


mystring = 'Hello'
mystring1 = '12ABC'

a = mystring.isalpha()
b = mystring1.isalpha()

print (a,b)


# In[22]:


mystring = "Hello World"

mystring.split()


# In[25]:


mystring = '   Test   '

mystring.lstrip()


# In[27]:


mystring.rstrip()


# In[28]:


mystring.strip()


# In[29]:


mydict = {83:  80};

txt = "Hello Sam!";

print(txt.translate(mydict));


# In[30]:


mystring = "HeLlO wOrLd"

mystring.swapcase()


# In[31]:


mystring = "Welcome to Python!!"

'to' in mystring


# In[1]:


mylist = [1,2,3,4]


# In[2]:


sum(mylist)


# In[3]:


mylist = [1,1,2,4,2,12,2,2,1,2,1,1,1]
mylist.count(1)


# In[4]:


len(mylist)


# In[5]:


min(mylist)


# In[6]:


max(mylist)


# In[9]:


mylist.sort(reverse = True)


# In[10]:


mylist


# In[11]:


del mylist[1]


# In[12]:


mylist


# In[15]:


mylist.remove(1)


# In[ ]:





# In[16]:


mylist


# In[17]:


l1 = [10, 20, [30, 40, [50, 60], 80], 90, 100]


# In[20]:


l1[2][2].append(70)


# In[22]:


l1


# In[23]:


l2 = [1,2,[3,4,5,6],9]


# In[24]:


l2[2].append([7,8])


# In[25]:


l2

