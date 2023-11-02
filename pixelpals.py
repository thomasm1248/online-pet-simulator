from datetime import datetime
from tkinter import *
from tkinter import filedialog
import json
import time
import threading
from pets import *
from pprint import pprint



#    ###  #      ###  ####   ###  #      ###
#   #     #     #   # #   # #   # #     #
#   #  ## #     #   # ####  ##### #      ###
#   #   # #     #   # #   # #   # #         #
#    #### #####  ###  ####  #   # #####  ###
#
# Any global variables we need

# Flag that indicates that the program should keep running
# Will be used by the main loop and the endProgram function
keepRunning = True

# The pet object if there is one
pet = None

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

# A reference to the label on the adoption window that contains the filename
# of the image that will represent the pet
lblFilename = None

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
    Apply time to pet by calling the pet's update method once per
    minute from the start time to the end time.

    Args:
        pet (pet object): the pet
        startTime (datetime): the start time
        endTime (datetime): the end time
    """
    print("Similating pet since app last opened... ", end="")
    # Advance the time by one minute, ticking the pet's clock each minute
    try:
        currentTime = startTime
        while currentTime < endTime:
            currentTime += timedelta(0, 60) # advance 60 seconds
            pet.update(currentTime)
        print("Done.")
    except(PassedAway):
        print("Pet passed away while you were gone.")
        showDeathScreenWindow(currentTime)

def readStateFromSaveFile():
    """
    Attempt to read the pet from the save file. Return boolean indicating success.
    Uses Pet.deserialize to convert the JSON dictionary to a pet object, and
    converts the date strings to datetime objects.

    Returns:
        boolean: true if save file successfully read
    """
    # Read data from the file, return False upon failure
    global pet
    try:
        file = open("pixelpalsave.json")
        global pet
        pet = json.load(file)
        file.close()
        print("Pet data found.")
    except:
        print("No pet found.")
        return False
    # Convert dates to datetime objects
    pet['adoption_time'] = textToDate(pet['adoption_time'])
    pet['last_update'] = textToDate(pet['last_update'])
    # Instantiate a pet object
    pet = Pet.deserialize(pet)
    # Since there was a save file, return True
    return True

def saveStateToFile():
    """
    Convert the pet object to dictionary, convert the datetime objects to strings,
    then write the dict to the save file as JSON.
    """
    # Convert the pet object to a dict
    petDict = pet.serialize()
    # Convert datetime objects to strings
    petDict['adoption_time'] = dateToText(petDict['adoption_time'])
    petDict['last_update'] = dateToText(petDict['last_update'])
    # Save the save data to a file
    file = open("pixelpalsave.json", "w")
    json.dump(petDict, file)
    file.close()

def endProgram():
    """
    Complete the necessary steps to end the program. Write to the save file,
    and close the current window.
    """
    # Write the current state to the save file
    if pet is not None:
        saveStateToFile()
    # Close the current window if there is one
    try:
        currentWindow.quit()
        currentWindow.destroy()
    except:
        pass
    # Terminate the program
    global keepRunning
    keepRunning = False

def createNewPet():
    """
    Called by pet adoption window when the submit button is clicked. Validate the
    inputs entered in the adoption window, and if there are no problems, create a
    new pet object, and write to the save file. Finish by switching to the pet
    care window.
    """
    # Get input from adoption window
    name = petName.get()
    petTypeName = petType.get().lower()
    file = lblFilename["text"]
    # Validate input
    # TODO
    # Instantiate a new pet object
    global pet
    pet = Pet.adopt(name, 1000, datetime.now(), file, TYPE=petTypeName)
    # Write to the save file
    saveStateToFile()
    # Switch to pet care window
    showPetCareWindow()

def clockTick():
    """
    Tick the pet object if there is one, and update the state as needed. Automatically
    save the state to the save file. This function only needs to be called once at the
    start of the program, and it will keep ticking until the program closes.
    """
    # Debugging:
    print("tick")
    # Call the pet's tick method if the user has a pet
    if pet is not None:
        try:
            pet.update(datetime.now())
        except(PassedAway):
            showDeathScreenWindow(datetime.now())
    # Save the state to the save file
    # TODO

def feedPet():
    pass

def waterPet():
    pass

def cleanPet():
    pass

def playWithPet():
    pass

def takePetToVet():
    pass



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
    if pet is not None:
        btnNewPet["state"] = "disabled"
    # Create a pet care button
    btnPetCare = Button(window, text="Take Care of Pet", command=showPetCareWindow)
    btnPetCare.grid(row=1, column=0)
    if pet is None:
        btnPetCare["state"] = "disabled"
    # Create a go somewhere button
    btnGoSomewhere = Button(window, text="Go Somewhere", command=showLocationWindow)
    btnGoSomewhere.grid(row=2, column=0)
    if pet is None:
        btnGoSomewhere["state"] = "disabled"
    # Create a give up button
    btnGiveUp = Button(window, text="Give Up", command=showGiveUpWindow)
    btnGiveUp.grid(row=3, column=0)
    if pet is None:
        btnGiveUp["state"] = "disabled"
    # Create a quit button
    btnQuit = Button(window, text="Quit", command=endProgram)
    btnQuit.grid(row=4, column=0)

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
    # Create a button for selecting an image for the pet
    global lblFilename
    def browse():
        filename = filedialog.askopenfilename()
        lblFilename.config(text=filename)
    btnBrowse = Button(window, text="Browse", command=browse)
    btnBrowse.grid(row=2, column=0)
    lblFilename = Label(window)
    lblFilename.grid(row=2, column=1)
    # Create a cancel button
    btnCancel = Button(window, text="Cancel", command=showMenuWindow)
    btnCancel.grid(row=3, column=0)
    # Create a submit button
    btnCreatePet = Button(window, text="Create Pet", command=createNewPet)
    btnCreatePet.grid(row=4, column=0)

def showPetCareWindow():
    """
    Display the pet care window. This window is used to take care of the pet.
    """
    # Create a new window
    window = newWindow()
    window.title("Pet Care")
    # Create Play Button
    btnPlay = Button(window, text="Play", command=playWithPet)
    btnPlay.grid(row=0, column=0)
    # Create Feed Button
    btnFeed = Button(window, text="Feed", command=feedPet)
    btnFeed.grid(row=0, column=1)
    # Create Water Button
    btnWater = Button(window, text="Water", command=waterPet)
    btnWater.grid(row=0, column=2)
    # Create Bathe Button
    btnBathe = Button(window, text="Bathe", command=cleanPet)
    btnBathe.grid(row=0, column=3)
    # Create Go Somewhere Button
    btnGoSomewhere = Button(window, text="Go Somewhere", command=showLocationWindow)
    btnGoSomewhere.grid(row=0, column=4)

def showLocationWindow():
    """
    Display the location window. This window is used to go somewhere with your pet.
    """
    # Create a new window
    window = newWindow()
    window.title("Location")
    Lb = Listbox(window)
    Lb.insert(1, 'Dog Park')
    Lb.insert(2, 'Vet')
    Lb.insert(3, 'Walk')
    Lb.insert(4, 'Grandmas House')
    btnGo = Button(window, text="Lets Go!", command=lambda: showOutcomeWindow(Lb.get(Lb.curselection())))
    Lb.pack()
    btnGo.pack()

def showOutcomeWindow(location):
    """
    Display the outcome window. This window is used to display the outcome of going somewhere with your pet.
    """
    # Create a new window
    window = newWindow()
    window.title("Outcome")
    label1 = Label(text="You went to " + location)
    label1.pack()
    pass

def showGiveUpWindow():
    """
    Display the Give Up window. This window is used to give up on your pet.
    """
    # Create a new window
    window = newWindow()
    window.title("Give Up")
    # Create a label to ask the user if they want to give up on their pet
    lblGiveUp = Label(window, text="Would you like to give up on your pet?")
    lblGiveUp.grid(row=0, column=0)
    # Create a button for yes
    btnYes = Button(window, text="Yes") # Still need to add command
    btnYes.grid(row=1, column=0)
    # Create a button for no
    btnNo = Button(window, text="No") # Still need to add command
    btnNo.grid(row=1, column=1)

def showRandomEventWindow():
    """
    Display the random event window. This window is used to display a random event with your pet.
    """
    # Create a new window
    window = newWindow()
    window.title("Random Event")
    pass

def showDeathScreenWindow():
    """
    Display a window that lets the user know that their pet has died.
    """
    # Create a new window
    window = newWindow()
    window.title("Death")
    # Create a label to let the user know their pet has died
    lblInfo = Label(window, text="Your pet has died.")
    lblInfo.grid(row=0, column=0)
    # Create a button to switch to the stats window
    btnViewStats = Button(window, text="View Stats", command=showStatsWindow)
    btnViewStats.grid(row=1, column=0)

def showStatsWindow():
    pass



#   ### #   # ### #####
#    #  ##  #  #    #
#    #  # # #  #    #
#    #  #  ##  #    #
#   ### #   # ###   #
#
# Get everything running

# Set up the program - might open the death window
readStateFromSaveFile()
# Show the main menu window if no other window is shown
if currentWindow is None:
    showMenuWindow()
# Main loop
timeOfLastTick = time.time()
while keepRunning:
    time.sleep(0.01)
    # Update the window
    currentWindow.update_idletasks()
    currentWindow.update()
    # Make clock tick every minute
    if time.time() - timeOfLastTick >= 60:
        timeOfLastTick = time.time()
        clockTick()
    # Exit the program if the window was closed by the user
    try:
        currentWindow.winfo_exists() # throws an error if the window has been closed
    except:
        endProgram()
