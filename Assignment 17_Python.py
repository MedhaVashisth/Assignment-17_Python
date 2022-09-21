#!/usr/bin/env python
# coding: utf-8

# In[3]:


def print_header(section: str):
    print('--------------------------')
    print('Start of section ' + section)


# In[4]:


def print_footer(section: str):
    print('End of section ' + section)


# In[9]:


guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')


# In[11]:


guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break 
    elif start > guess_me:
        print('oops')
        break
    start += 1


# In[13]:


for value in [3, 2, 1, 0]:
    print(value)


# In[16]:


even = [number for number in range(10) if number % 2 == 0]


# In[17]:


even


# In[18]:


squares = {key: key*key for key in range(10)}


# In[19]:


squares


# In[22]:


odd = {number for number in range(10) if number % 2 == 1}


# In[23]:


odd


# In[24]:


for thing in ('Got %s' % number for number in range(10)):
    print(thing)


# In[25]:


def good():
    return ['Harry', 'Ron', 'Hermione']


# In[27]:


good()


# In[29]:


def get_odds():
    for number in range(1, 10, 2):
        yield number 
for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print("The third odd number is", number)
        break


# In[31]:


def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@test
def greeting():
    print("Greetings, Earthling")


# In[32]:


greeting()


# In[47]:


class OopsException (Exception):
    pass
   
    

    raise OopsException('caught an oops')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
__main__.OopsException

    
try:
    raise OopsException
    except OopsException:
        print('Caught an oops')


# In[45]:


titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
movies 
{'Crewel Fate': 'A haunted yarn shop', 'Creature of Habit': 'A nun turnsinto a monster'}


# In[ ]:




