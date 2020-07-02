# Pengenalan Class

class Kalkulator:

    # static method cuman bisa dipake oleh class
    def name(arg):
        print("Ini Adalah Kalkulator", arg)
    
    # decoration staticmethod bisa dipakai class & object
    @staticmethod
    def tambah():
        print("a + b =")

    # object method
    def user(self, name):
        print("user kalkulator", name)

print("\n")
Kalkulator.name("Budi\n")
Kalkulator.tambah()

var1 = Kalkulator() #instatiation object 1
var1.tambah() # @staticmethod
var1.user("amin")

var2 = Kalkulator() #instatiation object 2
var2.user("muklis")


