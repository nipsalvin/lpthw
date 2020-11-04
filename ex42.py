##Animal is-a object
class Animal(object):
    pass

##class named Dog that is-a animal
class Dog(Animal):
    #classs Dog has-a __init__ and takes self and name parameteres
     def __init__(self,name):
         ##Dog has-a name
        self.name = name

##class named Cat that is-a animal
class Cat(Animal):

    def __init__(self,name):
        ##cat has-a name
        self.name = name

##class Person is-a object
class Person(object):

    def __init__(self,name):
        ##person has-a name
        self.name = name
##Person has-a pet of some kind
        self.pet = None


##class Employee is-a object
class Employee(Person):

    def __init__(self, name, salary):
        ##?? what strange magic is this
        super(Employee, self).__init__(name)
        ##??
        self.salary = salary

##class fish is-a object
class Fish(object):
    pass

##class salmon is-a fish
class Salmon(Fish):
    pass

##class halibut is-a fish
class Halibut(Fish):
    pass


##rover is-a Dog
rover = Dog("Rover")

##satan is-a cat
satan = Cat("Satan")

##mary is-a person
mary = Person("Mary")

##?mary has-a pet
mary.pet = satan

##frank is-a employee
frank = Employee("Frank", 120000)

##frank has-a pet
frank.pet = rover

##flipper is-a fish
flipper = Fish

##crouse is-a Salmon
crouse = Salmon

##harry is-a halibut
harry = Halibut