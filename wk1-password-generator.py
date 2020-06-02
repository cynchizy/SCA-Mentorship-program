
# coding: utf-8

# In[12]:


import string
import random

length = int(input("Enter the length of password: "))
if length <6:
    print("Error!!!! too small,must not be less than 6")

else:
    def getPass(length):
        return "".join(random.choice(string.ascii_letters + string.punctuation + string.digits) for x in range(length))
password = getPass(length)
print (password)

