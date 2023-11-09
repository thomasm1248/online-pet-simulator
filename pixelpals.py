import os
from datetime import datetime, timedelta
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import json
import time
import threading
from pets import *
from pprint import pprint
import pet_events.some_events as PetEvents



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

# Instead of deleting the pet when it dies, move it here so that
# the stats window still has access to it
deadPet = None

# Global variable to store a reference to the current window object
currentWindow = None
currentWindowFrame = None

# Constants
DATETIME_FORMAT = "%Y%m%d%H%M%S%f"
PET_TYPES = [
    "Cat",
    "Dog",
    "Fish",
    "Lizzard",
    "Rock",
    "Plant"
]
SAVEFILE_FLOAT_PRECISION = 4

# A reference to the label on the adoption window that contains the filename
# of the image that will represent the pet
lblFilename = None

# A list of label objects if the petCare window is open. Each label object
# should show a percentage of the stat as a string
statLabels = None

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

def newWindow(title):
    """
    Check if a window object is currently being stored in the "currentWindow" global,
    and if there is, close it. After that, use Tkinter to create a new window
    object, store it in the global variable, and return a reference to it.

    Returns:
        window object: the new window that has been created
    """
    global currentWindow
    global currentWindowFrame
    # Check if there is currently a window with a frame that needs to be closed
    if currentWindow is not None:
        currentWindowFrame.destroy()
    # Create and return a new window if there isn't one
    if currentWindow is None:
        currentWindow = Tk()
    # Set the title of the window
    currentWindow.title(title)
    # Add a frame to the window
    currentWindowFrame = Frame(currentWindow)
    currentWindowFrame.pack()
    return currentWindowFrame

def round_floats(o):
    """
    Rounds all the floats in an object.

    Args:
        o (object): the object containing floats
    
    Returns:
        object: same object, but with rounded floats

    Source:
        https://til.simonwillison.net/python/json-floating-point
    """
    if isinstance(o, float):
        return round(o, SAVEFILE_FLOAT_PRECISION)
    if isinstance(o, dict):
        return {k: round_floats(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [round_floats(x) for x in o]
    return o



#   #      ###   ###  ###  ###
#   #     #   # #      #  #   #
#   #     #   # #  ##  #  #
#   #     #   # #   #  #  #   #
#   #####  ###   #### ###  ###
#
# Functions that handle the logic of the program.

def simulateEffectOfTimeOnPet():
    """
    Apply time to pet by calling the pet's update method once per
    minute from the time the pet was last updated to the current time.
    """
    print("Similating pet since app last opened... ", end="")
    # Advance the time by one minute, ticking the pet's clock each minute
    startTime = pet.last_update
    endTime = datetime.now()
    try:
        currentTime = startTime
        while currentTime < endTime:
            currentTime += timedelta(0, 60) # advance 60 seconds
            pet.update(currentTime)
        print("Done.")
    except PassedAway as ex:
        print("Pet passed away while you were gone.")
        petDied(currentTime, ex)

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
    json.dump(round_floats(petDict), file)
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

def updateStatLabels():
    """
    Update the labels on the pet care window to show the current state of the pet.
    Don't do anything unless the pet care window is currently being shown.
    """
    # Abort if the pet care window isn't being shown
    if currentWindow.title() != "Pet Care":
        return
    # Get the current state of the pet
    currentStats = pet.current_stats()
    # Update the labels
    for statName, value in currentStats.items():
        statLabels[statName].config(text=("%.0f%%" % (value * 100)))

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
            # Update pet
            pet.update(datetime.now())
            # Update pet status labels if the pet care window is being displayed
            updateStatLabels()
        except PassedAway as ex:
            petDied(datetime.now(), ex)
        # Save the state to the save file
        saveStateToFile()

def petDied(time, message):
    """
    Called whenever the pet dies. Delete the save file, and switch to the death screen.
    
    Args:
        time (datetime): time the pet died
        message (string): a message to show the user
    """
    # Kill the pet
    global deadPet
    global pet
    deadPet = pet
    pet = None
    # Delete save file
    os.remove("pixelpalsave.json")
    # Switch to death screen
    showDeathScreenWindow(time, message)

def giveUpOnPet():
    """
    Called by the giveUpOnPet window when the user confirms that they want to give
    up on their pet. Make the pet die.
    """
    petDied(datetime.now(), "You gave up on %s." % pet.name)

def feedPet():
    """
    Called by the feed button on the pet care window.
    """
    PetEvents.feed(pet, 1.0)
    updateStatLabels()

def waterPet():
    """
    Called by the water button on the pet care window.
    """
    PetEvents.hydrate(pet, 1.0)
    updateStatLabels()

def cleanPet():
    """
    Called by the clean button on the pet care window.
    """
    PetEvents.clean(pet, 1.0)
    updateStatLabels()

def playWithPet():
    """
    Called by the play button on the pet care window.
    """
    PetEvents.play(pet, 1.0)
    updateStatLabels()

def takePetToVet():
    """
    """
    PetEvents.medicate(pet, 1.0)
    updateStatLabels()



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
    window = newWindow("Pixel Pals")
    # Create Title label
    lblTitle = Label(window, text="Pixel Pals")
    lblTitle.grid(row=0, column=0)
    lblTitle.config(font=("Courier", 44))
    # Create a new pet button
    btnNewPet = Button(window, text="New Pet", command=showAdoptionWindow)
    btnNewPet.grid(row=1, column=0)
    if pet is not None:
        btnNewPet["state"] = "disabled"
    # Create a pet care button
    btnPetCare = Button(window, text="Take Care of Pet", command=showPetCareWindow)
    btnPetCare.grid(row=2, column=0)
    if pet is None:
        btnPetCare["state"] = "disabled"
    # Create a go somewhere button
    btnGoSomewhere = Button(window, text="Go Somewhere", command=showLocationWindow)
    btnGoSomewhere.grid(row=3, column=0)
    if pet is None:
        btnGoSomewhere["state"] = "disabled"
    # Create a give up button
    btnGiveUp = Button(window, text="Give Up", command=showGiveUpWindow)
    btnGiveUp.grid(row=4, column=0)
    if pet is None:
        btnGiveUp["state"] = "disabled"
    # Create a quit button
    btnQuit = Button(window, text="Quit", command=endProgram)
    btnQuit.grid(row=5, column=0)

def showAdoptionWindow():
    """
    Display the pet adoption window. This window is used to create a new pet.
    """
    # Create a new window
    window = newWindow("New Pet")
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
    window = newWindow("Pet Care")
    # Create pet name label
    lblPetName = Label(window, text=pet.name)
    lblPetName.grid(row=0, column=0, columnspan=3)
    lblPetName.config(font=("Ariel", 20))
    # Display the image of the pet if there is one
    try:
        img = Image.open(pet.picture_path)
        width, height = img.size
        img = img.resize((300,round(300*height/width)))
        img = ImageTk.PhotoImage(img)
        lblPetPicture = Label(window, image=img)
        lblPetPicture.image = img
        lblPetPicture.grid(row=1, column=0, columnspan=3)
    except:
        lblNoPicture = Label(window, text="No Image Found")
        lblNoPicture.grid(row=1, column=0, columnspan=3)
    # Create pet status labels
    global statLabels
    statLabels = {}
    row = 2
    for statName in Pet.STATS:
        # Create label for the name of the stat
        lblStatName = Label(window, text=(statName.title() + ": "))
        lblStatName.grid(row=row, column=0, sticky=E)
        # Create label for the percentage of the stat
        lblStatPercent = Label(window)
        lblStatPercent.grid(row=row, column=1, sticky=E)
        # Add stat percent label to global 
        statLabels[statName] = lblStatPercent
        # Move to next row
        row += 1
    updateStatLabels()
    # Create Play Button
    btnPlay = Button(window, text="Play", command=playWithPet)
    btnPlay.grid(row=4, column=2, sticky=W)
    # Create Feed Button
    btnFeed = Button(window, text="Feed", command=feedPet)
    btnFeed.grid(row=2, column=2, sticky=W)
    # Create Water Button
    btnWater = Button(window, text="Water", command=waterPet)
    btnWater.grid(row=3, column=2, sticky=W)
    # Create Bathe Button
    btnBathe = Button(window, text="Bathe", command=cleanPet)
    btnBathe.grid(row=5, column=2, sticky=W)
    # Create Go Somewhere Button
    btnGoSomewhere = Button(window, text="Go Somewhere", command=showLocationWindow)
    btnGoSomewhere.grid(row=7, column=2)
    # Create Return to Menu button
    btnMenu = Button(window, text="Back", command=showMenuWindow)
    btnMenu.grid(row=7, column=0)

def showLocationWindow():
    """
    Display the location window. This window is used to go somewhere with your pet.
    """
    # Create a new window
    window = newWindow("Location")
    # Create the listbox containing locations to go to
    Lb = Listbox(window)
    if pet.TYPE == "dog":
        Lb.insert(1, 'Dog Park')
        Lb.insert(2, 'Vet')
        Lb.insert(3, 'Walk')
    elif pet.TYPE == "cat":
        Lb.insert(1, 'Pet Store')
        Lb.insert(2, 'Vet')
        Lb.insert(3, 'Walk')
    elif pet.TYPE == "fish":
        Lb.insert(1, 'Aquarium')
        Lb.insert(2, 'Vet')
        Lb.insert(3, 'Swim')
    elif pet.TYPE == "rock":
        Lb.insert(1, 'Gravel Pit')
        Lb.insert(2, 'Vet')
        Lb.insert(3, 'Rock Polisher')
    elif pet.TYPE == "lizzard":
        Lb.insert(1, 'A Hot Rock')
        Lb.insert(2, 'Vet')
        Lb.insert(3, 'Walk')
    elif pet.TYPE == "plant":
        Lb.insert(1, 'Greenhouse')
        Lb.insert(2, 'Plant Specialist')
        Lb.insert(3, 'Flower Pot Store')
    else:
        Lb.insert(1, 'The Park')
    # Create a back button
    btnBack = Button(window, text="Back", command=showPetCareWindow)
    # Create a button to confirm selected location in listbox
    btnGo = Button(window, text="Lets Go!", command=lambda: showOutcomeWindow(Lb.get(Lb.curselection())))
    # Place elements on the window
    Lb.grid(row=0, column=0, columnspan=2)
    btnBack.grid(row=1, column=0, sticky=W)
    btnGo.grid(row=1, column=1, sticky=E)

def showOutcomeWindow(location):
    """
    Display the outcome window. This window is used to display the outcome of going somewhere with your pet.
    """
    # Create a new window
    window = newWindow("Outcome")
    # Change stats and label based on the location you went to
    if location == 'Walk' or location == 'Swim':
        # Display if you walked or swam with your pet
        labelYouWent = Label(window, text="You went on a " + location + " with " + pet.name)
        playWithPet()  # TODO change to correct method
    elif location == 'Vet' or location == 'Plant Specialist':
        # Display where you went with your pet
        labelYouWent = Label(window, text="You went to the " + location + " with " + pet.name)
        takePetToVet()
    else:
        # Display where you went with your pet
        labelYouWent = Label(window, text="You went to the " + location + " with " + pet.name)
        playWithPet()  # TODO change to correct method
    labelYouWent.pack()
    # Create a button to go back to the petcare window
    btnGoBack = Button(window, text="Return Home", command=showPetCareWindow)
    btnGoBack.pack()

def showGiveUpWindow():
    """
    Display the Give Up window. This window is used to give up on your pet.
    """
    # Create a new window
    window = newWindow("Give Up")
    # Create a label to ask the user if they want to give up on their pet
    lblGiveUp = Label(window, text="Would you like to give up on your pet?")
    lblGiveUp.grid(row=0, column=0, columnspan=2)
    # Create a button for yes
    btnYes = Button(window, text="Yes", command=giveUpOnPet)
    btnYes.grid(sticky=E, row=1, column=0)
    # Create a button for no
    btnNo = Button(window, text="No", command=showMenuWindow)
    btnNo.grid(sticky=W, row=1, column=1)

def showRandomEventWindow():
    """
    Display the random event window. This window is used to display a random event with your pet.
    """
    # Create a new window
    window = newWindow("Random Event")
    pass

def showDeathScreenWindow(time, message):
    """
    Display a window that lets the user know that their pet has died.

    Args:
        time (datetime): date/time the pet died
        message (string): a message to give to the user
    """
    # Create a new window
    window = newWindow("Death")
    # Create a label to let the user know their pet has died
    lblInfo = Label(window, text=message)
    lblInfo.grid(row=0, column=0)
    # Create a label to let the user know when their pet died
    timeString = time.strftime("Passed away %b %d, at %I:%M %p")
    lblDate = Label(window, text=timeString)
    lblDate.grid(row=1, column=0)
    # Create a button to switch to the stats window
    btnViewStats = Button(window, text="View Stats", command=showStatsWindow)
    btnViewStats.grid(row=2, column=0)

def showStatsWindow():
    # TODO use the deadPet global to access the pet, not the pet global
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
# Make time pass since program was last opened
if pet is not None:
    simulateEffectOfTimeOnPet()
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
