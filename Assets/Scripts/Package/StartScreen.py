#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# StartFenster

import customtkinter as ctk
# Shared variables----------------------------------------
from .sharedVar import window_geometry, colorSET, text_colorSET, \
    start_image  # import of shared variables located in the sharedVar file


class StartScreen(ctk.CTkFrame):  # class for the StartScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")
        self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   y=5)

        # calling the create_widgets method to create all widgets that are children of StartScreen
        self.create_widgets()

    def create_widgets(self):
        # top bar------------------------------------------------------------
        startscreen_indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                                 fg_color=colorSET,
                                                 width=window_geometry[0] - 10,
                                                 height=40,
                                                 corner_radius=10,
                                                 text="Start",
                                                 text_color=text_colorSET,
                                                 font=("bold", 20),
                                                 anchor="w")
        startscreen_indicator_bar.place(x=0,
                                        y=0)

        # button frame------------------------------------------------------------
        startscreen_button_frame = ctk.CTkFrame(master=self,  # a frame for the buttons
                                                width=340,
                                                height=220)
        startscreen_button_frame.place(x=30,
                                       y=(window_geometry[1] / 2) - 280)

        # new test button------------------------------------------------------------
        startscreen_new_test_button = ctk.CTkButton(master=startscreen_button_frame,  # button to start a new test
                                                    width=300,
                                                    height=80,
                                                    corner_radius=10,
                                                    text="Neuer Test",
                                                    font=("bold", 40),
                                                    command=lambda: self.master.switch_window("1"))
        # the command calls the App lasses switch_window function and passes "1" as the "which" attribute
        startscreen_new_test_button.place(x=20,
                                          y=20)

        # options button------------------------------------------------------------
        startscreen_options_button = ctk.CTkButton(master=startscreen_button_frame,  # button to open the OptionsScreen
                                                   width=300,
                                                   height=80,
                                                   corner_radius=10,
                                                   text="Options",
                                                   font=("bold", 40),
                                                   command=lambda: self.master.switch_window("2"))
        # the command calls the App lasses switch_window function and passes "3" as the "which" attribute
        startscreen_options_button.place(x=20,
                                         y=120)

        # image frame------------------------------------------------------------
        startscreen_image_frame = ctk.CTkFrame(master=self,  # Frame for the StartScreen image
                                               width=600,
                                               height=600)
        startscreen_image_frame.place(x=640,
                                      y=(window_geometry[1] / 2) - 280)

        # image label----------------------------------------
        image_label = ctk.CTkLabel(master=startscreen_image_frame,  # StartScreen image
                                   text="",
                                   image=start_image)  # Here goes a render of the test object (maybe a gif)
        image_label.place(x=0,
                          y=0)
