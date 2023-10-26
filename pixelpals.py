from datetime import datetime
from tkinter import *
import json



#    ###  #      ###  ####   ###  #      ###
#   #     #     #   # #   # #   # #     #
#   #  ## #     #   # ####  ##### #      ###
#   #   # #     #   # #   # #   # #         #
#    #### #####  ###  ####  #   # #####  ###
#
# Any global variables we need

# State object
state = None

# Global variable to store a reference to the current window object
currentWindow = None

# Constants
DATETIME_FORMAT = "%Y%m%d%H%M%S%f"
PET_TYPES = [
    "Cat",
    "Dog",
    "Fish",
    "Lizard",
    "Rock",
    "Plant"
]

# StringVars for Tkinter Entry objects
petName = None
petType = None



#   #   # ##### ### #     ### ##### #   #
#   #   #   #    #  #      #    #   #   #
#   #   #   #    #  #      #    #    # #
#   #   #   #    #  #      #    #     #
#    ###    #   ### ##### ###   #     #
#
# General purpose functions that will be used by other parts of the
# program.

def dateToText(date):
    """
    Convert a date to a string using the format specified by
    DATETIME_FORMAT.

    Args:
        date (datetime): the date to be converted

    Returns:
        string: the string
    """
    return date.strftime(DATETIME_FORMAT)

def textToDate(text):
    """
    Parse a date from a string using the format specified
    by DATETIME_FORMAT.

    Args:
        text (string): the string to be parsed

    Returns:
        datetime: parsed date
    """
    return datetime.strptime(text, DATETIME_FORMAT)

def newWindow():
    """
    Check if a window object is currently being stored in the "currentWindow" global,
    and if there is, close it. After that, use Tkinter to create a new window
    object, store it in the global variable, and return a reference to it.

    Returns:
        window object: the new window that has been created
    """
    global currentWindow
    # Check if there is currently a window that needs to be closed
    if currentWindow is not None:
        currentWindow.quit()
        currentWindow.destroy()
    # Create and return a new window
    currentWindow = Tk()
    return currentWindow



#   #      ###   ###  ###  ###
#   #     #   # #      #  #   #
#   #     #   # #  ##  #  #
#   #     #   # #   #  #  #   #
#   #####  ###   #### ###  ###
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
        # TODO: save a snapshot of pet stats each hour or so

def readStateFromSaveFile():
    """
    Read the save file if there is one, and put the data in the global state
    variable. Certain values will be converted to a form more useable by the
    rest of the program. This function is designed be be run at the start of
    the program.

    Returns:
        boolean: true if save file successfully read
    """
    # Read data from the file, return False upon failure
    try:
        file = open("pixelpalsave.json")
        global state
        state = json.load()
        file.close();
    except:
        return False
    # Instantiate a pet object
    # TODO
    # Convert dates to datetime objects
    state.initial_date = textToDate(state.initial_date)
    state.save_date = textToDate(state.save_date)
    # Since there was a save file, return True
    return True

def saveStateToFile():
    """
    Save the current state to a save file. The current state can be found
    in the global state variable. Certain values will be converted into a
    format more JSON friendly. This function is designed be be run
    multiple times throughout the execution of the program.
    """
    # Create a data object that will be converted to JSON
    saveData = {}
    # Store some of the simpler objects
    saveData.initial_date = dateToText(state.initial_date)
    saveData.save_date = datetime.now()
    saveData.money = state.money
    # Make a simpler copy of the pet object
    saveData.pet = None # TODO
    # Store the statistics
    saveData.pet_stats = state.pet_stats
    # Save the save data to a file
    file = open("pixelpalsave.json", "w")
    json.dump(saveData, file)
    file.close()

def endProgram():
    """
    Complete the necessary steps to end the program. Write to the save file,
    and close the current window.
    """
    # Write the current state to the save file
    if state is not None:
        saveStateToFile()
    # Close the current window
    currentWindow.quit()
    currentWindow.destroy()

def createNewPet():
    """
    Called by pet adoption window when the submit button is clicked. Validate the
    inputs entered in the adopion window, and if there are no problems, create a
    new pet object, reset the current state object, and write to the save file.
    Finish by switching to the pet care window.
    """
    # Get input from adoption window
    # TODO
    # Validate input
    # TODO
    # Instantiate a new pet object
    # TODO
    # Create a new state object
    # TODO
    # Write to the save file
    # TODO
    # Switch to pet care window
    showPetCareWindow()



#    ###  #   # ###
#   #     #   #  #
#   # ### #   #  #
#   #   # #   #  #
#    ####  ###  ###
#
# Functions that build the GUI, and setup event handlers

def showMenuWindow():
    """
    Display the main menu window, and set up event handlers for the buttons.
    """
    # Create a new window
    window = newWindow()
    window.title("Pixel Pals")
    # Create a new pet button
    btnNewPet = Button(window, text="New Pet", command=showAdoptionWindow)
    btnNewPet.grid(row=0, column=0)
    if state is not None:
        btnNewPet["state"] = "disabled"
    # Create a pet care button
    btnPetCare = Button(window, text="Take Care of Pet", command=showPetCareWindow)
    btnPetCare.grid(row=1, column=0)
    if state is None:
        btnPetCare["state"] = "disabled"
    # Create a go somewhere button
    btnGoSomewhere = Button(window, text="Go Somewhere", command=showLocationWindow)
    btnGoSomewhere.grid(row=2, column=0)
    if state is None:
        btnGoSomewhere["state"] = "disabled"
    # Create a give up button
    btnGiveUp = Button(window, text="Give Up", command=showGiveUpWindow)
    btnGiveUp.grid(row=3, column=0)
    if state is None:
        btnGiveUp["state"] = "disabled"
    # Start the window
    window.mainloop()

def showAdoptionWindow():
    """
    Display the pet adoption window. This window is used to create a new pet.
    """
    # Create a new window
    window = newWindow()
    window.title("New Pet")
    # Create a field to enter the pet's name
    global petName
    petName = StringVar()
    entPetName = Entry(window, width=15, textvariable=petName)
    entPetName.grid(row=0, column=0)
    # Create a drop down list to select the pet type
    global petType
    petType = StringVar()
    optPetType = OptionMenu(window, petType, *PET_TYPES)
    optPetType.grid(row=1, column=0)
    # Create a cancel button
    btnCancel = Button(window, text="Cancel", command=showMenuWindow)
    btnCancel.grid(row=2, column=0)
    # Create a submit button
    btnCreatePet = Button(window, text="Create Pet", command=createNewPet)
    btnCreatePet.grid(row=3, column=0)
    # Start the window
    window.mainloop()

def showPetCareWindow():
    pass

def showLocationWindow():
    pass

def showOutcomeWindow():
    pass

def showGiveUpWindow():
    pass

def showRandomEventWindow():
    pass

def showDeathScreenWindow():
    pass

def showStatsWindow():
    pass



#   ### #   # ### #####
#    #  ##  #  #    #
#    #  # # #  #    #
#    #  #  ##  #    #
#   ### #   # ###   #
#
# Get everything running

showMenuWindow()
