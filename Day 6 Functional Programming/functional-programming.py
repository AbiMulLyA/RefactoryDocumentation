# Functional Programming

a = 3 
b = 4

def some_func():
    global a
    a = 5
    b = 0

some_func() 
print(a)
print(b)

def tambah_procedure(a,b):
    result = a+b
    print(result)
    
def tambah_fungsi(a,b):
    result = a+b
    return result

tambah_procedure(1,2)
tambah_fungsi(1,2)

# recursion
# factorial of a number
# n! = n * (n - 1)
def factorial(n):
    if n == 1:
        return n
    else:
        result = n * (factorial(n-1))
        return result

test_factorial = factorial(3)
print(test_factorial)

# First Class function
# 1. instance
def tambah(a,b):
    result = a+b
    return result
test_instance = tambah
print(type(test_instance(1,2)))
test_instance2 = tambah(1,2)
print(type(test_instance2))

# 2. return func from a function
def sum_func():
    def tambah(a,b):
        result = a+b
        return result
    return tambah
test_return = sum_func()
print(test_return(1,3))

# 3. parameter as another func
def tambah_in_param(a,b):
        result = a+b
        return result
def info():
    test = tambah_in_param(1,2)
    return " ini hasil tambah = {}".format(test)

test_param_func = info()
print(test_param_func)


#############################################
# Higher Order Function Built-in
# 1. map()
data = [1,2,3,4,5,6,7,8,9,10]
# squared each item in data
def squared(x):
    result = x**2
    return result

test_map = map(lambda x: x**2, data)
print(list(test_map))

# 2. filter()
data = [1,2,3,4,5,6,7,8,9,10]
def genap(x):
    return x % 2 == 0

test_filter= list(filter(lambda z: z%2 == 0, data))
print(test_filter)

# filter missing item
data = ["","abc","apple","","mango","grape",0, None]
test_data = list(filter(None, data))
print(test_data)

# reduce 
from functools import reduce
data = [1,2,3,4]
# val = 1 x 2
# val2 = val x 3
# val3 = val2 x 4
multiplier = lambda x,y : x*y
test_reduce = reduce(multiplier, data)
# 1. val1 = multiplier(data1,data2)
# 2. val2 = multiplier(val1, data3)
# 3. val3 = multiplier(val2, data4)
print(test_reduce)
##########################################################################################
## built-in function ngga cuma map filter reduce(module functools) ya
## masih banyak yang lain, sorted, any, all, sum, max, min. Bisa di eksplor.
##########################################################################################



# LAMBDA
def tambah_fungsi_2(a,b):
    result = a+b
    return result
# 1. 
test_lambda_1 = (lambda a : a*2)
print(test_lambda_1(2))
# 2.
test_lambda_2 = (lambda a,b : a*b)
print(test_lambda_2(2,10))
# 3.
x = 9
y = 10
test_lambda_3 = (lambda a,b : a*b)(x,y)
print(test_lambda_3)
