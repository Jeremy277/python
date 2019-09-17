#定义Dog类 跑 叫 吃
#定义Bird类 飞 叫 吃

class Animal:
    def shout(self):
        print('shout')
    def eat(self):
        print('eat')

class Dog(Animal):
    def run(self):
        print('run')
class Bird(Animal):
    def fly(self):
        print('fly')

animal =Animal()
dog = Dog()
bird = Bird()
print(isinstance(bird,Animal))#True
print(isinstance(animal,Bird))#False
print(issubclass(Animal,Bird))#False
print(issubclass(Dog,Animal))#True

print(type(dog) == Dog)#True
print(type(dog) == Animal)#False