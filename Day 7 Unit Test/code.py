class Kalkulator:
    @staticmethod
    def tambah_assert(a,b):
        assert a+b == 2, "harusnya 3"
    
    @staticmethod
    def tambah(a,b):
        return a+b
    
    @staticmethod
    def kuadrat(a):
        if type(a) is not int :
            raise TypeError
        # return type(a)
        if a < 0:
            raise ValueError("tidak boleh negatif")
        else:
            return a**2

if __name__ == "__main__":
    test = Kalkulator.tambah(1,2)
    print("result oke")
    test = Kalkulator.kuadrat(2)
    print(test)