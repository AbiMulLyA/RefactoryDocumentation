# print("module matematika")
pi = 3.14

def equal(a,b):
    hasil = a == b
    print("{} == {} {}".format(a,b,hasil))

def notequal(a,b):
    hasil = a != b
    print("{} != {} {}".format(a,b,hasil))

def greater(a,b):
    hasil = a > b
    print("{} > {} = {}".format(a,b,hasil))

def lesser(a,b):
    hasil = a < b
    print("{} < {} = {}".format(a,b,hasil))

# Ketika kita ngeprint __name__ di dalam :
####### module, output = __main__
####### file yang mengimport, output = comparison
print(__name__)