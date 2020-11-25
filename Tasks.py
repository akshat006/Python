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


# In[3]:


l2 = [1,2,[3,4,5,6],9]


# In[4]:


l2[2].append([7,8])


# In[5]:


l2


# In[6]:


mydict = {
    "color": "Blue",
    "brand": "VW"
}


# In[7]:


mydict.update({"Cost":1000000.00})


# In[8]:


mydict


# In[9]:


mydict.keys()


# In[10]:


mydict.items()


# In[11]:


mylist1 = [10,3,2,1,4]
mylist2 = [7,2,3.4]

mylist3 = mylist1 + mylist2
mylist3


# In[14]:


myset = {1,2,3}


# In[15]:


myset.add(4)


# In[17]:


myset.add(3)


# In[18]:


myset


# In[19]:


myset1 = {1,2,3}
myset2 = {4,5,6}

myset1.difference(myset2)


# In[20]:


myset1.remove(2)


# In[21]:


myset1


# In[22]:


myset1.remove(4)


# In[23]:


myset1.discard(4)


# In[24]:


myset1.isdisjoint(myset2)


# In[42]:


#Replace all ______ with rjust, ljust or center. 

thickness = 5 
c = 'H'

#Top Cone
for i in range(thickness):
    a = (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)
    print (a)

#Bottom Cone
for i in range(thickness):
    e= ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)
    print(e)


# In[43]:


'abc'.center(5,'-')


# In[48]:


import textwrap
a = textwrap.fill('ABCDEFGHIJKLIMNOQRSTUVWXYZ',width=4)
print(a)


# In[63]:


num1 = int(input('Please enter number 1: '))
num2 = int(input('Please enter number 2: '))

print('Choose the operation to perform from the below list')
print(' 1. Press 1 for Addition\n 2. Press 2 for Substraction\n 3. Press 3 for Multiplication\n 4. Press 4 for Division')
oper = int(input('Press the number: '))

if oper == 1:
    print (num1 + num2)
elif oper == 2:
    print(num1 - num2)
elif oper == 3:
    print(num1 * num2)
elif oper==4:
    print(num1/num2)


# In[70]:


"1 w 2 r 3g".title()


# In[66]:


s = "chris alan"
mylist = s.split()
mystring = ''
for i in mylist:
    mystring = mystring + i.capitalize() + ' '


# In[68]:


mystring.strip()


# In[75]:


myset = {1,2,3}


# In[76]:


sum(myset)


# In[82]:


myset.pop(2)


# In[81]:


myset


# In[83]:


n = ''
myset.pop(n)


# In[84]:


s = set(map(int, "1 2 3".split()))


# In[85]:


s


# In[91]:


n = 3
s = {1,2,3}
i = 1

for j in range(i):
    mylist = "remove 2".split()
    if len(mylist) == 2:
        s.remove(int(mylist[1]))
    else:
        s.mylist[0]
        
print(sum(s))


# In[93]:


myset + {4,5}


# In[94]:


myset1 = {4,5}


# In[100]:


i = 9
e = set("1 2 3 4 5 6 7 8 9".split())
j = 9
f = set("10 1 2 3 11 21 55 6 8".split())

comman = e.union(f)

diff1 = e.difference(f)
diff2 = f.difference(e)

comman.update(diff1)


print(comman)


# In[101]:


for count in range(10,1,-1):
    print(count)


# In[102]:


def ab(a,b):
    return b ** a

print(ab(b=2,2))


# In[103]:


0%2


# In[104]:


def fun(x):
    if x %2 == 0:
        return 1
    else:
        return 2


# In[105]:


print(fun(fun(2)))


# In[106]:


2%2


# In[107]:


nums = [1,2,3]
vals = nums
del vals[:]


# In[108]:


nums


# In[109]:


vals


# In[110]:


tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)


# In[111]:


lst = [1,2]

for v in range(2):
    lst.insert(-1,lst[v])
print(lst)


# In[112]:


a =  1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a,b)


# In[113]:


1 //5 + 1/5


# In[114]:


1 // 2


# In[115]:


count = 10

while (count > 0):
    print(count)
    count -= 1


# In[117]:


mylist = [1,2,3,4,5,6]

for i in mylist:
    print(i)


# In[119]:


mydict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

for i in mydict:
    print(mydict[i])


# In[120]:


for i in mydict.values():
    print(i)


# In[121]:


for i in mydict.keys():
    print(i)


# In[122]:


for i in mydict.items():
    print(i)


# In[ ]:




