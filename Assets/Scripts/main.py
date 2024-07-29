#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage

import customtkinter as ctk

from Package.StartScreen import StartScreen  # imports of other files of the package
from Package.OptionsScreen import OptionsScreen
from Package.ReallySwitch import ReallySwitch
from Package.NewTestScreen01 import NewTestScreen01
from Package.NewTestScreen02 import NewTestScreen02
from Package.NewTestScreen03 import NewTestScreen03
from Package.NewTestScreen04 import NewTestScreen04
from Package.NewTestScreen05 import NewTestScreen05
from Package.NewTestScreen06 import NewTestScreen06

# Shared variables----------------------------------------
from Package.SharedVar import GetStartupVariables
# import of shared variables located in the sharedVar file


class App(ctk.CTk):  # main window class, every other window class is called from here
    def __init__(self, title):  # title is given as an attribute from the class call
        # main initialization----------------------------------------
        super().__init__()
        ctk.set_appearance_mode(GetStartupVariables.appearance_mode[0])
        ctk.set_default_color_theme("blue")
        self.title(title)
        self.geometry(f"{GetStartupVariables.window_geometry[0]}x{GetStartupVariables.window_geometry[1]}")
        self.resizable(False, False)

        # windows----------------------------------------
        self.startscreen = StartScreen(self)  # ID = 0      other classes
        self.newtestscreen01 = NewTestScreen01(self)  # ID = 1.0
        self.newtestscreen02 = NewTestScreen02(self)  # ID = 1.1
        self.newtestscreen03 = NewTestScreen03(self)  # ID = 1.2
        self.newtestscreen04 = NewTestScreen04(self)  # ID = 1.3
        self.newtestscreen05 = NewTestScreen05(self)  # ID = 1.4
        self.newtestscreen06 = NewTestScreen06(self)  # ID = 1.5
        self.optionsscreen = OptionsScreen(self)  # ID = 2

        # top level windows----------------------------------------
        self.reallyswitch = None

        # show start screen initially----------------------------------------
        self.switch_window(GetStartupVariables.start_window)

        # run the app----------------------------------------
        self.mainloop()  # the main App window is run (mainloop)

    def open_top_level_window_really_switch(self, which):  # method for creating or focusing the top level window
        # "which" is an attribute given by the back button which calls this function
        if self.reallyswitch is None or not self.reallyswitch.winfo_exists():  # checking if the window exists
            self.reallyswitch = ReallySwitch(self, which)  # the top level window class from the other file is called
        else:
            self.reallyswitch.focus()  # focus the window if it exists

    def switch_window(self, which):  # method for switching windows with the attribute "which"
        if which == "0":
            self.startscreen.place(x=5, y=5)  # the wanted window is placed and all others are deleted from the window
            self.optionsscreen.place_forget()
            self.newtestscreen01.place_forget()
            self.newtestscreen02.place_forget()
            self.newtestscreen03.place_forget()
            self.newtestscreen04.place_forget()
            self.newtestscreen05.place_forget()
            self.newtestscreen06.place_forget()
        elif which == "1.0":
            self.newtestscreen01.place(x=5, y=5)
            self.startscreen.place_forget()
            self.optionsscreen.place_forget()
            self.newtestscreen02.place_forget()
            self.newtestscreen03.place_forget()
            self.newtestscreen04.place_forget()
            self.newtestscreen05.place_forget()
            self.newtestscreen06.place_forget()
        elif which == "1.1":
            self.newtestscreen02.place(x=5, y=5)
            self.newtestscreen01.place_forget()
            self.startscreen.place_forget()
            self.optionsscreen.place_forget()
            self.newtestscreen03.place_forget()
            self.newtestscreen04.place_forget()
            self.newtestscreen05.place_forget()
            self.newtestscreen06.place_forget()
        elif which == "1.2":
            self.newtestscreen03.place(x=5, y=5)
            self.newtestscreen02.place_forget()
            self.newtestscreen01.place_forget()
            self.startscreen.place_forget()
            self.optionsscreen.place_forget()
            self.newtestscreen04.place_forget()
            self.newtestscreen05.place_forget()
            self.newtestscreen06.place_forget()
        elif which == "1.3":
            self.newtestscreen04.place(x=5, y=5)
            self.newtestscreen03.place_forget()
            self.newtestscreen02.place_forget()
            self.newtestscreen01.place_forget()
            self.startscreen.place_forget()
            self.optionsscreen.place_forget()
            self.newtestscreen05.place_forget()
            self.newtestscreen06.place_forget()
        elif which == "1.4":
            self.newtestscreen05.place(x=5, y=5)
            self.newtestscreen04.place_forget()
            self.newtestscreen03.place_forget()
            self.newtestscreen02.place_forget()
            self.newtestscreen01.place_forget()
            self.startscreen.place_forget()
            self.optionsscreen.place_forget()
            self.newtestscreen06.place_forget()
        elif which == "1.5":
            self.newtestscreen06.place(x=5, y=5)
            self.newtestscreen05.place_forget()
            self.newtestscreen04.place_forget()
            self.newtestscreen03.place_forget()
            self.newtestscreen02.place_forget()
            self.newtestscreen01.place_forget()
            self.startscreen.place_forget()
            self.optionsscreen.place_forget()
        elif which == "2":
            self.optionsscreen.place(x=5, y=5)
            self.startscreen.place_forget()
            self.newtestscreen01.place_forget()
            self.newtestscreen02.place_forget()
            self.newtestscreen03.place_forget()
            self.newtestscreen04.place_forget()
            self.newtestscreen05.place_forget()
            self.newtestscreen06.place_forget()


if __name__ == "__main__":  # when the file this is in is called main then it is run
    GetStartupVariables()  # run GetStartupVariables from sharedVar
    App(GetStartupVariables.name_of_app)
    # calls the App class and passes the sharedVar name_of_app as the attribute "title"
