# Error Handling
# try except block 

# 1. 
# try:
#     num = int(input("masukkan nomer = "))
# except:
#     print("harus angka")

#2.
# try:
#     num = int(input("masukkan nomer = "))
# except Exception as error:
#     print(error)

#3.
try:
    num1 = int(input("masukkan nomer 1 = "))
    num2 = int(input("masukkan nomer 2 = "))
    hasil = num1/num2
except ValueError:
    print("inputan harus angka")
except ZeroDivisionError:
    print("angka tidak boleh 0")

# print(hasil)
