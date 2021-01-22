import networkx as nx 
import turtle
import turtfunctions as tf
import numpy as np
from collections import deque
from pychord import chord
from pychord import ChordProgression
import matplotlib.pyplot as plt 
# visualize both in-chord intervals and chord-to-chord intervals

# twelve tone dict
chromatic = {"C":0,  "C#":1, "Db":1, "D":2, "D#":3, "Eb":3, "E":4, "F":5, "F#":6, "Gb":6, "G":7, "G#":8, "Ab":8, "A":9, "A#":10, "Bb":10, "B":11}
intervals = ["unison", "m2", "maj2", "m3", "maj3", "p4", "tritone" "p5", "m6", "maj6", "m7", "maj7"] # to index

# sample chord progression
testprog = ["Am7", "Cmaj7", "Fmaj7", "Em7"]
prog = ChordProgression(testprog)
chordnotes = [p.components_with_pitch(4) for p in prog] 

tur = turtle.Turtle()
turtle.hideturtle() # hide turtle arrow

for i, chord in enumerate(chordnotes):
	indices = []
	for note in chord:
		index = chromatic[note[:-1]] # get the note and its index for interval purposes
		indices.append(index)
	ints = []
	for j, ind in enumerate(indices):
		if j==0:
			pass
		else:
			ints.append(intervals[np.abs(ind-indices[j-1])])
	chordnotes[i] = (chord, indices, ints)
	print(chordnotes[i])
	turtle.hideturtle() # hide turtle arrow
	tur.penup()
	tur.setpos(-5, 15)
	tur.write(ints[0])
	tur.home()
	tur.penup()
	tur.dot(20, "blue") # first interval
	tur.setpos(95,15)
	tur.write(ints[1])
	tur.penup()
	tur.setpos(100,0)
	tur.dot(20, "green") # second interval
	tur.setpos(195,15)
	tur.write(ints[2])
	tur.setpos(200,0)
	tur.dot(20, "red") #third interval
	tur.home()
	tur.clear()

turtle.done()
# print(chordnotes)

# tonnetz grid representation of circle of intervals
