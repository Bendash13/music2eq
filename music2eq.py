import py_midicsv as pm
import pandas
import re

upper_notes = []
x = {}
y = {}
miditestfile = 'cherry-ripe-piano-solo.mid'

# convert MIDI to raw data
def convert_midi2list(filename):
    csv_string = pm.midi_to_csv(filename)
    return csv_string


def convert_midi2csv():
    df = pandas.DataFrame(data={"col1": csv_string})
    df.to_csv('./midi.csv', sep=',',index=False)

def checker(string, list):
    tcount = 0
    fcount = 0
    for item in list:
        if string in item:
            tcount+=1
        else:
            fcount+=1
    print(f'T={tcount} F={fcount}')
    
    
def parse_list(list):
    checker('Note_on_c', converted)
    for line in list:
        pattern = re.compile('2, (\d+), Note_on_c, \d+, (\d+), (\d+)')
        re = pattern.match(line)
        print(re[0])

def thing():
    converted = convert_midi2list(miditestfile)
    
    


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


thing()