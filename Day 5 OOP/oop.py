class GroupCompany:
    jumlah = 0

    def __init__(self, name ="", address = ""):
        # instance variable
        self.__name = name
        self.address = address
        self.__phone = "809080"
        GroupCompany.jumlah += 1

    # property getter setter 
    @property
    def name(self):
        pass
    
    @name.getter
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name*new_name
        return self.__name

    def profileCompany(self):
        # print(GroupCompany.__jumlah)
        print("Nama : {}, {}".format(self.__name, self.address))

    def contact(self):
        print("ini contact company {}".format(self.__phone))
    
    def testCompany(self, var):
        print("coba ngeprint var = {}".format(var))

class Employee(GroupCompany):
    def __init__(self, name, address):
        self.name_employee = name
        super().__init__(name,address)
    
    def welcome(self):
        return "Welcome, {}".format(self.name_employee)

    def getCompanyContact(self):
        GroupCompany.contact(self)
    
    def getTestCompany(self, var):
        GroupCompany.testCompany(self, var)

    def test_without_super(self):
        GroupCompany.profileCompany(self)
    
    def test_with_super(self):
        super().profileCompany()

susi = Employee("Susi Pujiastuti","Jalan Di Hati")
mirna = Employee("Mirna","Jalan Pantura")

# print class variable
jumlahObject = mirna.jumlah
print(jumlahObject)

# accessed method from GroupCompany class
mirna.getCompanyContact()

# accessed method from GroupCompany class with parsing parameter
mirna.getTestCompany("test var")

# super() in inheritance
mirna.test_without_super()
mirna.test_with_super()