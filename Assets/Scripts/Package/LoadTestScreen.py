#!/usr/bin/python3
# Date: 09.02.24
# Author: Stocklasser
# DA Ideas
#

import customtkinter as ctk
# Shared variables----------------------------------------
from .sharedVar import geometry, colorSET, text_colorSET, \
    back_button_image  # import of shared variables located in the sharedVar file


class LoadTestScreen(ctk.CTkFrame):  # class for the LoadTestScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(geometry[0] - 10),
                         height=(geometry[1] - 10),
                         fg_color="transparent")
        self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   y=5)

        # calling the create_widgets method to create all widgets that are children of LoadTestScreen
        self.create_widgets()

    def create_widgets(self):
        # top bar------------------------------------------------------------
        loadtestscreen_indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                                    fg_color=colorSET,
                                                    width=geometry[0] - 70,
                                                    height=40,
                                                    corner_radius=10,
                                                    text="Load Test - Screen",
                                                    text_color=text_colorSET,
                                                    font=("bold", 20),
                                                    anchor="w")
        loadtestscreen_indicator_bar.place(x=0,
                                           y=0)

        # back button------------------------------------------------------------
        loadtestscreen_back_button = ctk.CTkButton(master=self,  # button to go back
                                                   width=40,
                                                   height=40,
                                                   corner_radius=10,
                                                   text="",
                                                   image=back_button_image,
                                                   command=lambda: self.master.open_top_level_window_really_switch("0"))
        # the command opens the top level window class "ReallySwitch" and passes "0" as the argument "which"
        loadtestscreen_back_button.place(x=1215,
                                         y=0)
