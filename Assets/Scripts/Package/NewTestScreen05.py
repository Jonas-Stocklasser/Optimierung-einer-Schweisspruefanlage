#!/usr/bin/python3
# Date: 28.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 5; ID=1.4

import customtkinter as ctk
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location
from .JsonFunctions import json_writer, json_reader


class NewTestScreen05(ctk.CTkFrame):  # class for the NewTestScreen05 window
    def __init__(self, parent, window_geometry):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        font_size = window_geometry[1] / 40

        # Grid configuration
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(tuple(range(1, 80)), weight=10)
        self.grid_columnconfigure(81, weight=3)
        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(tuple(range(1, 60)), weight=10)
        self.grid_rowconfigure(61, weight=4)

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=font_size / 2,
                                          text=("Neuer Test - Schritt 5:" +
                                                " Visuelle Einschätzung vom Prüfer eingeben"),
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", font_size),
                                          anchor="w")
        self.indicator_bar.grid(row=1, column=1, columnspan=77, rowspan=1, sticky="nesw")

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         corner_radius=font_size / 2,
                                         text="",
                                         anchor="center",
                                         image=back_arrow_image,
                                         command=lambda: self.master.confirm_go_back("1.3"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.grid(row=1, column=78, columnspan=2, rowspan=1, sticky="nesw")

        # textbox frame ------------------------------------------------------------
        self.textbox_frame = ctk.CTkFrame(master=self,  # frame for the textbox
                                          corner_radius=font_size)
        self.textbox_frame.grid(row=4, column=2, columnspan=40, rowspan=30, sticky="nesw")

        # textbox ------------------------------------------------------------
        self.textbox = ctk.CTkTextbox(master=self.textbox_frame,
                                      border_width=font_size / 4,
                                      font=("bold", font_size),
                                      corner_radius=font_size / 2)
        self.textbox.place(relx=0.01,
                           rely=0.01)

        # save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=font_size / 2)
        self.button_frame.grid(row=40, column=2, columnspan=13, rowspan=2, sticky="nesw")

        self.button_frame.grid_columnconfigure(0, weight=3)
        self.button_frame.grid_columnconfigure(1, weight=20)
        self.button_frame.grid_columnconfigure(2, weight=3)
        self.button_frame.grid_columnconfigure(3, weight=20)
        self.button_frame.grid_columnconfigure(4, weight=3)
        self.button_frame.grid_rowconfigure(0, weight=3)
        self.button_frame.grid_rowconfigure(1, weight=10)
        self.button_frame.grid_rowconfigure(2, weight=3)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         corner_radius=font_size / 2,
                                         text="Speichern",
                                         font=("bold", font_size),
                                         state="normal",
                                         command=lambda: self.save_textbox_data())
        self.save_button.grid(row=1, column=1, columnspan=1, rowspan=1, sticky="nesw")

        self.continue_button = ctk.CTkButton(master=self.button_frame,
                                             # continue button
                                             corner_radius=font_size / 2,
                                             text="Weiter",
                                             font=("bold", font_size),
                                             state="disabled",
                                             command=lambda: self.master.switch_window("1.5"))
        self.continue_button.grid(row=1, column=3, columnspan=1, rowspan=1, sticky="nesw")

    def save_textbox_data(self):
        visual_grade = self.textbox.get("1.0", "end")

        if visual_grade != "\n":
            self.continue_button.configure(state="normal")
            personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
            personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
            json_writer(personal_json_name, "visual_grade", visual_grade, personal_folder_path)
        else:
            print("Type something! An empty field is not permitted!")

    def update_size(self, font_size):
        self.indicator_bar.configure(font=("bold", font_size), height=font_size, corner_radius=font_size / 2)
        self.back_button.configure(width=font_size,
                                   height=font_size, corner_radius=font_size / 2)
        back_arrow_image.configure(size=(font_size, font_size))
        self.textbox_frame.configure(height=font_size * 3 * 7.5, width=font_size * 4 * 7.5, corner_radius=font_size)
        self.textbox.configure(font=("bold", font_size), height=font_size * 3 * 9.7, width=font_size * 4 * 10,
                               corner_radius=font_size / 2, border_width=font_size / 4)

        self.button_frame.configure(height=font_size * 2, corner_radius=font_size / 2)
        self.save_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4,
                                   corner_radius=font_size / 2)
        self.continue_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4,
                                       corner_radius=font_size / 2)
