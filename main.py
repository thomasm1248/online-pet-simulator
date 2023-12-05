from pets import *
import pet_events.some_events as pe
import random

import datetime


def main():
    rock = Rock.adopt("Dwayne", 10000, datetime.datetime.now(), "a")
    
    try:
        
        for day in range(206):
            for i in range(1440):
                rock.update(datetime.datetime.now() + datetime.timedelta(0, 60*i) + datetime.timedelta(0, 60*1400*day))
                
                if random.random() < 1e-2:
                    activity = random.choice(range(7))
                    
                    if activity <= 1:
                        pe.play(rock, 0.4)
                    elif activity <= 3:
                        pe.clean(rock, .2)
                    elif activity <= 4:
                        pe.medicate(rock, 0.5)
                    elif activity <= 5:
                        pe.feed(rock, 0.4)
                    elif activity <= 6:
                        pe.hydrate(rock, .3)

            #pe.play(rock, 0.4)
    except PassedAway:
        
        ...
    print(rock.adoption_time)
    print(rock.last_update)
    #pprint(rock.current_stats())
        

    
    #pprint(rock.current_stats())
    
    rock.plot_stats('assets/temp/plot.png')

    
if __name__=="__main__":
    main()