from datetime import datetime

# Util functions
#
# General purpose functions that will be used by other parts of the
# program.

# Program logic
#
# Functions that handle the logic of the program.

def simulateEffectOfTimeOnPet(pet, startTime, endTime):
    """
    Apply time to pet by calling the pet's tick method once per
    minute from the start time to the end time.

    Args:
        pet (pet object): the pet
        startTime (datetime): the start time
        endTime (datetime): the end time
    """
    # Find the number of minutes between the two times
    difference = endTime - startTime
    minutes = difference.days * 24 * 60 + difference.seconds // 60
    # Call the pet's tick method once for each minute
    for i in range(minutes):
        pet.tick()

# Event handlers
#
# Functions that will be called when GUI events take place.
