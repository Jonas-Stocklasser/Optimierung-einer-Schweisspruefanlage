#!/usr/bin/python3
# Date: 18.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 2; ID=1.1

import customtkinter as ctk
import tkcalendar as tkc
import math
import os
from datetime import datetime
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location
from .JsonFunctions import json_writer, json_reader, json_creator

window_geometry = GetStartupVariables.window_geometry
font_size = window_geometry[1] / 40


class NewTestScreen02(ctk.CTkFrame):  # class for the NewTestScreen02 window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

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
                                          text=("Neuer Test - Schritt 2:" +
                                                " persönliche Daten des Prüflings eingeben"),
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
                                         command=lambda: self.master.confirm_go_back("1.0"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.grid(row=1, column=78, columnspan=2, rowspan=1, sticky="nesw")

        # entry frame------------------------------------------------------------
        self.entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                        corner_radius=font_size)
        self.entry_frame.grid(row=4, column=2, columnspan=10, rowspan=15, sticky="nesw")

        # Grid configuration
        self.entry_frame.grid_columnconfigure(0, weight=10)
        self.entry_frame.grid_columnconfigure(tuple(range(1, 80)), weight=10)
        self.entry_frame.grid_columnconfigure(81, weight=10)
        self.entry_frame.grid_rowconfigure(0, weight=4)
        self.entry_frame.grid_rowconfigure(tuple(range(1, 49)), weight=10)
        self.entry_frame.grid_rowconfigure(50, weight=4)

        # first name entry------------------------------------------------------------
        self.first_name_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                   fg_color=GetStartupVariables.color_SET_blue,
                                                   corner_radius=font_size / 2,
                                                   text="Vorname",
                                                   text_color=GetStartupVariables.text_color_SET,
                                                   font=("bold", font_size))
        self.first_name_entry_label.grid(row=5, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.first_name_entry = ctk.CTkEntry(master=self.entry_frame,
                                             placeholder_text="Vorname",
                                             font=("bold", font_size)
                                             )
        self.first_name_entry.grid(row=10, column=20, columnspan=2, rowspan=1, sticky="nesw")

        # last name entry------------------------------------------------------------
        self.last_name_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                  fg_color=GetStartupVariables.color_SET_blue,
                                                  corner_radius=font_size / 2,
                                                  text="Nachname",
                                                  text_color=GetStartupVariables.text_color_SET,
                                                  font=("bold", font_size))
        self.last_name_entry_label.grid(row=22, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.last_name_entry = ctk.CTkEntry(master=self.entry_frame,
                                            placeholder_text="Nachname",
                                            font=("bold", font_size)
                                            )
        self.last_name_entry.grid(row=27, column=20, columnspan=2, rowspan=1, sticky="nesw")

        # birth date entry------------------------------------------------------------
        self.birth_date_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                   fg_color=GetStartupVariables.color_SET_blue,
                                                   corner_radius=font_size / 2,
                                                   text="Geburtsdatum",
                                                   text_color=GetStartupVariables.text_color_SET,
                                                   font=("bold", font_size))
        self.birth_date_entry_label.grid(row=39, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.birth_date_entry = tkc.DateEntry(master=self.entry_frame,
                                              font=("bold", math.ceil(font_size)),
                                              date_pattern='dd.mm.yyyy',
                                              year=2000,
                                              month=1,
                                              day=1,
                                              state="readonly")
        self.birth_date_entry.grid(row=44, column=20, columnspan=2, rowspan=1, sticky="nesw")
        # save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=font_size / 2)
        self.button_frame.grid(row=20, column=2, columnspan=13, rowspan=2, sticky="nesw")

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
                                         command=self.save_entry_data_examinee)
        self.save_button.grid(row=1, column=1, columnspan=1, rowspan=1, sticky="nesw")

        self.continue_button = ctk.CTkButton(master=self.button_frame,
                                             # continue button
                                             corner_radius=font_size / 2,
                                             text="Weiter",
                                             font=("bold", font_size),
                                             state="disabled",
                                             command=self.continue_button_function)
        self.continue_button.grid(row=1, column=3, columnspan=1, rowspan=1, sticky="nesw")

    def continue_button_function(self):  # method for the button actions
        self.master.switch_window("1.2")
        self.create_examinee_folder_and_json()

    def save_entry_data_examinee(self):  # method to save the entry data
        personal_infos_examinee = [self.first_name_entry.get(),
                                   self.last_name_entry.get(),
                                   self.birth_date_entry.get()]
        if len(personal_infos_examinee[0].strip()) + len(
                personal_infos_examinee[1].strip()) >= 4:  # integrity evaluation
            self.continue_button.configure(state="normal")  # unlock the continue button
            json_writer("personal_var", "personal_infos_examinee", personal_infos_examinee,
                        main_pi_location + "../JSON/")
        else:
            self.continue_button.configure(state="disabled")  # lock the continue button
            print("Sum of first name plus surname not at least 4 digits")

    @staticmethod
    def create_examinee_folder_and_json():  # create a new folder for all the created files for the examinee
        personal_infos_examinee = json_reader("personal_var", "personal_infos_examinee", main_pi_location + "../JSON/")
        exam_date = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"
        error_append = ""
        error_num = 0
        save_path = json_reader("startup_var", "save_path", main_pi_location + "../JSON/")
        new_folder = f"{save_path}/{personal_infos_examinee[1]}_{personal_infos_examinee[0]}" + error_append
        while True:
            try:
                os.mkdir(new_folder)
                break
            except FileExistsError:
                error_num += 1
                error_append = str(error_num)
                new_folder = f"{save_path}/{personal_infos_examinee[1]}_{personal_infos_examinee[0]}{error_append}"

        json_creator(f"{personal_infos_examinee[1]}_{personal_infos_examinee[0]}", f"{new_folder}/",
                     "personal_infos_examinee", personal_infos_examinee)
        json_writer("personal_var", "personal_folder_path",
                    f"{new_folder}/", main_pi_location + "../JSON/")
        json_writer("personal_var", "personal_json_name",
                    f"{personal_infos_examinee[1]}_{personal_infos_examinee[0]}", main_pi_location + "../JSON/")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
        json_writer(personal_json_name, "exam_date", exam_date, personal_folder_path)

    def update_size(self, font_size):
        self.indicator_bar.configure(font=("bold", font_size), height=font_size)
        self.back_button.configure(width=font_size,
                                   height=font_size)
        back_arrow_image.configure(size=(font_size, font_size))
        self.first_name_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5,
                                              corner_radius=font_size / 2)
        self.first_name_entry.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 10,
                                        corner_radius=font_size / 2)
        self.last_name_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5,
                                             corner_radius=font_size / 2)
        self.last_name_entry.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 10,
                                       corner_radius=font_size / 2)
        self.birth_date_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5,
                                              corner_radius=font_size / 2)
        self.birth_date_entry.configure(font=("bold", math.ceil(font_size) - 4))

        self.button_frame.configure(height=font_size * 2, corner_radius=font_size / 2)
        self.save_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4,
                                   corner_radius=font_size / 2)
        self.continue_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4,
                                       corner_radius=font_size / 2)
