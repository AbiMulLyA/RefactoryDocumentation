class Hash:
    def __init__(self, string, code):
        self.__string = string
        self.code = code
    
    @property
    def info(self):
        # return self.info
        return 'string "{}" and code "{}"'.format(self.__string, self.code)
    
    @property
    def string(self):
        return self.__string
    
    @string.setter
    def string(self, newString):
        self.__string = newString
    
    @string.deleter
    def string(self):
        del self.__string
    
    def md5(self):
        print("md5 : {}".format(self.__string))
    
    def sha1(self):
        print("sha1 : {}".format(self.__string))
    
    def sha256(self):
        print("sha256 : {}".format(self.__string))
    
    def sha512(self):
        print("sha512 : {}".format(self.__string))
        

# 1. instantiation test to Hash class
test = Hash("secret","123")
print(test.__dict__)
# 2. print info variabel that accessed to string private variabel
test.code = "0909"
print(test.info)
print(test.__dict__)
# 3. get value variabel string
print(test.string)
print(test.__dict__)
# 4. set value variabel string
test.string = "amin"
print(test.string)
print(test.__dict__)
# 5. del variabel string
del test.string
print(test.__dict__)