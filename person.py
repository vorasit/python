class person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    '''
    def myfunction(self):
        print("ok boy")
    '''
    def myfunction(abc):
        print("name :"+abc.name)
    
    def printname(self):
        print(self.name,self.age)

p1 = person("pin",25)
print("name : "+str(p1.name))
print("age : "+str(p1.age))
p1.myfunction()

class student(person): 
    def __init__(self,name,age,brithday):
        super().__init__(name,age) # all method parent
        self.birthday = brithday # add properties
    def present(self):
        print("Hello "+self.name)
        
'''error
    def printbirthday(self):
        print("brithday : "+ self.brithday)
'''
s1 = student("parn",21,1996)
s1.myfunction()
s1.printname()
print(s1.birthday)

class acer(student):
    def __init__(self,name,age,brithday,school):
        super().__init__(name,age,brithday)
        self.school = school

a1 = acer("pinzaa007",24,1996,"kmutnb")
a1.myfunction()
a1.printname()
print(a1.birthday)
print("school : "+a1.school)
a1.present()