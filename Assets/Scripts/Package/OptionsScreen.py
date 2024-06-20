#!/usr/bin/python3
# Date: 09.02.24
# Author: Stocklasser
# DA Ideas
#

import customtkinter as ctk
# Shared variables----------------------------------------
from .sharedVar import window_geometry, color_SET, text_color_SET, \
    back_arrow_image, appearance_mode


class OptionsScreen(ctk.CTkFrame):  # class for the OptionsScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")
        self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   y=5)

        # calling the create_widgets method to create all widgets that are children of OptionsScreen
        self.create_widgets()

    def create_widgets(self):
        # top bar------------------------------------------------------------
        optionsscreen_indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                                   fg_color=color_SET,
                                                   width=window_geometry[0] - 70,
                                                   height=40,
                                                   corner_radius=10,
                                                   text="Options - Screen",
                                                   text_color=text_color_SET,
                                                   font=("bold", 20),
                                                   anchor="w")
        optionsscreen_indicator_bar.place(x=0,
                                          y=0)

        # button frame------------------------------------------------------------
        optionsscreen_button_frame = ctk.CTkFrame(master=self,  # frame for the buttons and the menu
                                                  width=340,
                                                  height=80)
        optionsscreen_button_frame.place(x=450,
                                         y=(window_geometry[1] / 2) - 280)

        # back button------------------------------------------------------------
        optionsscreen_back_button = ctk.CTkButton(master=self,  # back button
                                                  width=40,
                                                  height=40,
                                                  corner_radius=10,
                                                  text="",
                                                  image=back_arrow_image,
                                                  command=lambda: self.master.switch_window("0"))
        # the command doesn't call the switch_window method because there is no unsaved content to loose
        optionsscreen_back_button.place(x=1215,
                                        y=0)

        # light mode / dark mode ------------------------------------------------------------
        # option menu
        options_light_dark_menu = ctk.CTkOptionMenu(master=optionsscreen_button_frame,  # menu for light / dark
                                                    width=100,
                                                    height=40,
                                                    font=("bold", 20),
                                                    dropdown_font=("bold", 20),
                                                    corner_radius=5,
                                                    values=appearance_mode,
                                                    command=self.master.appearance_mode_switch)
        # the command automatically passes the current value as an argument to the specified method
        options_light_dark_menu.place(x=220,
                                      y=20)
        # label
        options_light_dark_label = ctk.CTkLabel(master=optionsscreen_button_frame,  # label to describe the menu above
                                                fg_color=color_SET,
                                                width=180,
                                                height=40,
                                                corner_radius=5,
                                                text="Appearance mode",
                                                text_color=text_color_SET,
                                                font=("bold", 20))
        options_light_dark_label.place(x=20,
                                       y=20)
