import networkx as nx 
import librosa as rosas
from jchord.core import Note
from jchord.chords import Chord
import matplotlib.pyplot as plt 

# sample chord progression
prog = ["A minor7", "C major7", "F major7", "E minor7"]
prog = [(p.split()[0], p.split()[1]) for p in prog] # split into root and quality

jprog = [] #jchord chord objects for each chord in the progression
for (r,q) in prog: # root and quality
	jprog.append(Chord.from_name(q).with_root(Note(r, 4)))

intervals = [j.intervals() for j in jprog]
print(jprog)
# tonnetz grid representation of circle of intervals
#isofifths = {[root, fifth, ],[root, ]}
# root
