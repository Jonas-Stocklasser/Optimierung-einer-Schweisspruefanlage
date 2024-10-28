#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage

import customtkinter as ctk  # import of the customtkinter library
from tkinter import messagebox
import time
from Package.JsonFunctions import json_writer

from Package.StartScreen import StartScreen  # import of all the other files of the python package
from Package.OptionsScreen import OptionsScreen
from Package.NewTestScreen01 import NewTestScreen01
from Package.NewTestScreen02 import NewTestScreen02
from Package.NewTestScreen03 import NewTestScreen03
from Package.NewTestScreen04 import NewTestScreen04
from Package.NewTestScreen05 import NewTestScreen05
from Package.NewTestScreen06 import NewTestScreen06
from Package.TestPreparations01 import TestPreparations01
from Package.TestRun01 import TestRun01

# Shared variables----------------------------------------
# import of the GetStartupVariables class located in the sharedVar file
from Package.SharedVar import GetStartupVariables, main_pi_location

window_geometry = GetStartupVariables.window_geometry

class App(ctk.CTk):  # main window class, every other window class is called from here and is a child of this
    def __init__(self, title):  # title is given as an attribute from the class call

        # main initialization----------------------------------------
        super().__init__()
        self.aspect_ratio = 4 / 3
        ctk.set_appearance_mode(GetStartupVariables.appearance_mode[0])
        ctk.set_default_color_theme("blue")
        self.title(title)

        self.geometry(f"{window_geometry[0]}x{window_geometry[1]}")
        self.resizable(True, True)
        #self.after(1000, lambda: self.state("zoomed"))

        self.last_resize_time = 0  # Timestamp of the last resize event
        self.resize_interval = 0.02  # Time in seconds to wait before processing the next resize event

        # dictionary for all window frames----------------------------------------
        self.windows = {"0": StartScreen(self),
                        "1.0": NewTestScreen01(self),
                        "1.1": NewTestScreen02(self),
                        "1.2": NewTestScreen03(self),
                        "1.3": NewTestScreen04(self),
                        "1.4": NewTestScreen05(self),
                        "1.5": NewTestScreen06(self),
                        "2.0": TestPreparations01(self),
                        "3": OptionsScreen(self),
                        "4.0": TestRun01(self)}

        # top level windows----------------------------------------
        self.reallyswitch = None  # initializes the window variable as "None"

        # show start screen initially----------------------------------------
        self.switch_window(GetStartupVariables.start_window)

        self.protocol("WM_DELETE_WINDOW", lambda: self.close_commands())

        # Bind events
        self.bind("<Configure>", self.on_resize)
        self.bind("<Unmap>", self.on_unmap)

        # run the app----------------------------------------
        self.mainloop()  # the main App window is run (mainloop)

    # methods----------------------------------------
    def confirm_go_back(self, which):
        if messagebox.askokcancel("Wirklich zurück gehen?",
                                  "Wollen Sie wirklich zum vorherigen Bildschirm zurückgehen?"):
            self.switch_window(which)
        else:
            pass

    def switch_window(self, which):  # method for switching windows with the attribute "which"
        for window in self.windows.values():
            window.pack_forget()  # forget every window that is in the dictionary

        if which in self.windows:
            self.windows[which].pack(expand=True, fill="both")  # place the window with the matching index to the attribute "which"

    def on_resize(self, event):
        current_time = time.time()
        if current_time - self.last_resize_time < self.resize_interval:
            return  # Ignore this event if it's too soon after the last one

        self.last_resize_time = current_time  # Update the last resize time

        # Maintain aspect ratio when resizing the window.
        width = self.winfo_width()
        height = self.winfo_height()

        # Calculate the new height based on the width and aspect ratio
        new_height = int(width / self.aspect_ratio)

        # If the height has changed, resize the window to maintain aspect ratio
        if height != new_height:
            self.geometry(f"{width}x{new_height}")  # Update geometry to maintain aspect ratio
            font_size = new_height / 40
            print(font_size)
            self.update_fonts(font_size)


    def update_fonts(self, font_size):
        for window in self.windows.values():
            # Assuming each window has a method to update its fonts
            if hasattr(window, 'update_font_size'):
                window.update_font_size(font_size)


    def on_unmap(self, event):
        # Handle the window being unmaximized
        width = self.winfo_width()
        new_height = int(width / self.aspect_ratio)
        self.geometry(f"{width}x{new_height}")  # Adjust the size to maintain aspect ratio


    def close_commands(self):
        if messagebox.askokcancel("Applikation beenden", "Möchten Sie die Applikation wirklich beenden?"):
            if "4.0" in self.windows:
                test_run_01 = self.windows["4.0"]
                if hasattr(test_run_01, "cancel_after_on_closing"):
                    test_run_01.cancel_after_on_closing()
            self.destroy()
        else:
            pass


if __name__ == "__main__":  # when the file this is in is called "main" then it is run
    GetStartupVariables()  # run GetStartupVariables from sharedVar
    App(GetStartupVariables.name_of_app)
    # calls the App class and passes the sharedVar name_of_app as the attribute "title"
