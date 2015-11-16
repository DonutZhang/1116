
# coding: utf-8

# In[1]:

class_ntust = {
    "number" : "123",
    "name" : "Jerry"
}
class_ntust


# In[2]:

school = [["班級","甲班"],["姓名","AD"],["學號","222"]]
dict(school)


# In[4]:

school2 = ["中文","cd","ef"]
dict(school2)


# In[6]:

#dict:' 雙項目tuple的串列
lot = [('a','b'),('c','d'),('e','f')]
dict(lot)


# In[7]:

#dict:' 雙項目串列的tuple
tol = (["a","b"],["c","d"],["e","f"])
dict(tol)


# In[9]:

#dict:' 雙字元字串的串列
los = ['ab','cd','ef']
dict(los)


# In[10]:

#dict:' 雙字元字串的tuple
tos = ('ab','cd','ef')
dict(tos)


# In[36]:

#dict 鍵:值
a = {'書':'Book','蘋果':'apple','車':'car'}
dict(a)
a["書"]


# In[38]:

#dict:以update() 合併
pyh = {
    '1':'aa',
    '2':'bb',
    '3':'cc'
}
pyh2 = {
    '4':'dd',
    '2':'22'
}
pyh.update(pyh2)
pyh


# In[40]:

#dict : get() 取值
pyh.get('1')


# In[41]:

pyh.get('11','NON')


# In[43]:

sign = {
    'g':'green',
    'y':'yellow',
    'r':'red'
}
sign.keys()


# In[46]:

sign.values()


# In[47]:

list(sign.values())


# In[48]:

list(sign.items())


# In[56]:

lib = {
    '書':'Book',
}
lib.get(input(''),'error')


# In[58]:

lib = {
    '書':'Book',
}
lib.get(input('輸入:'),'error')


# In[60]:

a = [11,22,33,11]
set(a)


# In[ ]:



