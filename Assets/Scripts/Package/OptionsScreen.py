#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# OptionenFenster; ID = 3

import customtkinter as ctk
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location
from .JsonFunctions import json_writer

window_geometry = GetStartupVariables.window_geometry
font_size = window_geometry[1] / 40

class OptionsScreen(ctk.CTkFrame):  # class for the OptionsScreen window
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
                                          text="Options",
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", font_size),
                                          anchor="w")
        self.indicator_bar.grid(row=1, column=1, columnspan=77, rowspan=1, sticky="nesw")

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         corner_radius=10,
                                         text="",
                                         anchor="center",
                                         image=back_arrow_image,
                                         command=lambda: self.master.switch_window("0"))
        # the command doesn't call the switch_window method because there is no unsaved content to loose
        self.back_button.grid(row=1, column=78, columnspan=2, rowspan=1, sticky="nesw")

        # button frame------------------------------------------------------------
        self.button_frame = ctk.CTkFrame(master=self,  # frame for the buttons and the menu
                                         corner_radius=20)
        self.button_frame.grid(row=4, column=2, columnspan=15, rowspan=4, sticky="nesw")

        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=5)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)
        self.button_frame.grid_columnconfigure(4, weight=5)
        self.button_frame.grid_columnconfigure(5, weight=1)
        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_rowconfigure(1, weight=5)
        self.button_frame.grid_rowconfigure(2, weight=1)
        # light mode / dark mode ------------------------------------------------------------
        # label
        self.options_light_dark_label = ctk.CTkLabel(master=self.button_frame,
                                                     # label to describe the menu above
                                                     fg_color=GetStartupVariables.color_SET_blue,
                                                     corner_radius=10,
                                                     text="Anzeigemodus",
                                                     text_color=GetStartupVariables.text_color_SET,
                                                     font=("bold", 20))
        self.options_light_dark_label.grid(row=1, column=1, columnspan=1, rowspan=1, sticky="nesw")

        # option menu
        self.options_light_dark_menu = ctk.CTkOptionMenu(master=self.button_frame,
                                                         # menu for light / dark
                                                         font=("bold", 20),
                                                         dropdown_font=("bold", 20),
                                                         corner_radius=10,
                                                         values=GetStartupVariables.appearance_mode,
                                                         command=self.appearance_mode_switch)
        # the command automatically passes the current value as an argument to the specified method
        self.options_light_dark_menu.grid(row=1, column=4, columnspan=1, rowspan=1, sticky="new")


    @staticmethod
    def appearance_mode_switch(mode):  # method for switching the appearance mode to dark/light mode
        if mode == "light":
            json_writer("startup_var", "appearance_mode", ["light", "dark"], main_pi_location + "../JSON/")

        elif mode == "dark":
            json_writer("startup_var", "appearance_mode", ["dark", "light"], main_pi_location + "../JSON/")


    def update_font_size(self, font_size):
        self.indicator_bar.configure(font=("bold", font_size), height=font_size)
        self.back_button.configure(width=font_size,
                                   height=font_size)
        back_arrow_image.configure(size=(font_size, font_size))
        self.options_light_dark_label.configure(font=("bold", font_size))
        self.options_light_dark_menu.configure(font=("bold", font_size), dropdown_font=("bold", font_size))

