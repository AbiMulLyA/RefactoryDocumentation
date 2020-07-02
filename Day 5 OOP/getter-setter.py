class GroupCompany:

    # class variable
    __jumlah = 0

    def __init__(self, name ="", address = ""):
        # instance variable
        self.__name = name
        self.address = address
        self.__phone = "809080"
        # GroupCompany.jumlah += 1

    # getter
    def getName(self):
        return self.__name
    
    # getter
    def getPhone(self):
        return self.__phone

    # setter
    def setPhone(self, new_phone):
        self.__phone = new_phone
        return self.__phone

    def setName(self, new_name):
        self.__name = new_name
        return self.__name

    def profile(self):
        print(GroupCompany.__jumlah)
        return "Nama : {}, {}".format(self.__name, self.address)

obj1 = GroupCompany(name = "MDD", address= "Jakarta")
obj2 = GroupCompany(name = "Refactory")

test = obj1.profile()
# print(test)
# print(obj1.__dir__)
# print(obj2.__dict__)
# print(GroupCompany.__dict__)

# print(obj1.getName())
# print(obj1.getPhone())

print(obj1.setName("New MDD"))
print(obj1.setPhone(""))

