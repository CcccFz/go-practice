#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Implementation of the abstract factory pattern"""


class PetShop(object):

    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print 'We have a lovely %s' % pet
        print 'It says %s' % pet.speak()
        print 'we also have %s' % self.pet_factory.get_food()
        print '----------------------------------'

class Dog(object):
    def __str__(self):
        return 'Dog'

    def speak(self):
        return 'Wang!!! Wang!!!'

class Cat(object):
    def __str__(self):
        return 'Cat'

    def speak(self):
        return 'Miao~~ Miao~~'

class DogFactory(object):
    def get_pet(self):
        return Dog()

    def get_food(self):
        return 'dog food'

class CatFactory(object):
    def get_pet(self):
        return Cat()

    def get_food(self):
        return 'cat food'

def get_factory():
    import random
    return random.choice([CatFactory, DogFactory])()

if __name__ == '__main__':
    for i in range(4):
        shop = PetShop(get_factory())
        shop.show_pet()
