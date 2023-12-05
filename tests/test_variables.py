import datetime
from pets import *

day_datetime_str = '09/19/22 13:55:26'
day_datetime_object = datetime.datetime.strptime(day_datetime_str, '%m/%d/%y %H:%M:%S')

night_datetime_str = '09/19/22 21:55:26'
night_datetime_object = datetime.datetime.strptime(night_datetime_str, '%m/%d/%y %H:%M:%S')

test_picture_path = 'test_image.jpg'

test_dog     = lambda: Dog.adopt("test",0,day_datetime_object,test_picture_path)
test_cat     = lambda: Cat.adopt("test",0,day_datetime_object,test_picture_path)
test_fish    = lambda: Fish.adopt("test",0,day_datetime_object,test_picture_path)
test_lizzard = lambda: Lizzard.adopt("test",0,day_datetime_object,test_picture_path)
test_rock    = lambda: Rock.adopt("test",0,day_datetime_object,test_picture_path)
test_plant   = lambda: Plant.adopt("test",0,day_datetime_object,test_picture_path)