#!/usr/bin/env python
# coding: utf-8

# In[1]:


#5\2\2022 class 3


a =[1,2,3]
b =[4,5,6]
a.append(b)#last la place (list in list)
print(a)


# In[2]:


a =[1,2,3]
b =[4,5,6]
a.extend(b) #place in same list (same ah place agum)
print(a)


# In[3]:


#copy
# copy is classified into two types
#1 shallow memory 2 deep memory
#shallow memory = shared memory #deep memory = different memory

#shared memory
a = [1,2,3]
b=a
a.append(4)
print(a)
print(b)


# In[4]:


#different memory
a=[1,2,3]
b=a.copy()
a.append(4)
print(a)
print(b)


# In[5]:


#tuple 
#tuple which are immutable (non editable) which is faster than list and brackets are changed
a = (1,2,3)
print(type(a))


# In[6]:


a = (1,2,3)
print(isinstance(a,tuple))


# In[7]:


a.append(4)


# In[8]:


print(min(a))


# In[9]:


print(max(a))


# In[10]:


print(sorted(a))


# In[11]:


print(a.index('2'))


# In[12]:


print(a.index(2)) #index only work ,rindex,rfind


# In[13]:


print(a.rindex(2))


# In[14]:


print(a.find(2))


# In[15]:


print(a[0])


# In[16]:


print(a[: :-1])


# In[17]:


a.find(2)


# In[18]:


a ={1,2,3}                                  #set
print(type(a))


# In[19]:


print(isinstance(a,set))


# In[20]:


print(isinstance(a,set))


# In[21]:


a = {1,1,1,2,2,2,3,3,3}
print(a) #set removes duplicate


# In[22]:


a = ['hello','hello']
a = list(set(a))
print (a)
a = set(list(a)) 


# In[23]:


a = {1,2,3}
print(a[0]) #indexing rindexing,find,rfind wont work in set


# In[24]:


a ={1,2,3}
print(min(a))
print(max(a))
print(sorted(a))


# In[25]:


print(a.rindex("a"))


# In[26]:


print(a.find("a"))


# In[27]:


a = {1,2,3}
a.add(4)
print(a)


# In[29]:


a = {1,10,20,3,4}
print(a)


# In[33]:


a ={1,2,3,4,5}
b ={4,5,6,7,8}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))


# In[34]:


a = {1,2}
b={1,2,3,4}
print(a.issuperset(b))


# In[35]:


print(a.issubset(b))


# In[36]:


print(b.issuperset(a))


# In[37]:


print(b.issubset(a))


# In[38]:


a ={1,2,3}
b={3,4,5}
print(a-b) #its works only in set


# In[39]:


a = [1,2,3]
b = [4,5,6]
print(a+b)   #it is works in only list


# In[ ]:




