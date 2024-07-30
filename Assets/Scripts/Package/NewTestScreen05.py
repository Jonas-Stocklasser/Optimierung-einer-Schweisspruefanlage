#!/usr/bin/python3
# Date: 28.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 5; ID=1.4

import customtkinter as ctk
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image
from .JsonFunctions import json_writer, json_reader


class NewTestScreen05(ctk.CTkFrame):  # class for the NewTestScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(GetStartupVariables.window_geometry[0] - 10),
                         height=(GetStartupVariables.window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   y=5)

        # top bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          width=GetStartupVariables.window_geometry[0] - 70,
                                          height=40,
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 5:" +
                                                " Visuelle Einschätzung vom Prüfer eingeben"),
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", 20),
                                          anchor="w")
        self.indicator_bar.place(x=0,
                                 y=0)

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         width=40,
                                         height=40,
                                         corner_radius=10,
                                         text="",
                                         anchor="ne",
                                         image=back_arrow_image,
                                         command=lambda: self.master.open_top_level_window_really_switch(
                                             "1.3"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=GetStartupVariables.window_geometry[0] - 65,
                               y=0)

        # textbox frame ------------------------------------------------------------
        self.textbox_frame = ctk.CTkFrame(master=self,  # frame for the textbox
                                          width=910,
                                          height=455,
                                          corner_radius=20)
        self.textbox_frame.place(x=30,
                                 y=80)

        # textbox ------------------------------------------------------------

        self.textbox = ctk.CTkTextbox(master=self.textbox_frame,
                                      width=890,
                                      height=435,
                                      border_width=5,
                                      font=("bold", 20),
                                      corner_radius=10)
        self.textbox.place(x=10,
                           y=10)

        # save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         width=250,
                                         height=70,
                                         corner_radius=20)
        self.button_frame.place(x=30,
                                y=570)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         width=120,
                                         height=50,
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", 20),
                                         state="normal",
                                         command=lambda: self.save_textbox_data())
        self.save_button.place(x=10,
                               y=10)

        self.continue_button = ctk.CTkButton(master=self.button_frame,
                                             # continue button
                                             width=100,
                                             height=50,
                                             corner_radius=10,
                                             text="Weiter",
                                             font=("bold", 20),
                                             state="disabled",
                                             command=lambda: self.master.switch_window("1.5"))
        self.continue_button.place(x=140,
                                   y=10)

    def save_textbox_data(self):
        self.continue_button.configure(state="normal")
        self.save_button.configure(state="disabled")
        visual_grade = self.textbox.get("1.0", "end")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", "../Other/")
        personal_json_name = json_reader("personal_var", "personal_json_name", "../Other/")
        json_writer(personal_json_name, "visual_grade", visual_grade, personal_folder_path)
