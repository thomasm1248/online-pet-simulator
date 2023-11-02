from .Pet import Pet
import random

class Rock(Pet):
    TYPE = "rock"
        
    def update(self, time):
        super().update(time)
        
        # random crack
        
class Cat(Pet):
    TYPE = "cat"
        
    def update(self, time):
        super().update(time)
    
    