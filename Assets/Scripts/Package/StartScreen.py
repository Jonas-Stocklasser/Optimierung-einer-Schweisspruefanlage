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
font_size = window_geometry[1] / 40


class StartScreen(ctk.CTkFrame):  # class for the StartScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         fg_color="transparent")

        # Grid configuration
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(tuple(range(1, 80)), weight=10)
        self.grid_columnconfigure(81, weight=3)
        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(tuple(range(1, 60)), weight=10)
        self.grid_rowconfigure(61, weight=4)

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=10,
                                          text="Start",
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", font_size),
                                          anchor="w")
        self.indicator_bar.grid(row=1, column=1, columnspan=80, rowspan=1, sticky="nesw")

        # button frame------------------------------------------------------------
        self.button_frame = ctk.CTkFrame(master=self,  # a frame for the buttons
                                         corner_radius=20)
        self.button_frame.grid(row=4, column=2, columnspan=15, rowspan=20, sticky="nesw")

        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=5)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=5)
        self.button_frame.grid_columnconfigure(4, weight=1)
        self.button_frame.grid_columnconfigure(5, weight=5)
        self.button_frame.grid_columnconfigure(6, weight=1)
        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_rowconfigure(1, weight=5)
        self.button_frame.grid_rowconfigure(2, weight=1)
        self.button_frame.grid_rowconfigure(3, weight=5)
        self.button_frame.grid_rowconfigure(4, weight=1)
        self.button_frame.grid_rowconfigure(5, weight=5)
        self.button_frame.grid_rowconfigure(6, weight=1)

        # new test button------------------------------------------------------------
        self.new_test_button = ctk.CTkButton(master=self.button_frame,
                                             # button to start a new test
                                             corner_radius=10,
                                             text="Neuer Test",
                                             font=("bold", font_size*2),
                                             command=lambda: self.master.switch_window("1.0"))
        # the command calls the App lasses switch_window function and passes "1" as the "which" attribute
        self.new_test_button.grid(row=1, column=1, columnspan=5, rowspan=1, sticky="nesw")

        # options button------------------------------------------------------------
        self.options_button = ctk.CTkButton(master=self.button_frame,
                                            # button to open the OptionsScreen
                                            corner_radius=10,
                                            text="Optionen",
                                            font=("bold", font_size*2),
                                            command=lambda: self.master.switch_window("3"))
        # the command calls the App lasses switch_window function and passes "3" as the "which" attribute
        self.options_button.grid(row=3, column=1, columnspan=5, rowspan=1, sticky="nesw")

        # quit button------------------------------------------------------------
        self.quit_button = ctk.CTkButton(master=self.button_frame,
                                         # button to open the OptionsScreen
                                         corner_radius=10,
                                         text="Desktop",
                                         font=("bold", font_size*2),
                                         command=lambda: sys.exit(0))
        self.quit_button.grid(row=5, column=1, columnspan=5, rowspan=1, sticky="nesw")

        # image frame------------------------------------------------------------
        self.image_frame = ctk.CTkFrame(master=self)  # Frame for the StartScreen image
        self.image_frame.grid(row=4, column=30, columnspan=40, rowspan=15, sticky="nesw")

        # image label----------------------------------------
        self.image_label = ctk.CTkLabel(master=self.image_frame,  # StartScreen image
                                        text="",
                                        image=pruefstueck_image)  # Here goes a render of the test object (maybe a gif)
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")

    def update_size(self, font_size):
        self.indicator_bar.configure(font=("bold", font_size), height=font_size)
        self.new_test_button.configure(font=("bold", 2*font_size), height=font_size * 2.5, width=font_size * 4)
        self.options_button.configure(font=("bold", 2*font_size), height=font_size * 2.5, width=font_size * 4)
        self.quit_button.configure(font=("bold", 2*font_size), height=font_size * 2.5, width=font_size * 4)
        pruefstueck_image.configure(size=(font_size*16*1.5, font_size*9*1.5))
