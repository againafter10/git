#### inheritance python
### In Python, method overloading is not possible,the defaliut parameters allows you to do that here
# if you really want access the same function with different features you  use method overriding.

class Person:
    
    def __init__(self,name=None,gender=None):
        self.name=name
        self.gender=gender
    
    def GetPerson(self):
        return self.name , self.gender
    
    def Getmoredetails(self,age):
        return "extra details of age %s" %age

        
        
class Nationality(Person):
    
    def __init__(self,first,gender,origin=None):
        Person.__init__(self,first,gender)
        self.origin = origin
        
    def GetNationality(self):
        return self.GetPerson() , self.origin
    
    def Getmoredetails(self,age=None,weight=None):
        return "extra details of age and weight are  %s and %s " %(age,weight)
    

x = Person("Marge", "Female")
y = Nationality("Homer", "Simpson", "India")

print(x.GetPerson())
print
print(y.GetNationality())
print
print(x.Getmoredetails(23))
print
print(y.Getmoredetails(23,98))

#############################
