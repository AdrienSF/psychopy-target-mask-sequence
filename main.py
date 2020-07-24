import sys
import csv
import random
from psychopy import visual, core, event
from mask import Mask

# check input
description = sys.argv[0] + " <number of trials to run (int)> <SOA in number of refresh frames (int)> <output file name>"

try:
    trial_num = int(sys.argv[1])
    SOA = int(sys.argv[2])
    out_file_name = sys.argv[3]
except:
    print( "\n" + description + "\n")
    raise

# initialize CSV file
with open(out_file_name, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(['trial_number', 'target_location', 'target_orientation', 'SOA', 'RT', 'key_pressed'])

# start experiment
win = visual.Window(size=(800, 600))

for n in range(1, trial_num+1):
    # generate random position and orientation for this trial
    chosen_ori = random.choice([{'label': 'R', 'value': 0}, {'label': 'D', 'value': 90}, 
                                {'label': 'U', 'value': -90}, {'label': 'L', 'value': 180}])
    chosen_pos = random.choice([{'label': 'UR', 'value': (800/4, 600/4)}, {'label': 'UL', 'value': (-800/4, 600/4)}, 
                                {'label': 'LR', 'value': (800/4, -600/4)}, {'label': 'Ll', 'value': (-800/4, -600/4)}])
    # wait for 2 seconds (120 refreshes)
    core.wait(2)
    # Present a small ‘+’ sign in the middle of the screen for 500 ms (30 refreshes)
    plus = visual.TextStim(win, text=u"+")
    plus.draw()
    win.flip()
    core.wait(.5)
    # present the target stimulus at a random orientation for one refresh
    # [NOTE]: unfortunately, letters are not centered
    stim = visual.TextStim(win, text=u"E", units="pix", height=50)
    stim.ori = chosen_ori['value']
    stim.pos = chosen_pos['value']
    stim.draw()
    plus.draw()
    win.flip()
    # start timer as stim is shown
    timer = core.Clock()
    # waiting 1/60 sec should result in displaying for one refresh
    core.wait(1/60)

    # erase the target stimulus and then wait for SOA-1 refreshes
    plus.draw()
    win.flip()
    core.wait(SOA/60)

    # present the mask stimulus for 250 ms (15 refreshes)
    mask = Mask(win=win, pos=chosen_pos['value'])
    mask.draw()
    plus.draw()
    # stim.draw()
    win.flip()
    core.wait(.25)

    # erase the mask stimulus and then begin waiting for a keypress. 
    # Capture the keypress and record which key was pressed (response) and when it was pressed with respect 
    # to the onset of the target (response time, or RT in ms)
    plus.draw()
    win.flip()

    res = event.waitKeys(keyList=['left', 'right', 'up', 'down'], timeStamped=timer)[0]

    # Clear the screen completely
    win.flip()

    # save info to CSV
    info = [ n, chosen_pos['label'], chosen_ori['label'], SOA, res[1], res[0] ]

    with open(out_file_name, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(info)


win.close()