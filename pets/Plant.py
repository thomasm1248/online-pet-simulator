from .Pet import Pet
import random
       
class Plant(Pet):
    TYPE = "plant"
        
    def update(self, time):
        super().update(time)
    
    