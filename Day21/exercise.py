# class Person:
#   pass
# print(Person)

# p = Person()
# print(p)

# class Person:
#       def __init__ (self, name):
#         # self allows to attach parameter to the class
#           self.name =name

# p = Person('Manish')
# print(p.name)
# print(p)

# class Person:
#     def __init__(self, firstname, lastname, age, country, city):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
#         self.city = city
#     def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


# p = Person('Manish', 'Kumar', 250, 'India', 'Motihari')
# # print(p.firstname)
# # print(p.lastname)
# # print(p.age)
# # print(p.country)
# # print(p.city)
# print(p.person_info())


# class Person:
#       def __init__(self, firstname='Manish', lastname='Kumar', age=250, country='India', city='Motihari'):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city

#       def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

# p1 = Person()
# print(p1.person_info())
# p2 = Person('Abhishek', 'Kasera', 30, 'Allahabad', 'Uttar Pradesh')
# print(p2.person_info())

class Person:
      def __init__(self, firstname='Manish', lastname='Kumar', age=250, country='India', city='Motihari'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
# print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('Abhishek', 'Kasera', 30, 'Allahabad', 'Uttar Pradesh')
# print(p2.person_info())
# print(p1.skills)
# print(p2.skills)


class Student(Person):
    pass


s1 = Student('Mohan', 'Goyel', 30, 'Iceland', 'Sitaie')
s2 = Student('Ramu', 'Teja', 28, 'US', 'Espoo')
# print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
# print(s1.skills)

# print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
# print(s2.skills)

'''
We did not call the init() constructor in the child class. If we didn't call it then we can still access all the properties from the parent. But if we do call the constructor we can access the parent properties by calling super.
We can add a new method to the child or we can override the parent class methods by creating the same method name in the child class. When we add the init() function, the child class will no longer inherit the parent's init() function.
'''

class Student(Person):
    def __init__ (self, firstname='Manish', lastname='Kumar',age=250, country='India', city='Motihari', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Mohan', 'Goyel', 30, 'Iceland', 'Sitaie', 'male')
s2 = Student('Ramu', 'Teja', 28, 'US', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
