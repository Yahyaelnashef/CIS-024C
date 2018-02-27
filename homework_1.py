
# coding: utf-8

# In[1]:


x = 5
y = 10

print x,y


# In[2]:


x = 3
y = 9
z = x + y

print z 


# In[3]:


a = 5 
b = 6 
print a,b 


# In[4]:


greeting = "Hello"
person = "Oscar"


# In[5]:


personalGreeting = greeting + " " + person + "!"


# In[6]:


print personalGreeting


# In[8]:


age = int(raw_input("Please Enter your Age: "))
if age > 35:
    print "Age is greater than 35!"
else:
    print "Age is NOT greater than 35!"


# In[13]:


number = 10
newNumber = number%4
print " This is using the / operator  " + str(number/4)
print "  This is using the // operator  " + str(number//4)
print "   This is using the % operator  " + str(newNumber)


# In[14]:


number = 101.35
newNumber = number%4
print " This is using the / operator  " + str(number/4)
print "  This is using the // operator  " + str(number//4)
print "   This is using the % operator  " + str(newNumber)


# In[23]:


myAge = int(21)
yourAge = int(25)
result = myAge == yourAge
print result
hisAge = int(25)
result = hisAge == myAge
print result

