from .Pet import Pet
import random
       
class Plant(Pet):
    TYPE = "plant"
        
    def update(self, time):
        # check if its night time
        is_night = not (6 <= time.hour <= 19)
        
        # if it's night, consume nutrients
        if is_night:
            super().update(time)
        
        # if it's day, produce nutrients (increase hunger as opposed to decrease it)
        else: 
            hunger_0 = self.get_stat("hunger")
            super().update(time)
            hunger_1 = self.get_stat("hunger")
            
            # get the automated hunger depletion
            delta_hunger =  hunger_1 - hunger_0
             
            # make the decrement an increment
            self.regulate_stat("hunger", -1.5 * delta_hunger)
            
    
    