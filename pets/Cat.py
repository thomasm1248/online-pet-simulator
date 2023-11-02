from .Pet import Pet
import random
       
class Cat(Pet):
    TYPE = "cat"
        
    def update(self, time):
        super().update(time)
    
    