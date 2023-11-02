from pets import Pet

# event functions can be whatever
# they can take different fill/depletion levels for each stat
# this is just an example
# feed fills hunger, depletes thirst.
def feed(pet: Pet, feed_level):
    pet.regulate_stat("hunger", feed_level)
    pet.regulate_stat("health", feed_level / 10)
    pet.regulate_stat("hydration", -feed_level/4)
    pet.regulate_stat("hygiene", -feed_level/4)
    
    pet.add_cost(10)

# play fills love, depletes hunger. 
def play(pet: Pet, play_level):
    pet.regulate_stat("love", play_level)
    pet.regulate_stat("health", play_level / 10)
    pet.regulate_stat("hunger", -play_level/5)
    pet.regulate_stat("hygiene", -play_level/5)
    
    pet.add_cost(1)
    
def hydrate(pet: Pet, hydration_level):
    pet.regulate_stat("hydration", hydration_level)
    pet.regulate_stat("health", hydration_level / 10)
    pet.regulate_stat("hygiene", -hydration_level/4)
    
    pet.add_cost(1)
    
def clean(pet: Pet, clean_level):
    pet.regulate_stat("hygiene", clean_level)
    pet.regulate_stat("love", -clean_level/3)
    
    pet.add_cost(20)
    
def medicate(pet: Pet, medicine_level):
    pet.regulate_stat("health", medicine_level)
    pet.regulate_stat("love", -medicine_level/2)
    
    pet.add_cost(200)