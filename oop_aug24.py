'''
OOP --> Class,Object,Methods (__init__())
Encapsulation -->Public,Protected,Private
Inheritance --> It is one of key feature of OOP where we inherit
the properties (attributes/methods) from one class to another
class (base class (Parent class) --> dervied class (Child Class))
Whatsapp -->Personal User,Business User (Catalog),Community Admin
Features -->Code Reusability,Avoiding Code Duplication,
Code Maintainability,Polymorphism (Method Overriding(super()),
Method Overloading,Operator Overloading __add__,__str__)

Types : Single Inheritance (Finger Print)
-->One child class inherting properties from one parent class only
Multiple Inheritance (Mother,Father -->Child) -->One child
class inheriting properties from two parent classes
Multilevel Inheritance (GrandParent -->Parent --> child)
level by level
Hierarchical Inheritance --> multiple child classes 
inheriting properties from single parent
Hybrid Inheritance -->It can carry one or more type of
inheritances
Syntax : 

Single Inheritance:

class baseclass:
    statement(s)..
    ......
class Derivedclass(baseclass):
    ........
    ......
'''
#Whatsapp Scenario -->Personal User,Business user
'''
class User:
    """Single Inheritance usage"""
    def send_message(self):
        print('Sending Message')
    def voice_call(self):
        print('Making Voice Calls')
    def video_call(self):
        print("making video calls")
class BusinessUser(User):
    #pass
    def create_catalog(self):
        print("Displaying Products Catalog")
u1 = BusinessUser()
print(dir(u1))
u1.send_message()
u1.video_call()
u1.voice_call()
u1.create_catalog() 

#Social Media Login --> users -->update_users
class Users:
    """Single Inheritance usage"""
    company = "Codegnan" #class attribute
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def full_name(self):
        return self.fname + self.lname
#u1 = Users("saketh","kallepu")
#print(u1.full_name())
#print(u1.company)
class Update_users(Users):
    def update_name(self):
        return self.fname.title()+" "+self.lname.title().strip()
u1 = Update_users("saketh"," kallepu")
print(u1.company)
print(u1.full_name())
print(u1.update_name())
u2 = Users("sai","tarigopula")
print(u2.full_name())
print(u2.company)

#What if we have constructor in child class also....
#Father --> Kid (Property)

class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'Father Property is {self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self):
        #self.property = 200000
        self.cash = 2000000
    def kid_property(self):
        print(f'Kid Property is {self.cash}')
obj = Kid()
obj.father_property()
obj.kid_property()
#in above case it is giving same value for Father also as 
#2 lakhs..when we gave property as same attribute in both classes
#Constructor Overriding -->super() usage
'''
#In above example we use super().__init__() 

class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'Father Property is {self.property}')
class Kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self):
        super().__init__() #calling superclass constructor
        self.cash = 200000
    def kid_property(self):
        print(f'Kid Property is {self.cash}')
        print(f'Kid Final Property is {self.cash + self.property}')
obj = Kid()
obj.father_property()
obj.kid_property()





