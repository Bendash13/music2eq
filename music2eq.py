import py_midicsv as pm
import pandas as pd
import re


miditestfile = 'cherry-ripe-piano-solo.mid'
pattern = re.compile(r'2, (\d+), Note_on_c, \d+, (\d+), (\d+)')
tempo_pattern = re.compile(r'1, 0, Tempo, (\d+)')

# convert MIDI to raw csv data
def convert_midi2list(filename):
    csv_string = pm.midi_to_csv(filename)
    return csv_string

#Parse data list to create list of time, pitch, velocity for dataframe conversion    
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
            result = [int(b[1]), int(b[2]), int(b[3])]
            note_list.append(result)
            
    return note_list

    
#Calculate the BPM from tempo in MIDI file
def bpm_get(thing):
    for line in thing:
        b = tempo_pattern.match(line)
        if b == None:
            pass
        else:
            return 60000000/int(b[1])

            
#Convert MIDI clock time to seconds using calculated BPM
def convert2sec(val, bpm):
    bpval = (60/bpm)/2
    cval = val/480
    return bpval*cval
    
    
#Calculate centre pitch to evenly distribute data to x and y movements
def centre_pitch(keylist):
    avg = sum(keylist)/len(keylist)
    middle = round(avg)
    return middle
    

#Function for .apply() to scale velocity
def pdscale(val):
    return ((val/127)-0.5)*40
    

#Convert list of lists generated by parse_list() into pandas dataframe
def convert2dataframe(listolists):
    df = pd.DataFrame.from_records(listolists, columns=['time', 'pitch', 'velocity'])    
#    df = pd.DataFrame.from_records(listolists, columns=['section', 'time', 'command', 'channel', 'pitch', 'velocity', 'other'])
    return df
    
    
#Function to run through the whole process to generate scaled x and y values, currently just prints descriptives of data
def music2eq():
    converted = convert_midi2list(miditestfile)
    bpm = bpm_get(converted)
    parsed_list = parse_list(converted)
    df = convert2dataframe(parsed_list)
    df = df[df.velocity != 0]
    df.velocity = df.velocity.apply(pdscale)
    df.time = df.time.apply(convert2sec, args=(bpm,))
    split_pitch = centre_pitch(df.pitch.tolist())
    x = df[df.pitch >= split_pitch]
    y = df[df.pitch < split_pitch]
    x = x.groupby('time', as_index=False).mean()
    y = y.groupby('time', as_index=False).mean()
    statx = x.describe()
    staty = y.describe()
    print(statx, staty)
    
     
music2eq()