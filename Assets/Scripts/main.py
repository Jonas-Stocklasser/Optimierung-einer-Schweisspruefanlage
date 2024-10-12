#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage

import customtkinter as ctk  # import of the customtkinter library

from Package.StartScreen import StartScreen  # import of all the other files of the python package
from Package.OptionsScreen import OptionsScreen
from Package.ReallySwitch import ReallySwitch
from Package.NewTestScreen01 import NewTestScreen01
from Package.NewTestScreen02 import NewTestScreen02
from Package.NewTestScreen03 import NewTestScreen03
from Package.NewTestScreen04 import NewTestScreen04
from Package.NewTestScreen05 import NewTestScreen05
from Package.NewTestScreen06 import NewTestScreen06
from Package.TestPreparations01 import TestPreparations01

# Shared variables----------------------------------------
# import of the GetStartupVariables class located in the sharedVar file
from Package.SharedVar import GetStartupVariables


class App(ctk.CTk):  # main window class, every other window class is called from here and is a child of this
    def __init__(self, title):  # title is given as an attribute from the class call

        # main initialization----------------------------------------
        super().__init__()
        ctk.set_appearance_mode(GetStartupVariables.appearance_mode[0])
        ctk.set_default_color_theme("blue")
        self.title(title)
        self.geometry(f"{GetStartupVariables.window_geometry[0]}x{GetStartupVariables.window_geometry[1]}")
        self.resizable(False, False)

        # dictionary for all window frames----------------------------------------
        self.windows = {"0": StartScreen(self),
                        "1.0": NewTestScreen01(self),
                        "1.1": NewTestScreen02(self),
                        "1.2": NewTestScreen03(self),
                        "1.3": NewTestScreen04(self),
                        "1.4": NewTestScreen05(self),
                        "1.5": NewTestScreen06(self),
                        "2.0": TestPreparations01(self),
                        "3": OptionsScreen(self)}

        # top level windows----------------------------------------
        self.reallyswitch = None    # initializes the window variable as "None"

        # show start screen initially----------------------------------------
        self.switch_window(GetStartupVariables.start_window)

        # run the app----------------------------------------
        self.mainloop()  # the main App window is run (mainloop)

    # methods----------------------------------------
    def open_top_level_window_really_switch(self, which):  # method for creating or focusing the top level window
        # "which" is an attribute given by each back button when calling this method
        if self.reallyswitch is None or not self.reallyswitch.winfo_exists():  # checking if the window exists
            self.reallyswitch = ReallySwitch(self, which)  # the top level window class (Package.ReallySwitch)is called
        else:
            self.reallyswitch.focus()  # focus the window if it exists

    def switch_window(self, which):  # method for switching windows with the attribute "which"
        for window in self.windows.values():
            window.place_forget()   # forget every window that is in the dictionary

        if which in self.windows:
            self.windows[which].place(x=5, y=5)  # place the window with the matching index to the attribute "which"


if __name__ == "__main__":  # when the file this is in is called "main" then it is run
    GetStartupVariables()  # run GetStartupVariables from sharedVar
    App(GetStartupVariables.name_of_app)
    # calls the App class and passes the sharedVar name_of_app as the attribute "title"
