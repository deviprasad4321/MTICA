class Dog:
    price=400
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def bark(self):
        print('woof')
        print(self.name,'has',self.price,'price and its colour is',self.color)
if __name__=="__main__":
    pet1=Dog("Tommy","Brown")
    pet2=Dog("Sheru","White")
    pet1.bark()
    pet2.bark()
    print(pet1.price)
    print(pet2.price)
##    print(pet1)#object
##    print(pet2)#object
    print(Dog.price)
    Dog('abc','Blue').bark()
    
    
