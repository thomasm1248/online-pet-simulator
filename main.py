from pets import *
import pet_events.some_events as pe

import datetime
from pprint import pprint

def main():
    rock = Plant.adopt("roccko", 10000, datetime.datetime.now(), "a")

    pprint(rock.serialize())
    
    try:
        for _ in range(100_000):
            rock.update(datetime.datetime.now())
    except PassedAway:
        print(_)
        ...
        
    #pprint(rock.current_stats())
        
    pe.medicate(rock, 0.5)
    pe.play(rock, 0.4)
    pe.feed(rock, 0.4)
    pe.hydrate(rock, .3)
    pe.clean(rock, .2)
    
    #pprint(rock.current_stats())
    
    rock.plot_stats('assets/temp/plot.png')

    
if __name__=="__main__":
    main()