from fretindex import *
from audioindex import *
from noteindex import *
from tkinter import *
from playsound import playsound
from sys import platform
import tkinter.messagebox
import random

def delete_fret(fretboard_canvas):
    fretboard_canvas.delete('fret')

def make_fret_list(scale, position):
    ###Generate a list of notes from the given scale, position###
    if scale == 'min_pent':
        if position in ('6','7'):
            tkinter.messagebox.showinfo('Error',
            'The pentatonic scale only has 5 positions!')
        else:
            return min_pent_positions[position]
    elif scale == 'maj_pent':
        if position in ('6','7'):
            tkinter.messagebox.showinfo('Error',
            'The pentatonic scale only has 5 positions!')
        else:
            return maj_pent_positions[position]

def choose_fret(fret_list):
    ###Generates a random fret from the fret list.###
    return random.choice(fret_list)

def print_fret(fret, fretboard_canvas):
    ###prints the note into the fretboard canvas###
    fretboard_canvas.create_oval(
        finger_positions[fret],
        fill = 'red',
        outline = '',
        tags = 'fret',
        )

def change_fret_markers(key, scale, position, bottomframe):
    ###Changes position of fret markers depending on position, key, scale
    string = key + "_" + scale + "_" + position
    mappings = fret_marker_mappings[string]
    xlabel0 = Label(bottomframe, text = mappings[0])
    xlabel1 = Label(bottomframe, text = mappings[1])
    xlabel2 = Label(bottomframe, text = mappings[2])
    xlabel3 = Label(bottomframe, text = mappings[3])
    xlabel4 = Label(bottomframe, text = mappings[4])
    xlabel5 = Label(bottomframe, text = mappings[5])

    xlabel0.grid(row = 6, column = 1)
    xlabel1.grid(row = 6, column = 2)
    xlabel2.grid(row = 6, column = 3)
    xlabel3.grid(row = 6, column = 4)
    xlabel4.grid(row = 6, column = 5)
    xlabel5.grid(row = 6, column = 6)

def make_fret(key, scale, position, fretboard_canvas, bottomframe):
    ###Makes new note###
    delete_fret(fretboard_canvas)
    fret_list = make_fret_list(scale, position)
    fret = choose_fret(fret_list)
    print_fret(fret, fretboard_canvas)
    change_fret_markers(key, scale, position, bottomframe)

def make_audio_list(key, scale, position):
    if scale == 'min_pent':
        if position in ('6','7'):
            tkinter.messagebox.showinfo('Error',
            'The pentatonic scale only has 5 positions!')
        else:
            return min_pent_audio_positions[(key+position)]
    elif scale == 'maj_pent':
        if position in ('6','7'):
            tkinter.messagebox.showinfo('Error',
            'The pentatonic scale only has 5 positions!')
        else:
            return maj_pent_audio_positions[(key+position)]

def make_audio(key, scale, position):
    audio_list = make_audio_list(key, scale, position)
    audio = choose_fret(audio_list)
    if platform == "darwin":
        playsound("audio//" + audio + ".wav")
    elif platform == "win32":
        playsound("audio\\" + audio + ".wav")

def make_note_list(key, scale, position):
    if scale == 'min_pent':
        if position in ('6','7'):
            tkinter.messagebox.showinfo('Error',
            'The pentatonic scale only has 5 positions!')
        else:
            return min_pent_note_dictionary[position]
    elif scale == 'maj_pent':
        if position in ('6','7'):
            tkinter.messagebox.showinfo('Error',
            'The pentatonic scale only has 5 positions!')
        else:
            return maj_pent_note_dictionary[position]

def make_note(key, scale, position, display):
    note_list = make_note_list(key, scale, position)
    note = choose_fret(note_list)
    display.config(text = note)
