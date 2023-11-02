from .Pet import Pet
import random
       
class Fish(Pet):
    TYPE = "fish"
        
    def update(self, time):
        super().update(time)
    
    