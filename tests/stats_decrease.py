import unittest
from pets import *
import datetime
from .test_variables import *

class TestStatsDecrease(unittest.TestCase):

    def test_decrease_dog_day(self):
        dog = test_dog()
        
        stats_pre_update = dog.current_stats().values()
        
        dog.update(day_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = dog.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")

    def test_decrease_dog_night(self):
        dog = test_dog()
        
        stats_pre_update = dog.current_stats().values()
        
        dog.update(night_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = dog.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")
    
    def test_decrease_cat_day(self):
        cat = test_cat()
        
        stats_pre_update = cat.current_stats().values()
        
        cat.update(day_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = cat.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")

    def test_decrease_cat_night(self):
        cat = test_cat()
        
        stats_pre_update = cat.current_stats().values()
        
        cat.update(night_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = cat.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")
            
    def test_decrease_fish_day(self):
        fish = test_fish()
        
        stats_pre_update = fish.current_stats().values()
        
        fish.update(day_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = fish.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")

    def test_decrease_fish_night(self):
        fish = test_fish()
        
        stats_pre_update = fish.current_stats().values()
        
        fish.update(night_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = fish.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")
    def test_decrease_lizzard_day(self):
        lizzard = test_lizzard()
        
        stats_pre_update = lizzard.current_stats().values()
        
        lizzard.update(day_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = lizzard.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")

    def test_decrease_lizzard_night(self):
        lizzard = test_lizzard()
        
        stats_pre_update = lizzard.current_stats().values()
        
        lizzard.update(night_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = lizzard.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")
            
    def test_decrease_rock_day(self):
        rock = test_rock()
        
        stats_pre_update = rock.current_stats().values()
        
        rock.update(day_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = rock.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")

    def test_decrease_rock_night(self):
        rock = test_rock()
        
        stats_pre_update = rock.current_stats().values()
        
        rock.update(night_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = rock.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")
            
    def test_decrease_plant_day(self):
        plant = test_plant()
        
        stats_pre_update = plant.current_stats().values()
        
        plant.update(day_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = plant.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            if plant.STATS[i] == 'hygiene' or plant.STATS[i] == 'hunger': 
                continue
            
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")

    def test_decrease_plant_night(self):
        plant = test_plant()
        
        stats_pre_update = plant.current_stats().values()
        
        plant.update(night_datetime_object + datetime.timedelta(0, 60))
        
        stats_post_update = plant.current_stats().values()
        
        for i, (pre, post) in enumerate(zip(stats_pre_update, stats_post_update)):
            if plant.STATS[i] == 'hygiene': 
                continue
            self.assertEqual(pre > post, True, f"stat#{i}: {pre} should be greater than {post}.")