#!/usr/bin/python3
# Date: 09.02.24
# Author: Stocklasser
# DA Ideas
#

import customtkinter as ctk
# Shared variables----------------------------------------
from .sharedVar import colorSET, text_colorSET  # import of shared variables located in the sharedVar file


class ReallySwitch(ctk.CTkToplevel):  # top level window class for checking if you really want to go back
    def __init__(self, parent, which):
        # the attribute "which" is passed on to the widgets and from there to the window switch method in the app class
        super().__init__(parent)
        self.geometry("350x150")
        self.resizable(False, False)
        self.title("!ACHTUNG!")
        self.attributes("-topmost", "true")  # the window is at the top at all times

        # calling the create_widgets method to create all widgets that are children of ReallySwitch and passing "which"
        self.create_widgets(which)

    def create_widgets(self, which):
        # top bar------------------------------------------------------------
        top_level_indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                               fg_color=colorSET,
                                               width=340,
                                               height=20,
                                               corner_radius=5,
                                               text="Wirklich zurück gehen?",
                                               text_color=text_colorSET,
                                               font=("bold", 15))
        top_level_indicator_bar.place(x=5,
                                      y=5)

        # button frame------------------------------------------------------------
        top_level_button_frame = ctk.CTkFrame(master=self,  # frame for the buttons
                                              width=340,
                                              height=115)
        top_level_button_frame.place(x=5,
                                     y=30)

        # yes button------------------------------------------------------------
        startscreen_yes_button = ctk.CTkButton(master=top_level_button_frame,  # yes button to continue going back
                                               width=100,
                                               height=50,
                                               corner_radius=10,
                                               text="Ja",
                                               font=("bold", 20),
                                               command=lambda: (self.master.switch_window(which), self.destroy()))
        # the command call the switch_window method and passes "which" as an argument, then destroys itself
        startscreen_yes_button.place(x=5,
                                     y=32.5)

        # no button------------------------------------------------------------
        startscreen_no_button = ctk.CTkButton(master=top_level_button_frame,  # no button for canceling going back
                                              width=100,
                                              height=50,
                                              corner_radius=10,
                                              text="Nein",
                                              font=("bold", 20),
                                              command=lambda: self.destroy())  # the command destroys the window
        startscreen_no_button.place(x=235,
                                    y=32.5)
