import py_midicsv as pm
import pandas

upper_notes = []
x = {}
y = {}
# convert MIDI to raw data
def parse_csv():
    csv_string = pm.midi_to_csv("cherry-ripe-piano-solo.mid")
    df = pandas.DataFrame(data={"col1": csv_string})
    df.to_csv('./midi.csv', sep=',',index=False)


# split data into two groups
def check(input):
    if input in upper_notes:
        return True
    else:
        return False
        
        
def splitter():
    for section in csv_string:
        upper = check(section)
        if upper == True:
            x.append(section)
        else:
            y.append(section)
    
    
# timing fix?
# scale velocity to correct scaling for converter


parse_csv()