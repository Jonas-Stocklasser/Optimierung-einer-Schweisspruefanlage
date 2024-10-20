#!/usr/bin/python3
# Date: 18.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 2; ID=1.1

import customtkinter as ctk
import tkcalendar as tkc
import os
from datetime import datetime
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location
from .JsonFunctions import json_writer, json_reader, json_creator


class NewTestScreen02(ctk.CTkFrame):  # class for the NewTestScreen02 window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(GetStartupVariables.window_geometry[0] - 10),
                         height=(GetStartupVariables.window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          width=GetStartupVariables.window_geometry[0] - 70,
                                          height=40,
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 2:" +
                                                " persönliche Daten des Prüflings eingeben"),
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", 20),
                                          anchor="w")
        self.indicator_bar.place(x=0,
                                 y=0)

        # entry frame------------------------------------------------------------
        self.entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                        width=340,
                                        height=360,
                                        corner_radius=20)
        self.entry_frame.place(x=30,
                               y=75)

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         width=40,
                                         height=40,
                                         corner_radius=10,
                                         text="",
                                         anchor="ne",
                                         image=back_arrow_image,
                                         command=lambda: self.master.comfirm_go_back("1.0"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=GetStartupVariables.window_geometry[0] - 65,
                               y=0)

        # first name entry------------------------------------------------------------
        self.first_name_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                   fg_color=GetStartupVariables.color_SET_blue,
                                                   width=100,
                                                   height=40,
                                                   corner_radius=10,
                                                   text="Vorname",
                                                   text_color=GetStartupVariables.text_color_SET,
                                                   font=("bold", 20))
        self.first_name_entry_label.place(x=10,
                                          y=10)

        self.first_name_entry = ctk.CTkEntry(master=self.entry_frame,
                                             placeholder_text="Vorname",
                                             width=250,
                                             height=50,
                                             font=("bold", 20)
                                             )
        self.first_name_entry.place(x=10,
                                    y=60)

        # last name entry------------------------------------------------------------
        self.last_name_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                  fg_color=GetStartupVariables.color_SET_blue,
                                                  width=100,
                                                  height=40,
                                                  corner_radius=10,
                                                  text="Nachname",
                                                  text_color=GetStartupVariables.text_color_SET,
                                                  font=("bold", 20))
        self.last_name_entry_label.place(x=10,
                                         y=130)

        self.last_name_entry = ctk.CTkEntry(master=self.entry_frame,
                                            placeholder_text="Nachname",
                                            width=250,
                                            height=50,
                                            font=("bold", 20)
                                            )
        self.last_name_entry.place(x=10,
                                   y=180)

        # birth date entry------------------------------------------------------------
        self.birth_date_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                   fg_color=GetStartupVariables.color_SET_blue,
                                                   width=100,
                                                   height=40,
                                                   corner_radius=10,
                                                   text="Geburtsdatum",
                                                   text_color=GetStartupVariables.text_color_SET,
                                                   font=("bold", 20))
        self.birth_date_entry_label.place(x=10,
                                          y=250)

        self.birth_date_entry = tkc.DateEntry(master=self.entry_frame,
                                              font=("bold", 20),
                                              date_pattern='dd.mm.yyyy',
                                              year=2000,
                                              month=1,
                                              day=1,
                                              state="readonly")
        self.birth_date_entry.place(x=15,
                                    y=300)
        # save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         width=250,
                                         height=70,
                                         corner_radius=20)
        self.button_frame.place(x=30,
                                y=500)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         width=120,
                                         height=50,
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", 20),
                                         command=self.save_entry_data_examinee)
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
                                             command=self.continue_button_function)
        self.continue_button.place(x=140,
                                   y=10)

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
