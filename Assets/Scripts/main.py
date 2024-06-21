#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage

import customtkinter as ctk
import pandas as pd

from Package.StartScreen import StartScreen  # imports of other files of the package
from Package.OptionsScreen import OptionsScreen
from Package.ReallySwitch import ReallySwitch
# Shared variables----------------------------------------
from Package.sharedVar import window_geometry, name_of_app, \
    start_window, GetStartupVariables, appearance_mode  # import of shared variables located in the sharedVar file


class App(ctk.CTk):  # main window class, every other window class is called from here
    def __init__(self, title):  # title is given as an attribute from the class call
        # main initialization----------------------------------------
        super().__init__()
        ctk.set_appearance_mode(appearance_mode[0])
        ctk.set_default_color_theme("blue")
        self.title(title)
        self.geometry(f"{window_geometry[0]}x{window_geometry[1]}")
        self.resizable(False, False)

        # windows----------------------------------------
        self.startscreen = StartScreen(self)  # ID = 0      other classes
        # self.newtestscreen = NewTestScreen(self)  # ID = 1
        self.optionsscreen = OptionsScreen(self)  # ID = 2

        # top level windows----------------------------------------
        self.reallyswitch = None

        # show start screen initially----------------------------------------
        self.switch_window(start_window)

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
        elif which == "1":
            self.startscreen.place_forget()
            self.optionsscreen.place_forget()
        elif which == "2":
            self.startscreen.place_forget()
            self.optionsscreen.place(x=5, y=5)

    # Function for changing appearance mode----------------------------------------
    def appearance_mode_switch(self, mode):  # method for switching the appearance mode to dark/light mode
        ctk.set_appearance_mode(mode)  # the attribute "mode" is given by the menu widget in the OptionsScreen class
        data = pd.read_json("../Other/startup_var.json", encoding="latin1")
        if mode == "light":
            index = data.index[data['var'] == "appearance_mode"].tolist()
            data.at[index[0], 'val'] = ["light", "dark"]
            with open("../Other/startup_var.json", "w") as file:
                data.to_json(file, orient="records", indent=2)
        elif mode == "dark":
            index = data.index[data['var'] == "appearance_mode"].tolist()
            data.at[index[0], 'val'] = ["dark", "light"]
            with open("../Other/startup_var.json", "w") as file:
                data.to_json(file, orient="records", indent=2)

    def window_size_switch(self, size):
        print("Neustart fuer Aenderung erforderlich")
        data = pd.read_json("../Other/startup_var.json", encoding="latin1")
        if size == "HD":
            index = data.index[data['var'] == "window_geometry"].tolist()
            data.at[index[0], 'val'] = [1280, 720]
            index = data.index[data['var'] == "window_size"].tolist()
            data.at[index[0], 'val'] = ["HD", "FullHD"]
            with open("../Other/startup_var.json", "w") as file:
                data.to_json(file, orient="records", indent=2)


        elif size == "FullHD":
            index = data.index[data['var'] == "window_geometry"].tolist()
            data.at[index[0], 'val'] = [1920, 1080]
            index = data.index[data['var'] == "window_size"].tolist()
            data.at[index[0], 'val'] = ["FullHD", "HD"]
            with open("../Other/startup_var.json", "w") as file:
                data.to_json(file, orient="records", indent=2)


if __name__ == "__main__":  # when the file this is in is called main then it is run
    GetStartupVariables()  # run GetStartupVariables from sharedVar
    App(name_of_app)  # calls the App class and passes the sharedVar name_of_app as the attribute "title"
