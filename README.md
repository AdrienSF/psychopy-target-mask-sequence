# Psychopy target mask sequence
This project uses psychopy to perform a [masking experiment](https://en.wikipedia.org/wiki/Visual_masking).
 
## Experiment design specifications
Assuming a screen with a 60 Hz refresh rate (16.6666666... ms per refresh).
The experiment has N number of trials (N is parameter).
The delay between the target and mask stimulus is called the stimulus onset asynchrony (SOA). The SOA is a parameter, expressed in number of refresh frames.
The target stimulus is the letter ‘E’ (capital) presented at one of four orientations (with arms facing up, down, left, or right).
The mask stimulus is four small squares, equal in size to the letter ‘E’, surrounding the location of the letter ‘E’.
The target-mask sequence is presented at one of four possible locations in the periphery (UL = upper left, UR = upper right, LL = lower left, LR = lower right), chosen at random on each trial -  [like in Del Cul et al (2007)](https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0050260&type=printable).
Valid responses are one of the four arrow keys on the keyboard (upArrow, downArrow, leftArrow, rightArrow).
 
On each trial, the script:
* Presents a small ‘+’ sign in the middle of the screen for 500 ms (30 refreshes)
* Keeping the ‘+’ sign on the screen, presents the target stimulus at a random orientation for one refresh
* Keeping the ‘+’ sign on the screen, erases the target stimulus and then wait for SOA-1 refreshes
* Keeping the ‘+’ sign on the screen, presents the mask stimulus for 250 ms (15 refreshes)
* Keeping the ‘+’ sign on the screen, erases the mask stimulus and then begins waiting for a keypress. It captures the keypress and records which key was pressed (response) and when it was pressed with respect to the onset of the target (response time, or RT in ms)
* The script clears the screen completely and then waits for 2 seconds (120 refreshes)
N trials are performed.
 
The results are saved to a tab-delimited file (CSV) with the following columns:
* Trial number (sequential)
* Target location (‘UL’, ‘UR’, ‘LL’, ‘LR’)
* Target orientation (‘U’, ‘D’, ‘L’, ‘R’)
* SOA (for this simple version it will always be the same number)
* Reaction time (RT)
* Which key was pressed
 
 
## Installation
To run this script, the psychopy python library is required. After cloning or downloading this repository, run main.py to launch the experiment. The number of trials to run, SOA, and output file name are given as command line arguments:

python3 main.py < number of trials to run > < SOA in number of refresh frames > < output file name >
