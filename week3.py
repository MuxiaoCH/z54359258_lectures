# If statement
happy = True
if happy is True:
    print("I am happy")
print("This will print regardless of the value of happy")

#Boolean logic

var1 = 'a'
var2 = 'a'
print(var1 is var2)
print(var1 == var2)

var3 = ['a']
var4 = ['a']
print(var3 is var4)
print(var3 == var4)

# else statement
b = False
if b is True:
   print("b is True")
else:
   print("b is not True")

# elif statement
a = 0
b = True
if a != 0:
   print("a is non-zero")
elif b is True:
   print("b is True")
elif a < 0 and b is True:
   print("a is negative and b is True")
else:
   print("None of the conditions above hold")

a = -1
b = True
if a != 0:
   print("a is non-zero")
elif b is True:
   print("b is True")
elif a < 0 and b is True:
   print("a is negative and b is True")
else:
   print("None of the conditions above hold")

# pass statement


#exercise 1

hours = input('Enter number of hours you worked this week: ')
hours = int(hours)
normal_rate = 51.45
overload_rate = 88.9

if hours > 35:
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else :
    pay = hours * normal_rate

print(f'This weekly payment is: {pay}')

#Loops

d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for key in d:
    print(key)

d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for key_value_tuple in d.items():
    print(f"key_value_tuple is {key_value_tuple}")
    # Unpacking
    key, value = key_value_tuple
    print(f"KEY: {key} VALUE: {value}")

a = [1,2,3]
b = [1,2,3]

for var1 in a:
    for var2 in b:
        print(var1,var2)


