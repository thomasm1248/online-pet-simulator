import unittest
from pets import *
import datetime
from .test_variables import *

class TestDeath(unittest.TestCase):
    
    def test_death_regulate_dog(self):
        dog = test_dog()
        
        with self.assertRaises(PassedAway):
            dog.regulate_stat('health', -3000)
            
    def test_death_neglect_dog(self):
        dog = test_dog()
        
        with self.assertRaises(PassedAway):
            for _ in range(10000000):
                dog.update(night_datetime_object)
                
    def test_death_regulate_cat(self):
        cat = test_cat()
        
        with self.assertRaises(PassedAway):
            cat.regulate_stat('health', -3000)
            
    def test_death_neglect_cat(self):
        cat = test_cat()
        
        with self.assertRaises(PassedAway):
            for _ in range(10000000):
                cat.update(night_datetime_object)
    def test_death_regulate_fish(self):
        fish = test_fish()
        
        with self.assertRaises(PassedAway):
            fish.regulate_stat('health', -3000)
            
    def test_death_neglect_fish(self):
        fish = test_fish()
        
        with self.assertRaises(PassedAway):
            for _ in range(10000000):
                fish.update(night_datetime_object)
    def test_death_regulate_lizzard(self):
        lizzard = test_lizzard()
        
        with self.assertRaises(PassedAway):
            lizzard.regulate_stat('health', -3000)
            
    def test_death_neglect_lizzard(self):
        lizzard = test_lizzard()
        
        with self.assertRaises(PassedAway):
            for _ in range(10000000):
                lizzard.update(night_datetime_object)
    def test_death_regulate_rock(self):
        rock = test_rock()
        
        with self.assertRaises(PassedAway):
            rock.regulate_stat('health', -3000)
            
    def test_death_neglect_rock(self):
        rock = test_rock()
        
        with self.assertRaises(PassedAway):
            for _ in range(10000000):
                rock.update(night_datetime_object)
    def test_death_regulate_plant(self):
        plant = test_plant()
        
        with self.assertRaises(PassedAway):
            plant.regulate_stat('health', -3000)
            
    def test_death_neglect_plant(self):
        plant = test_plant()
        
        with self.assertRaises(PassedAway):
            for _ in range(10000000):
                plant.update(night_datetime_object)