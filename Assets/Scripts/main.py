#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage

import customtkinter as ctk  # import of the libraries
from tkinter import messagebox
from screeninfo import get_monitors
import RPi.GPIO as GPIO

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
from Package.SharedVar import GetStartupVariables

monitor = get_monitors()[0] # get the current monitors specifications
current_window = None # instance variable to track which screen is displayed


class App(ctk.CTk):  # main window class, every other window class is called from here and is a child of this one
    def __init__(self, title, window_geometry):  # title is given as an attribute from the class call

        # main initialization----------------------------------------
        super().__init__()
        ctk.set_appearance_mode(GetStartupVariables.appearance_mode[0]) # general application settings
        ctk.set_default_color_theme("blue")
        self.title(title)
        self.geometry(f"{window_geometry[0]}x{window_geometry[1]}")
        print(window_geometry)
        global current_window

        # dictionary for all window frames----------------------------------------
        self.windows = {"0": StartScreen(self, window_geometry),
                        "1.0": NewTestScreen01(self, window_geometry),
                        "1.1": NewTestScreen02(self, window_geometry),
                        "1.2": NewTestScreen03(self, window_geometry),
                        "1.3": NewTestScreen04(self, window_geometry),
                        "1.4": NewTestScreen05(self, window_geometry),
                        "1.5": NewTestScreen06(self, window_geometry),
                        "2.0": TestPreparations01(self, window_geometry),
                        "3": OptionsScreen(self, window_geometry),
                        "4.0": TestRun01(self, window_geometry)}

        # show start screen initially----------------------------------------
        self.switch_window(GetStartupVariables.start_window)

        # App closing handling
        self.protocol("WM_DELETE_WINDOW", lambda: self.close_commands())

        # keybindings for the ventilation feature and test methods----------------------------------------
        self.bind("<Return>", lambda event: TestPreparations01.unair_on(current_window))
        self.bind("<KeyRelease-Return>", lambda event: TestPreparations01.unair_off(current_window))
        self.bind("1", lambda event: TestRun01.test_stop_functionality_too_low(current_window))
        self.bind("2", lambda event: TestRun01.test_stop_functionality_normal1(current_window))
        self.bind("3", lambda event: TestRun01.test_stop_functionality_normal2(current_window))
        self.bind("4", lambda event: TestRun01.test_stop_functionality_too_high(current_window))
        self.bind("<Up>", lambda event: TestRun01.test_stop_functionality_pressure_up(current_window))
        self.bind("<Down>", lambda event: TestRun01.test_stop_functionality_pressure_down(current_window))

        # run the app----------------------------------------
        self.mainloop()  # the main App window is run (mainloop)

    # methods----------------------------------------
    def confirm_go_back(self, which):
        if messagebox.askokcancel("Wirklich zurück gehen?",
                                  "Wollen Sie wirklich zum vorherigen Bildschirm zurückgehen?"):
            self.switch_window(which) # the "which" argument is passed on to the switch_window method
        else:
            pass

    def error_message(self, title, text): # to display errors
        messagebox.showerror(title, text)

    def switch_window(self, which):  # method for switching windows with the attribute "which"
        global current_window
        for window in self.windows.values():
            window.place_forget()  # place_forget every window that is in the dictionary

        if which in self.windows:
            self.windows[which].place(x=10,
                                      y=10)  # place the window with the matching index to the attribute "which" in the main window
        current_window = which # set the current window variable to the right window

    def close_commands(self): # on closing the app
        if messagebox.askokcancel("Applikation beenden", "Möchten Sie die Applikation wirklich beenden?"):
            if "4.0" in self.windows: # if the test_run_01 window is open then ensure the pump is deactivated
                test_run_01 = self.windows["4.0"]
                if hasattr(test_run_01, "cancel_after_on_closing"):
                    test_run_01.cancel_after_on_closing()
            GPIO.cleanup() # cleanup of all GPIO ports
            self.destroy() # destroy the App window
        else:
            pass


if __name__ == "__main__":  # gets executed when inside the "main"
    print("startup")
    window_height = monitor.height # get the monitors height
    window_width = int(window_height * (4 / 3)) # calculate the 4:3 monitor width
    window_geometry_new = [window_width, window_height] # set the geometry to the new dimensions
    GetStartupVariables()
    # calls the App class and passes the sharedVar name_of_app as the attribute "title"
    App(GetStartupVariables.name_of_app, window_geometry_new)
