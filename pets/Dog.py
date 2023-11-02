from .Pet import Pet
import random
       
class Dog(Pet):
    TYPE = "dog"
        
    def update(self, time):
        super().update(time)
    
    