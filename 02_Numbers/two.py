# Octal Value: 0o<value>
print(0o20)

# Hex Value: 0x<value>
print(0xFF)

# Binary: 0b<value>
print(0b10000)

# CONVERSION: 

# Decimal => Octal
print(oct(64))

# Decimal => Hex
print(hex(64))

# Decimal => Binary
print(bin(10))


# IMPORTANT
print(int('1000',2))
print(int('12',8))
print(int('12',16))

# bitwise
print(4 << 2)
print(4 >> 2)


# import
import random 
print(random.random())
print(random.randint(1, 100))

teas = ["lemon", "masala", "earl gray"]
print(random.choice(teas))
print(random.shuffle(teas))


# Decimal precision
print(0.1 + 0.1 + 0.4)
print(0.1 + 0.1 + 0.1)
print(0.1 + 0.1 + 0.1 - 0.3) # give problem
print((0.1 + 0.1 + 0.1) - 0.3) # give problem

# Decimal Context Manager
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print((Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) - Decimal('0.3'))

# Fraction
from fractions import Fraction
myFraction = Fraction(2/7)
print(myFraction)


# SET: get => Union(|), Intersection(&), defferences(-), Superset 
setone = {1,2,3,4}

print(setone & {1,2,3})
print(setone | {1,2,3})
print(setone - {1,2,3,4}) # set() => {} will not come, Bcz: {} disctionary hote hai
# set(): Empty set

print(type({}))


# Boolean
print(True == 1)
print(False == 0)
print(True is 1) # False: Inside Memory both are diff object value are same internally

print(True + 1) # 5
