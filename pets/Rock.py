from .Pet import Pet
import random

class Rock(Pet):
    TYPE = "rock"
        
    def update(self, time):
        super().update(time)
        
        # random crack
    