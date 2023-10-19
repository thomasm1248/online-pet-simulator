
# Util functions
#
# General purpose functions that will be used by other parts of the
# program.

# Program logic
#
# Functions that handle the logic of the program.

# Apply time to pet by calling the pet's tick method once per
# minute of time.
def simulateEffectOfTimeOnPet(pet, time):
    """
    Apply time to pet by calling the pet's tick method once per
    minute of time that has passed.

    Args:
        pet (pet object): the pet
        time (int): the minutes
    """
    for i in range(time):
        pet.tick()

# Event handlers
#
# Functions that will be called when GUI events take place.
