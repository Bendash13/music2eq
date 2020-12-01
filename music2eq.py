import py_midicsv as pm
import pandas as pd
import re


miditestfile = 'cherry-ripe-piano-solo.mid'
pattern = re.compile(r'2, (\d+), Note_on_c, \d+, (\d+), (\d+)')
tempo_pattern = re.compile(r'1, 0, Tempo, (\d+)')

# convert MIDI to raw data
def convert_midi2list(filename):
    csv_string = pm.midi_to_csv(filename)
    return csv_string


def convert_list2listolists(csv_string):
    listolists = []
    for bit in csv_string:
        bit = bit.strip('\n')
        a = bit.split(',')
        listolists.append(a)
#    df = pd.DataFrame([x.split(',') for x in csv_string.split('/n')])
#    
#    df.to_csv('./midi.csv', sep=',',index=False)
    return listolists
    


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

    
def bpm_get(thing):
    for line in thing:
        b = tempo_pattern.match(line)
        if b == None:
            pass
        else:
            return 60000000/int(b[1])

            
def convert2sec(val, bpm):
    bpval = (60/bpm)/2
    cval = val/480
    return bpval*cval
    
            
# split data into two groups       
        
def splitter(list):
    x = []
    y = []
    for item in list:
        if int(item[1]) >= 58:
            y.append(item)
        else:
            x.append(item)
    return x, y
        
# scale velocity to correct scaling for converter

def len_lists_of_lists(list):
    print(f'y = {len(list[1])} x = {len(list[0])}')


def centre_pitch(keylist):
    avg = sum(keylist)/len(keylist)
    middle = round(avg)
    return middle
    
    
def scale_velocity(list):
    new_list = []
    for i in list:
        val = ((int(i[2])/127)-0.5)*2
        result = [int(i[0]), int(i[1]), val]
        new_list.append(result)
    return new_list


def pdscale(val):
    return ((val/127)-0.5)*40
    
            
def convert2dataframe(listolists):
    df = pd.DataFrame.from_records(listolists, columns=['time', 'pitch', 'velocity'])    
#    df = pd.DataFrame.from_records(listolists, columns=['section', 'time', 'command', 'channel', 'pitch', 'velocity', 'other'])
    return df
    
    
def thing():
    converted = convert_midi2list(miditestfile)
    parsed_list = parse_list(converted)
    split_lists = splitter(parsed_list)
    #len_lists_of_lists(split_lists)
    scaled_x = scale_velocity(split_lists[0])
    scaled_y = scale_velocity(split_lists[1])

def thing2():
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
    
    
def integerer(x):
    return int(x)
    
    
def tester():
    converted = convert_midi2list(miditestfile)
    df = convert_list2listolists(converted)
    df = convert2dataframe(df)
    df.velocity = df[df.velocity != None]
    df.velocity = df.velocity.apply(integerer)
    df = df[df.velocity != 0]
    
    
    
thing2()