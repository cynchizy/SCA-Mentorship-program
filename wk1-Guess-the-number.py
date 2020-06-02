
# coding: utf-8

# In[15]:


import random

Game_values = rand.randint(0,20)
User_input=int(input("Guess a number: "))

if Game_values == User_input:
    print("Correct!")
elif Game_values < User_input:
    print("Your guess is too low")
else:
    print("Your guess is too high")

