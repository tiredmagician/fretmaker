from tkinter import *
import keyindex as ki
from functions import *

#This contains default mappings fret markers
mappings = ['0','1','2','3','4','5']

LARGE_FONT = ("Verdana", 12)

class Fretmaker(Tk):
    ###Class for the main window###
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        key = StringVar()
        scale = StringVar()
        position = StringVar()

        #Drop down menus
        main_menu = Menu(self)
        self.config(menu = main_menu)

        key_menu = Menu(main_menu)
        key_menu.add_radiobutton(label = "C", variable = key, value = 'C')
        key_menu.add_radiobutton(label = "C#", variable = key, value = 'C#')
        key_menu.add_radiobutton(label = "D", variable = key, value = 'D')
        key_menu.add_radiobutton(label = "D#", variable = key, value = 'D#')
        key_menu.add_radiobutton(label = "E", variable = key, value = 'E')
        key_menu.add_radiobutton(label = "F", variable = key, value = 'F')
        key_menu.add_radiobutton(label = "F#", variable = key, value = 'F#')
        key_menu.add_radiobutton(label = "G", variable = key, value = 'G')
        key_menu.add_radiobutton(label = "G#", variable = key, value = 'G#')
        key_menu.add_radiobutton(label = "A", variable = key, value = 'A')
        key_menu.add_radiobutton(label = "A#", variable = key, value = 'A#')
        key_menu.add_radiobutton(label = "B", variable = key, value = 'B')
        main_menu.add_cascade(label = "Key", menu = key_menu)

        scale_menu = Menu(main_menu)
        scale_menu.add_radiobutton(label = 'Major Pentatonic', variable = scale,
                                   value = 'maj_pent')
        scale_menu.add_radiobutton(label = 'Minor Pentatonic', variable = scale,
                                   value = 'min_pent')
        scale_menu.add_radiobutton(label = 'Major', variable = scale,
                                   value = 'maj')
        scale_menu.add_radiobutton(label = 'Natural Minor', variable = scale,
                                   value = 'nat_min')
        scale_menu.add_radiobutton(label = 'Melodic Minor', variable = scale,
                                   value = 'mel_min')
        main_menu.add_cascade(label = "Scale", menu = scale_menu)

        position_menu = Menu(main_menu)
        position_menu.add_radiobutton(label = '1', variable = position, value = '1')
        position_menu.add_radiobutton(label = '2', variable = position, value = '2')
        position_menu.add_radiobutton(label = '3', variable = position, value = '3')
        position_menu.add_radiobutton(label = '4', variable = position, value = '4')
        position_menu.add_radiobutton(label = '5', variable = position, value = '5')
        position_menu.add_radiobutton(label = '6', variable = position, value = '6')
        position_menu.add_radiobutton(label = '7', variable = position, value = '7')
        main_menu.add_cascade(label = "Position", menu = position_menu)

        self.frames = {}

        for F in (StartPage, FretPage, AudioPage):

            frame = F(container, self, key, scale, position)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller, key, scale, position):
        Frame.__init__(self,parent)
        label = Label(self, text = "This is the start page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        fretbutton = Button(self, text = "Fretboard mode", command = lambda: controller.show_frame(FretPage))

        fretbutton.pack()

        audiobutton = Button(self, text = "Audio mode", command = lambda: controller.show_frame(AudioPage))

class FretPage(Frame):

    def __init__(self, parent, controller, key, scale, position):
        Frame.__init__(self,parent)
        self.key = key
        self.scale = scale
        self.position = position

        topframe = Frame(self,parent)
        topframe.pack()

        bottomframe = Frame(self,parent)
        bottomframe.pack(side = BOTTOM)

        #labels for all the strings
        ylabel0 = Label(bottomframe, text = 'E')
        ylabel1 = Label(bottomframe, text = 'B')
        ylabel2 = Label(bottomframe, text = 'G')
        ylabel3 = Label(bottomframe, text = 'D')
        ylabel4 = Label(bottomframe, text = 'A')
        ylabel5 = Label(bottomframe, text = 'E')

        ylabel0.grid(row = 0, column = 0)
        ylabel1.grid(row = 1, column = 0)
        ylabel2.grid(row = 2, column = 0)
        ylabel3.grid(row = 3, column = 0)
        ylabel4.grid(row = 4, column = 0)
        ylabel5.grid(row = 5, column = 0)

        #labels for position markers(variable)
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

        #Canvas with the default fretboard drawn
        fretboard_canvas = Canvas(bottomframe, bg = "white", width = 450, height = 200)
        fretboard_canvas.grid(row = 0, rowspan = 6, column = 1, columnspan = 6)
        fretboard_canvas.create_rectangle(36, 15, 418, 190, outline = 'black')
        fretboard_canvas.create_line(36, 50, 418, 50)
        fretboard_canvas.create_line(36, 85, 418, 85)
        fretboard_canvas.create_line(36, 120, 418, 120)
        fretboard_canvas.create_line(36, 155, 418, 155)
        fretboard_canvas.create_line(112, 15, 112, 190)
        fretboard_canvas.create_line(189, 15, 189, 190)
        fretboard_canvas.create_line(265, 15, 265, 190)
        fretboard_canvas.create_line(342, 15, 342, 190)

        #Function to be called when the next note button is pressed
        def next_note():
            curr_key = key.get()
            curr_scale = scale.get()
            curr_pos = position.get()
            if curr_key == '' or curr_scale == '' or curr_pos == '':
                tkinter.messagebox.showinfo('Error',
                'Choose a key, scale and position.')
            else:
                make_note(curr_key, curr_scale, curr_pos, fretboard_canvas, bottomframe)

        #The button bound to the make_note function
        next_button = Button(topframe,
            text = "Next Note",
            fg = 'black',
            command = next_note)

        next_button.pack(side = LEFT)

        #Home button
        home_button = Button(topframe,
            text = "Back to Home",
            command=lambda: controller.show_frame(StartPage))

        home_button.pack()

class AudioPage(Frame):
     def __init__(self, parent, controller, key, scale, position):
         Frame.__init__(self, parent)
         self.key = key
         self.scale = scale
         self.position = position

         #Function to be called when play note button is pressed
         def play_note():
             curr_key = key.get()
             curr_scale = scale.get()
             curr_pos = position.get()
             if curr_key == '' or curr_scale == '' or curr_pos == '':
                 tkinter.messagebox.showinfo('Error',
                 'Choose a key, scale and position.')
             else:
                 get_audio(curr_key, curr_scale, curr_pos)

         #The button bound to the make_note function
         play_button = Button(topframe,
             text = "Play Note",
             fg = 'black',
             command = play_note)

         play_button.pack(side = LEFT)

         #Home button
         home_button = Button(topframe,
             text = "Back to Home",
             command=lambda: controller.show_frame(StartPage))

         home_button.pack()

app = Fretmaker()
app.title("Guitar training")
app.mainloop()
