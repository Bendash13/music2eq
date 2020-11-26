import py_midicsv as pm
import pandas
import re

miditestfile = 'cherry-ripe-piano-solo.mid'
pattern = re.compile(r'2, (\d+), Note_on_c, \d+, (\d+), (\d+)')

# convert MIDI to raw data
def convert_midi2list(filename):
    csv_string = pm.midi_to_csv(filename)
    return csv_string

# pulls out the csv file - not strictly necessary
def convert_midi2csv():
    df = pandas.DataFrame(data={"col1": csv_string})
    df.to_csv('./midi.csv', sep=',',index=False)

def checker(string, list):
    tcount = 0 # counts if the string is present
    fcount = 0 # counts if the string is not present
    for item in list:
        if string in item:
            tcount+=1
        else:
            fcount+=1
    print(f'T={tcount} F={fcount}') # prints no. of present and not present
    
# cuts out the time, pitch and velocity so we know what to work with    
def parse_list(list):
    note_list = []
    for line in list:
        b = pattern.match(line)
        if b == None:
            pass
        else:
#            time = b[1]
#            pitch = b[2]
#            velocity = b[3]
            result = [b[1], b[2], b[3]]
            note_list.append(result)
    return note_list

# split data into two groups - changed into the x and y coordinates based on pitch       
# currently at 58, just under middle C (midi pitch - 60)        
def splitter(list):
    x = []
    y = []
    for item in list:
        if int(item[1]) >= 58: # dictates halfway point
            y.append(item)
        else:
            x.append(item)
    return x, y

# compares the list of x movements vs the list of y movements, try to be as even as possible
def len_lists_of_lists(list):
    print(f'y = {len(list[1])} x = {len(list[0])}')

# scale velocity to correct scaling for converter
def scale_velocity(list):
    new_list = []
    for i in list:
        val = ((int(i[2])/127)-0.5)*2
        result = [int(i[0]), int(i[1]), val]
        new_list.append(result)
    return new_list
            
            
    
    
def thing():
    # converts midi file into a list
    converted = convert_midi2list(miditestfile)
    # separates the important information from the midi file
    parsed_list = parse_list(converted)
    # splits the list based on pitch into x and y coordinates
    split_lists = splitter(parsed_list)
    #len_lists_of_lists(split_lists)
    # scales the velocity to give the shake table movement
    scaled_x = scale_velocity(split_lists[0])
    scaled_y = scale_velocity(split_lists[1])


thing()
