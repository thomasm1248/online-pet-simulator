from datetime import datetime

#    ###  #      ###  ####   ###  #      ###
#   #     #     #   # #   # #   # #     #
#   #  ## #     #   # ####  ##### #      ###
#   #   # #     #   # #   # #   # #         #
#    #### #####  ###  ####  #   # #####  ###
#
# Any global variables we need

# The variable that will hold the pet object
pet = None

#  #   # ##### ### #     ### ##### #   #
#  #   #   #    #  #      #    #   #   #
#  #   #   #    #  #      #    #    # #
#  #   #   #    #  #      #    #     #
#   ###    #   ### ##### ###   #     #
#
# General purpose functions that will be used by other parts of the
# program.

def dateToText(date):
    """
    Convert a date to a string using the format: %Y%m%d%H%M%S%f

    Args:
        date (datetime): the date to be converted

    Returns:
        string: the string
    """
    return date.strftime("%Y%m%d%H%M%S%f")

def textToDate(text):
    """
    Parse a date from a string using the format: %Y%m%d%H%M%S%f

    Args:
        text (string): the string to be parsed

    Returns:
        datetime: parsed date
    """
    return datetime.strptime(text, "%Y%m%d%H%M%S%f")

#  #      ###   ###  ###  ###
#  #     #   # #      #  #   #
#  #     #   # #  ##  #  #
#  #     #   # #   #  #  #   #
#  #####  ###   #### ###  ###
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

#  ##### #   # ##### #   # #####  ###
#  #     #   # #     ##  #   #   #
#  ####  #   # ####  # # #   #    ###
#  #      # #  #     #  ##   #       #
#  #####   #   ##### #   #   #    ###
#
# Functions that will be called when GUI events take place.
