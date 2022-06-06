#Collections: Counter,namedtuple,

#Counter:
#It counts the number of items in an iterable, and store item as keys and number of times it appears as value
from collections import Counter
from typing import OrderedDict
my_string="aaabbbccccddddeeee"
my_counter=Counter(my_string)
print(my_counter)
print(my_counter.most_common(2))
#help(Counter)
c= Counter(b=4, a=3, c=0, d=-2)
print(list(c.elements()))

#namedtuple:
#they are used to create the tuple which are accessible by fields and better representation
from collections import namedtuple

Point=namedtuple("Point","x,y")
pt=Point(0,4)
print(pt.x,pt.y)
pt._replace(x=33)
print(pt.x,pt.y)
Point.__doc__

#defaultdict
#It is subclass of dict. It returns default value if we call a key which is not present in the dictionary
from collections import defaultdict
my_dict=defaultdict(list,p=5,q=6)
my_dict3=defaultdict(int,p=5,q=6)
my_dict2=defaultdict(lambda: 5,{"p":5,"q":6}) #first argument can be any callable(fuction,class)
my_dict4=defaultdict(lambda: "value does no exist",{"p":5,"q":6})
print(my_dict["g"]) #will return [] as it is the default value

#dque
#It is queu with extra features 
from collections import deque
my_deque=deque([1,2,3,4])
print(my_deque)
print(my_deque.index(1))



#OrderedDict
from collections import OrderedDict
#in normal dicts
d1={}
d1["j"]=9
d1["k"]=11

d2={}
d2["k"]=11
d2["j"]=9

print(d1==d2) # for comparission order of insertion does not matter
print(d1)
print(d2)

#but in ordered dicts
d3=OrderedDict()
d3["j"]=9
d3["k"]=11

d4=OrderedDict()
d4["k"]=11
d4["j"]=9

print(d3==d4) # for comparission order of insertion matters
print(d3)
print(d4)