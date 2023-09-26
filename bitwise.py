# he we have compliment( ~) tilde, left shift(<<), or(|) XOR (^), (>>)

# compliment gives reverse 

print(~12) # this will give you a negative 13, we have 2's compliment, we dont store negative numbers in the computer system , you have to convert all numbers to positive number , to find 2's compliment you have to add 1's compliment + 1 , convert 13 to binary, then change it to compliment and add 1. 


# we can use bitwise AND , bitwise OR
print(12 & 13) # remember 12 = 00001100 and 13= 00001101, so using the AND operator we have 00001100, 1 stands for true while 0 stands for false , we only have T when its TT in AND statement 
# for OR 

print(12 | 13) # in OR statement , you only have T when one of the statement is T 

# we have XOR 
print(12 ^ 13)

# using <<, left shift
print(10 << 2) # we have to convert 10 to binary which is 1010, so you shift two zeros to the right 101000 which is now 40, note in right shift you are gaining bits 

# lets talk about right shift >>>

print(10 >> 2) # this shifts the zeros , that is you are losing two zeros to the right 



