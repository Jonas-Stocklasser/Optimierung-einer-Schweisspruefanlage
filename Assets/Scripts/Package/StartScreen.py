#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Start Screen ; ID=0

import customtkinter as ctk
import sys
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, \
    pruefstueck_image  # import of shared variables located in the sharedVar-file

window_geometry = GetStartupVariables.window_geometry


class StartScreen(ctk.CTkFrame):  # class for the StartScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          width=window_geometry[0] - 10,
                                          height=window_geometry[1] / 20,
                                          corner_radius=10,
                                          text="Start",
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", 20),
                                          anchor="w")
        self.indicator_bar.place(x=0,
                                 y=0)

        # button frame------------------------------------------------------------
        self.button_frame = ctk.CTkFrame(master=self,  # a frame for the buttons
                                         width=340,
                                         height=320,
                                         corner_radius=30)
        self.button_frame.place(x=30,
                                y=75)

        # new test button------------------------------------------------------------
        self.new_test_button = ctk.CTkButton(master=self.button_frame,
                                             # button to start a new test
                                             width=300,
                                             height=80,
                                             corner_radius=10,
                                             text="Neuer Test",
                                             font=("bold", 40),
                                             command=lambda: self.master.switch_window("1.0"))
        # the command calls the App lasses switch_window function and passes "1" as the "which" attribute
        self.new_test_button.place(x=20,
                                   y=20)

        # options button------------------------------------------------------------
        self.options_button = ctk.CTkButton(master=self.button_frame,
                                            # button to open the OptionsScreen
                                            width=300,
                                            height=80,
                                            corner_radius=10,
                                            text="Optionen",
                                            font=("bold", 40),
                                            command=lambda: self.master.switch_window("3"))
        # the command calls the App lasses switch_window function and passes "3" as the "which" attribute
        self.options_button.place(x=20,
                                  y=120)

        # quit button------------------------------------------------------------
        self.quit_button = ctk.CTkButton(master=self.button_frame,
                                         # button to open the OptionsScreen
                                         width=300,
                                         height=80,
                                         corner_radius=10,
                                         text="Desktop",
                                         font=("bold", 40),
                                         command=lambda: sys.exit(0))
        # the command calls the App lasses switch_window function and passes "3" as the "which" attribute
        self.quit_button.place(x=20,
                               y=220)

        # image frame------------------------------------------------------------
        self.image_frame = ctk.CTkFrame(master=self,  # Frame for the StartScreen image
                                        width=616,
                                        height=364)
        self.image_frame.place(x=630,
                               y=75)

        # image label----------------------------------------
        self.image_label = ctk.CTkLabel(master=self.image_frame,  # StartScreen image
                                        text="",
                                        image=pruefstueck_image)  # Here goes a render of the test object (maybe a gif)
        self.image_label.place(x=20,
                               y=20)
