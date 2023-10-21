#_________arithmethic operators
a = 12.2
b = 13.2
print(a+b)  #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a/b)  #division
print(a//b) #floor division(int division)
print(a%b)  #modulus    
print(a**b) #exponent
print(a**0.5) #square root

#_________comparison operators


#_________Assignment operators
a = 12  


#_________Bitwise operators


#_________shorthand operators
a += 2  #a = a + 2
a -= 2  #a = a - 2
a *= 2  #a = a * 2
a /= 2  #a = a / 2
a //= 2 #a = a // 2
a = int(a)
a %= 2  #a = a % 2
a **= 2 #a = a ** 2
a &= 2  #a = a & 2 #&represent bitwise and
a |= 2  #a = a | 2 #|represent bitwise or
a ^= 2  #a = a ^ 2 #^represent bitwise xor
a >>= 2 #a = a >> 2 #>>represent bitwise right shift
a <<= 2 #a = a << 2 #<<represent bitwise left shift


#_________Identity operators

#is operator is used to check if two variables point the same object
a = 12
b = "12"
c = 12

print("a and c is same: ", a is c)
print(type(a))
print(type(a) is int) 
#is not operator is used to check if two variables do not point the same object
print(type(b))
print(type(b) is not int) 



#_________Membership operators
#in operator is used to check if a value is present in a sequence

names = "jennie, lisa, rose, jisoo"
name1 = "lisa"
name2 = "lisa is cool."

print(name1 in name2)
print(name2 in names)
