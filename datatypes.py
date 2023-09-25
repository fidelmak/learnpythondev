# types of data types in python are : NONE, NUMERIC, LIST, TUPLE, SET, RANGE, DICTIONARY OR MAP 
# NUMERIC is categorized into : INT, FLOAT, COMPLEX BOOL
num = 2.5 # float
num2 = 5
num3 = 6 + 8j # a + bj this is a complex number 

# to convert from each numerics 

a = 5.8
b = int(a)
# to convert to float 

k = float(b)
# to convert to complex

k = 5
c = complex(b, k)
# we have boolean , we always take decision which are true or false 

b < k
bool = b< k 
print(type(bool))

# bool is about true and false , in programming we us True as 1 and false as 0
print(int(True))
print(int(False))
# we also have sequence which are List, Tuple, Set, String, Range 
MyList = [1,2,3,4,5]
print(type(MyList))
# we also have set
mySet = {1,1,23,45,65}
print(mySet)
print(type(mySet))

# we also have tuples 
t = (1,2,3,4)
# we also have string 
s = "paul"
print(type(s))
# we also have range 
d = range(10)
print(d)
# to print the range of numbers we can pass it to a list 
print(list(d))



