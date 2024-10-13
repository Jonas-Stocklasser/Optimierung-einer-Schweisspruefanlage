#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# OptionenFenster; ID = 3

import customtkinter as ctk
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location
from .JsonFunctions import json_writer


class OptionsScreen(ctk.CTkFrame):  # class for the OptionsScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(GetStartupVariables.window_geometry[0] - 10),
                         height=(GetStartupVariables.window_geometry[1] - 10),
                         fg_color="transparent")
        # self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   # y=5)

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          width=GetStartupVariables.window_geometry[0] - 70,
                                          height=40,
                                          corner_radius=10,
                                          text="Optionen",
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", 20),
                                          anchor="w")
        self.indicator_bar.place(x=0,
                                 y=0)

        # button frame------------------------------------------------------------
        self.button_frame = ctk.CTkFrame(master=self,  # frame for the buttons and the menu
                                         width=470,
                                         height=130,
                                         corner_radius=20)
        self.button_frame.place(x=30,
                                y=75)

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         width=40,
                                         height=40,
                                         corner_radius=10,
                                         text="",
                                         anchor="ne",
                                         image=back_arrow_image,
                                         command=lambda: self.master.switch_window("0"))
        # the command doesn't call the switch_window method because there is no unsaved content to loose
        self.back_button.place(x=GetStartupVariables.window_geometry[0] - 65,
                               y=0)

        # light mode / dark mode ------------------------------------------------------------
        # option menu
        self.options_light_dark_menu = ctk.CTkOptionMenu(master=self.button_frame,
                                                         # menu for light / dark
                                                         width=100,
                                                         height=40,
                                                         font=("bold", 20),
                                                         dropdown_font=("bold", 20),
                                                         corner_radius=5,
                                                         values=GetStartupVariables.appearance_mode,
                                                         command=self.appearance_mode_switch)
        # the command automatically passes the current value as an argument to the specified method
        self.options_light_dark_menu.place(x=220,
                                           y=20)
        # label
        self.options_light_dark_label = ctk.CTkLabel(master=self.button_frame,
                                                     # label to describe the menu above
                                                     fg_color=GetStartupVariables.color_SET_blue,
                                                     width=180,
                                                     height=40,
                                                     corner_radius=5,
                                                     text="Anzeigemodus",
                                                     text_color=GetStartupVariables.text_color_SET,
                                                     font=("bold", 20))
        self.options_light_dark_label.place(x=20,
                                            y=20)

        # Window size ------------------------------------------------------------
        # option menu
        self.options_window_size_menu = ctk.CTkOptionMenu(master=self.button_frame,
                                                          width=100,
                                                          height=40,
                                                          font=("bold", 20),
                                                          dropdown_font=("bold", 20),
                                                          corner_radius=5,
                                                          values=GetStartupVariables.window_size,
                                                          command=self.window_size_switch)
        # the command automatically passes the current value as an argument to the specified method
        self.options_window_size_menu.place(x=220,
                                            y=70)
        # label
        self.options_window_size_label = ctk.CTkLabel(master=self.button_frame,
                                                      # label to describe the menu above
                                                      fg_color=GetStartupVariables.color_SET_blue,
                                                      width=180,
                                                      height=40,
                                                      corner_radius=5,
                                                      text="Fenstergröße",
                                                      text_color=GetStartupVariables.text_color_SET,
                                                      font=("bold", 20))
        self.options_window_size_label.place(x=20,
                                             y=70)

        # Function for changing appearance mode----------------------------------------

    @staticmethod
    def appearance_mode_switch(mode):  # method for switching the appearance mode to dark/light mode
        ctk.set_appearance_mode(mode)  # the attribute "mode" is given by the menu widget in the OptionsScreen class
        if mode == "light":
            json_writer("startup_var", "appearance_mode", ["light", "dark"], main_pi_location + "../JSON/")

        elif mode == "dark":
            json_writer("startup_var", "appearance_mode", ["dark", "light"], main_pi_location + "../JSON/")

    @staticmethod
    def window_size_switch(size):
        print("Neustart für Änderung erforderlich")
        if size == "HD - 1280x720":
            json_writer("startup_var", "window_geometry", [1280, 720], main_pi_location + "../JSON/")
            json_writer("startup_var", "window_size", ["HD - 1280x720", "FullHD - 1920x1080"],
                        main_pi_location + "../JSON/")

        elif size == "FullHD - 1920x1080":
            json_writer("startup_var", "window_geometry", [1920, 1080], main_pi_location + "../JSON/")
            json_writer("startup_var", "window_size", ["FullHD - 1920x1080", "HD - 1280x720"],
                        main_pi_location + "../JSON/")
