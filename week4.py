# Define a function called `qan_tic`
def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic

# Call the function
res = qan_tic()           # (5b)
print(res)

# Define a function called `qan_tic`
def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)

print(qan_tic)


def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)

tic = "WES.AX"            # (5)
print(tic)                # (6)
qan_tic()

#exercise

lst = [0,1,2,3,4,5,6,7,8,9,19,20,22,23,25,29,30,31]

def is_even_num(lis):
    evennum = []
    for n in lis:
        if n % 2 == 0:
            evennum.append(n)
    print(evennum)
    return evennum

is_even_num(lst)

lst = [2,3,10,14,20,21,25,13,15]
new_lst = [x**2 for x in lst if x**2>150]
print(new_lst)

numbers = [0,1,1,2,5,6,8,2,4,6,8]
new_numbers = {x for x in numbers if x % 2 == 0}
print(new_numbers)

