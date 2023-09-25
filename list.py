# lets talk about list in python 
names = ['Benson', 'Joy', 'Fedrick',]
ages =[34, 56, 76,]

print(names[1:3])
print(names[-2])

print()

full = [names, ages ]

print(full)

# list is immutable 

ages.append(24)

print(ages)

names.insert(2,'Fidelis')
print(names)

# deleting by index number 

ages.pop(3)

print(ages)

names.pop()

print(names)

#multiple values 

names.extend(['Bidemi','Sholla', 'BadBoy'])

print(names)



print(min(ages))
print(max(ages))
ages.sort()
print(ages)