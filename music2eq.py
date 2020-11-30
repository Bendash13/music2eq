import py_midicsv as pm
import pandas
import re


miditestfile = 'cherry-ripe-piano-solo.mid'
pattern = re.compile(r'2, (\d+), Note_on_c, \d+, (\d+), (\d+)')

# convert MIDI to raw data
def convert_midi2list(filename):
    csv_string = pm.midi_to_csv(filename)
    return csv_string

# pulls out the csv file - potentially take out
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
    print(f'T={tcount} F={fcount}') # prints no. present and not present
    
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
            pitch_list.append(b[2])
    return note_list, pitch_list

# function that finds the centre note to split the song
def centre_pitch(list):
    avg = sum(list)/len(list)
    middle = round(avg)
    return middle

# split data into two groups - changed into x and y coordinates based on pitch
# now splits at the identified centre note rather than through manual iteration process, may need further adjustment
def splitter(list, middle):
    x = []
    y = []
    for item in list:
        if int(item[1]) >= middle:
            y.append(item)
        else:
            x.append(item)
    return x, y
        
# finds number of x and y data to compare
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
    # converts midi to list/csv
    converted = convert_midi2list(miditestfile)
    # find time, pitch and velocity
    parsed_list, pitches = parse_list(converted)
    # finds the central pitch to split the song
    centre = centre_pitch(pitches)
    # splits the song based on the found central pitch
    split_lists = splitter(parsed_list, centre)
    #len_lists_of_lists(split_lists)
    scaled_x = scale_velocity(split_lists[0])
    scaled_y = scale_velocity(split_lists[1])


thing()
