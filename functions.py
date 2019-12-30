from keyindex import *
from audioindex import *
from tkinter import *
from playsound import playsound
import tkinter.messagebox
import random

def delete_note(fretboard_canvas):
    fretboard_canvas.delete('note')

def make_note_list(scale, position):
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


def choose_note(note_list):
    ###Generates a random note from the note list.###
    return random.choice(note_list)

def print_note(note, fretboard_canvas):
    ###prints the note into the fretboard canvas###
    fretboard_canvas.create_oval(
        finger_positions[note],
        fill = 'red',
        outline = '',
        tags = 'note',
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

def make_note(key, scale, position, fretboard_canvas, bottomframe):
    ###Makes new note###
    delete_note(fretboard_canvas)
    note_list = make_note_list(scale, position)
    note = choose_note(note_list)
    print_note(note, fretboard_canvas)
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

def get_audio(key, scale, position):
    audio_list = make_audio_list(key, scale, position)
    note = choose_note(audio_list)
    playsound(audio_dictionary[note])
