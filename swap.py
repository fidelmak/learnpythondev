a = 6
b = 7
temp = a 
a =b 
b = temp 
print(a)
print(b)

# in a better way 
x = 5
y = 10
x = x + y
y = x - y 
x = x - y
print(x)
print(y)
# we can also make use of XOR 

w = 4
c = 8
w = w ^ c
c = w ^ c
w = w ^ c
print(w)
print(c)


# another way is rot_thwo

f = 2
d = 4 
f,d = d,f 
print(f)
print(d)


