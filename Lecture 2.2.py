#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
list of lists  [   []     ]
list of dicts  [   {}     ]
dict of lists  {   []     }
dict of dicts  {   {}     }

'''


# In[ ]:


'''
to call dictionary, go by the keys, which are the ones before colon
to call list, go by index which starts from 0
'''


# In[ ]:





# In[ ]:





# ## dict of lists

# In[1]:


stocks_nested_list = {
    "APPL": ["Apple", 101.32, "NASDAQ", 937.7],
    "MU": ["Micron Technology", 32.12, "NASDAQ", 48.03],
    "AMD": ["Advanced Micro Devices", 23.12, "NASDAQ", 29.94],
    "TWTR": ["Twitter", 34.40, "NASDAQ", 26.42]
}


# In[2]:


type(stocks_nested_list)


# In[3]:


stocks_nested_list.keys()


# In[4]:


type(stocks_nested_list["MU"])


# In[ ]:


len(stocks)


# In[ ]:


#### ex2


# In[14]:


stocks_nested_list = {
    "nasdaq":{
    "APPL": ["Apple", 101.32, 937.7],
    "MU": ["Micron Technology", 32.12, 48.03],
    "AMD": ["Advanced Micro Devices", 23.12, 29.94],
    "TWTR": ["Twitter", 34.40, 26.42]
},
    "nyse": {
        "ABC":[
                {"Stock_Name": "ABC Company",
               "Stock_Ticker": "ABC",
               "Closing_Price": 26.89}
              ],
        "DFG":[
               {"Stock_Name": "DFG Company",
               "Stock_Ticker": "DFG",
               "Closing_Price": 89.26}
              ]
    }
}


# In[15]:


len(stocks_nested_list)


# In[16]:


stocks_nested_list.keys()


# In[18]:


type(stocks_nested_list["nyse"])


# In[19]:


stocks_nested_list["nyse"].keys()


# In[20]:


stocks_nested_list["nyse"]["ABC"]


# In[21]:


stocks_nested_dict = {
    "APPL": {
        "name": "Apple",
        "exchange": "NASDAQ",
        "market_cap": 937.7
    },
    "MU": {
        "name": "Micron Technology",
        "exchange": "NASDAQ",
        "market_cap": 48.03
    },
    "AMD": {
        "name": "Advanced Micro Devices",
        "exchange": "NASDAQ",
        "market_cap": 29.94
    },
    "TWTR": {
        "name": "Twitter",
        "exchange": "NASDAQ",
        "market_cap": 26.42
    }
}


# In[23]:


stocks_nested_dict.keys()


# In[24]:


stocks_nested_dict["AMD"]


# In[25]:


type(stocks_nested_dict["AMD"])


# In[26]:


stocks_nested_dict["AMD"].keys()


# In[27]:


stocks_nested_dict["AMD"]["market_cap"]


# # for loops

# In[29]:


'''
for x in something:
    do somecode
x is the iteration point
something is the iterable
somecode is whatever you want to do with it
'''


# In[31]:


for x in range(10):
    print(x)


# In[32]:


for x in range(10,20):
    print(x)


# In[33]:


name = "chicago"
for x in name:
    print(x)


# In[34]:


battlestars =[{'Ship': 'Pegasus',
  'Commander': 'Admiral Helena Cain',
  'Pilots': ['Whiplash', 'Thumper']},
 {'Ship': 'Galactica',
  'Commander': 'Admiral William Adama',
  'Pilots': ['Starbuck', 'Apollo', 'Helo', 'Athena']}]


# In[35]:


type(battlestars)


# In[36]:


len(battlestars)


# In[37]:


battlestars[1]


# In[38]:


battlestars[1].keys()


# In[43]:


for k,v in battlestars[1].items():
    print(k,v)


# # ifelse

# In[44]:


'''
if someCondition:
    someCode
elif someCondition:
    someCode
else:
    someCode
'''


# In[46]:


x = 5
y = 4

if x == 5 and y == 4:
    print("x is 5 and y is 4")
else:
    print("x is not 5 and y is not 4")


# In[47]:


x = 5
y = 4

if x == 5 and y == 3:
    print("x is 5 and y is 4")
else:
    print("x is not 5 and y is not 4")


# In[51]:


y = 9

if y != 9:
    print("y is not 1")
else:
    print("y is something else")


# In[52]:


x = 1
y = 8

if x == 1 and y < 10:
    print("do something")
else:
    print("don't do something")


# In[53]:


x = 1
y = 8

if y < 10:
    if x > 0:
        print("do something")
    else:
        print("don't do something")


# In[54]:


x = 1
y = 8

if y < 10:
    if x > 1:
        print("do something")
    elif y >= 8:
        print("here is y")
    else:
        print("don't do something")


# # boolean

# In[57]:


name = "Yohan"

group_one = ["Greg","Tony","Susan"]
group_two = ["Carla","Yohan","Jefferson"]

if name in group_one:
    print(name + " is in group one")
elif name in group_two:
    print(name + " is in group two")
else:
    print(name + "does not have a group yet")


# In[58]:


x = 5
y = 10

if 2 * x>= y:
    print("2 times the x is y")
else:
    print("something else")


# In[61]:


x = 5
y = 10

if (2 * x>= y) and (y / 5 > x):
    print("2 times the x is y")
else:
    print("something else")


# # while loop

# In[64]:


x = "y"

while x == "y":
    p = 5
    l = 4
    k = p*l/10**p
    print(k)
    x = input("enter either y or n")


# In[68]:


x = "y"

while x == "y":
    p = 5
    l = 4
    k = p*l/10**p
    print(k)
    
    for x in list(range(5)):
        print(x)
        
   


# # functions

# In[ ]:


'''

def function_name(parameter1,parameter2, ......):
    someCode

'''


# In[69]:


def func():
    a = 5
    b = 4
    return a*b


# In[70]:


func()


# In[71]:


market_price = 78
number_of_shares = 1000

def market_cap(market_price, number_of_shares):
    
    cap = market_price * number_of_shares
    
    return cap


# In[72]:


market_cap(market_price,number_of_shares)


# In[ ]:


# write a function that calculates future value 
# FV=PV(1+i)n


# In[81]:


def future_value(pv,i,n):
    
    fv = (pv * (1 + i))**n
    
    return fv
    


# In[82]:


future_value(100,0.6,12)


# ### all in one

# In[ ]:


def samplefunction(a = 5, b= 7, c = 8, d = 9, f = 3):
    
    g = a + b
    print(f"a plus b is {g}")

    x = "y"

    while x =="y":
        p = 5
        l = 4
        k = p*l/10**p-1

        print(f"k value is{k}")
        
        if ((c == d) and (f * 4 = 12)) or (a > b):
            for x in list(range(5)):
                print(x)
                
            word = "peace"
            for x in word:
                print(x)
                
        elif f * c == 24:
            
            print("do something")
            
        else:
            mylist = ["a","b",99]
            for x in mylist:
                print(x)

        x = input("enter y or n")


# In[95]:


samplefunction(a = 99, b = 11, c = 7, d = 7, f = 21)


# In[ ]:




