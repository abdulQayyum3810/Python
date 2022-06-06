import random
print("Random Numbers")
a=random.random() #generates float in interval [0,1]
print(a)
b=random.uniform(1,10) #generate float between the range
print(b)
c=random.randint(1,10) #includes upper and lower bounds
print(c)
d=random.randrange(1,10,step=3) #does not includes upper bound
print(d)
e=random.normalvariate(0,1) #random number from normal distribution
print(e)

#Random item from arrays
my_list=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("Random choices from arrays\n",my_list)
#single item
rand_item=random.choice(my_list)
print(rand_item)
#multiple items
rand_items1=random.choices(my_list,k=3) #Can have duplicates
print("rand_choices",rand_items1)
rand_items2=random.sample(my_list,k=4)
print("rand_sample",rand_items2)
A=random.shuffle(my_list)
print(my_list) #changes original list


#Reproduceable random numbers
print("Reproduceable random numbers")
random.seed(1)
print(random.random())
print(random.randint(1,10))
#reproduction
random.seed(1)
print(random.random())
print(random.randint(1,10))
#give seed a different value to get different random number
random.seed(2)
print(random.random())
print(random.randint(1,10))


#Secret random numbers for Passwords,Account Authentications, Security Tokens and etc
#It takes more time but produces true random number.
import secrets
print("Secret random numbers")
print(secrets.randbelow(10)) #random int below 10
print(secrets.randbits(4)) #k random bit (binary bits) number
print(secrets.choice(my_list))
print(secrets.token_hex(4))

#Numpy random numbers
import numpy as np
print("Using Numpy")
print(np.random.rand(2,3)) #n dimensioned random numbers in interval [0,1)
print(np.random.randint(3,10,(2,2))) #intergers between [a,b)
#shuffling array
np_list=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.random.shuffle(np_list)#shuffles original list along first dimension
print("shuffled_np_list\n",np_list) 
#reproduceable numpy random numbers
print("Reproduceable numpy random numbers")
np.random.seed(1)
print(np.random.rand(2,2))
np.random.seed(1)
print(np.random.rand(2,2))
print "kk"
