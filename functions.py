from keyindex import *
from tkinter import *
import tkinter.messagebox
import random

def delete_note(fretboard_canvas):
    fretboard_canvas.delete('note')

def make_note_list(scale, position):
    ###Generate a list of notes from the given scale, position###
    if scale == 'minor_pentatonic':
        if position in ('6','7'):
            tkinter.messagebox.showinfo('Error',
            'The minor pentatonic scale only has 5 positions!')
        else:
            return minor_pentatonic_positions[position]

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

def change_fret_markers(key, scale, position):
    ###Changes position of fret markers depending on position, key, scale
    string = key + "_" + scale + "_" + position
    mappings = fret_marker_mappings[string]

def make_note(key, scale, position, fretboard_canvas):
    ###Makes new note###
    delete_note(fretboard_canvas)
    note_list = make_note_list(scale, position)
    note = choose_note(note_list)
    print_note(note, fretboard_canvas)
    change_fret_markers(key, scale, position)
