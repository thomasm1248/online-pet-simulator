

# Information about project

## Structure of system

- Python script
- Data file to save the state of the simulation between sessions

## On start

- Read save file
- Simulate elapsed time and update state variables
- Build GUI
- Start listening for events
	- Adopt a pet
	- Save and exit
	- Feed
	- Play
	- Clean
	- Hydrate
	- Doctor
	- Groom

## Pet

### State variables

- Money spent to date
- Food level
- Water level
- Love level
- Hygiene level
- Health
- Name
- Picture
- Pet type

### Classes

- Cat
- Dog
- Fish
- Lizard
- Rock
- Plant

### Stats, Rates, & Costs

- Hunger rate
- Thirst rate
- Loneliness rate
- Dirty rate
- Groom rate
- Health crisis chance
- Food refill cost
- Groom cost
- Doctor visit cost
- Cleaning cost
- Initial purchase cost
