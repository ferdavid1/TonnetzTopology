import networkx as nx 
import librosa as rosa
from jchord.core import Note
from pychord import chord
#from jchord.progressions import ChordProgression
from pychord import ChordProgression
import matplotlib.pyplot as plt 

# sample chord progression
testprog = ["Am7", "Cmaj7", "Fmaj7", "Em7"]
#prog = list(ChordProgression.from_string(testprog))[0] # make progression into list of chord objects
prog = ChordProgression(testprog)
print(prog[0].components_with_pitch(4)) 

# tonnetz grid representation of circle of intervals
#isofifths = {[root, fifth, ],[root, ]}
# root
