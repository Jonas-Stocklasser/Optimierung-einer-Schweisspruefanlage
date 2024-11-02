#!/usr/bin/python3
# Date: 21.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 3; ID=1.2

import customtkinter as ctk
import tkinter as tk
import math
import tkcalendar as tkc
from .JsonFunctions import json_reader, json_writer
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetPersonalVariables, back_arrow_image, main_pi_location

window_geometry = GetStartupVariables.window_geometry
font_size = window_geometry[1] / 40


class NewTestScreen03(ctk.CTkFrame):  # class for the NewTestScreen03 window
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
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 3:" +
                                                " persönliche Daten des Prüfers eingeben"),
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
                                         command=lambda: self.master.confirm_go_back("1.1"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.grid(row=1, column=78, columnspan=2, rowspan=1, sticky="nesw")

        # option menu examiner------------------------------------------------------------
        self.examiner_option_menu_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                       corner_radius=10)
        self.examiner_option_menu_frame.grid(row=4, column=2, columnspan=15, rowspan=2, sticky="nesw")

        # Grid configuration
        self.examiner_option_menu_frame.grid_columnconfigure(0, weight=3)
        self.examiner_option_menu_frame.grid_columnconfigure(1, weight=20)
        self.examiner_option_menu_frame.grid_columnconfigure(2, weight=3)
        self.examiner_option_menu_frame.grid_columnconfigure(3, weight=20)
        self.examiner_option_menu_frame.grid_columnconfigure(4, weight=3)
        self.examiner_option_menu_frame.grid_rowconfigure(0, weight=3)
        self.examiner_option_menu_frame.grid_rowconfigure(1, weight=10)
        self.examiner_option_menu_frame.grid_rowconfigure(2, weight=3)

        self.examiner_option_menu_label = ctk.CTkLabel(
            master=self.examiner_option_menu_frame,
            fg_color=GetStartupVariables.color_SET_blue,
            corner_radius=10,
            text="Voreinstellungen",
            text_color=GetStartupVariables.text_color_SET,
            font=("bold", font_size))
        self.examiner_option_menu_label.grid(row=1, column=1, columnspan=1, rowspan=1, sticky="nesw")

        self.options_menu_examiner = ctk.CTkOptionMenu(master=self.examiner_option_menu_frame,
                                                       font=("bold", font_size),
                                                       dropdown_font=("bold", font_size),
                                                       corner_radius=5,
                                                       variable=tk.StringVar(
                                                           value=GetPersonalVariables.last_chosen_examiner),
                                                       values=GetPersonalVariables.examiner_list,
                                                       command=self.examiner_select)
        # the command automatically passes the current value as an argument to the specified method
        self.options_menu_examiner.grid(row=1, column=3, columnspan=1, rowspan=1, sticky="new")
        # entry frame------------------------------------------------------------
        self.entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                        corner_radius=20)
        self.entry_frame.grid(row=8, column=2, columnspan=10, rowspan=15, sticky="nesw")

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
                                                   corner_radius=10,
                                                   text="Vorname",
                                                   text_color=GetStartupVariables.text_color_SET,
                                                   font=("bold", font_size))
        self.first_name_entry_label.grid(row=5, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.first_name_entry = ctk.CTkEntry(master=self.entry_frame,
                                             font=("bold", font_size),
                                             state="disabled"
                                             )
        self.first_name_entry.grid(row=10, column=20, columnspan=2, rowspan=1, sticky="nesw")

        self.first_name_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                           corner_radius=10)
        self.first_name_entry_unchanged_overlay_label_frame.grid(row=10, column=20, columnspan=2, rowspan=1,
                                                                 sticky="nesw")

        self.first_name_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.first_name_entry_unchanged_overlay_label_frame,
            anchor="w",
            text=GetPersonalVariables.personal_infos_examiner[0],
            font=("bold", font_size))
        self.first_name_entry_unchanged_overlay_label.place(relx=0.1,
                                                            rely=0.3)

        # last name entry------------------------------------------------------------
        self.last_name_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                  fg_color=GetStartupVariables.color_SET_blue,
                                                  corner_radius=10,
                                                  text="Nachname",
                                                  text_color=GetStartupVariables.text_color_SET,
                                                  font=("bold", font_size))
        self.last_name_entry_label.grid(row=22, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.last_name_entry = ctk.CTkEntry(master=self.entry_frame,
                                            font=("bold", font_size),
                                            state="disabled")
        self.last_name_entry.grid(row=27, column=20, columnspan=2, rowspan=1, sticky="nesw")

        self.last_name_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                          corner_radius=10)
        self.last_name_entry_unchanged_overlay_label_frame.grid(row=27, column=20, columnspan=2, rowspan=1,
                                                                sticky="nesw")

        self.last_name_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.last_name_entry_unchanged_overlay_label_frame,
            anchor="w",
            text=GetPersonalVariables.personal_infos_examiner[1],
            font=("bold", font_size))
        self.last_name_entry_unchanged_overlay_label.place(relx=0.1,
                                                           rely=0.3)

        # birth date entry------------------------------------------------------------
        self.birth_date_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                   fg_color=GetStartupVariables.color_SET_blue,
                                                   corner_radius=10,
                                                   text="Geburtsdatum",
                                                   text_color=GetStartupVariables.text_color_SET,
                                                   font=("bold", font_size))
        self.birth_date_entry_label.grid(row=39, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.birth_date_entry = tkc.DateEntry(master=self.entry_frame,
                                              font=("bold", math.ceil(font_size)),
                                              date_pattern='dd.mm.yyyy',
                                              year=1976,
                                              month=2,
                                              day=1,
                                              state="readonly")
        self.birth_date_entry.grid(row=44, column=20, columnspan=2, rowspan=1, sticky="nesw")

        self.birth_date_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                           corner_radius=10)
        self.birth_date_entry_unchanged_overlay_label_frame.grid(row=44, column=20, columnspan=2, rowspan=1,
                                                                 sticky="nesw")

        self.birth_date_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.birth_date_entry_unchanged_overlay_label_frame,
            anchor="w",
            text=GetPersonalVariables.personal_infos_examiner[2],
            font=("bold", font_size))
        self.birth_date_entry_unchanged_overlay_label.place(relx=0.1,
                                                            rely=0.3)

        # change, save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=20)
        self.button_frame.grid(row=25, column=2, columnspan=18, rowspan=2, sticky="nesw")

        # Grid configuration
        self.button_frame.grid_columnconfigure(0, weight=3)
        self.button_frame.grid_columnconfigure(1, weight=20)
        self.button_frame.grid_columnconfigure(2, weight=3)
        self.button_frame.grid_columnconfigure(3, weight=20)
        self.button_frame.grid_columnconfigure(4, weight=3)
        self.button_frame.grid_columnconfigure(5, weight=20)
        self.button_frame.grid_columnconfigure(6, weight=3)
        self.button_frame.grid_rowconfigure(0, weight=3)
        self.button_frame.grid_rowconfigure(1, weight=10)
        self.button_frame.grid_rowconfigure(2, weight=3)

        self.change_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                           corner_radius=10,
                                           text="Ändern",
                                           font=("bold", font_size),
                                           state="normal",
                                           command=lambda: self.change_entry_data_examiner())
        self.change_button.grid(row=1, column=1, columnspan=1, rowspan=1, sticky="nesw")

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", font_size),
                                         state="disabled",
                                         command=lambda: self.save_entry_data_examiner())
        self.save_button.grid(row=1, column=3, columnspan=1, rowspan=1, sticky="nesw")

        self.continue_button = ctk.CTkButton(master=self.button_frame,
                                             # continue button
                                             corner_radius=10,
                                             text="Weiter",
                                             font=("bold", font_size),
                                             state="normal",
                                             command=self.continue_button_function)
        self.continue_button.grid(row=1, column=5, columnspan=1, rowspan=1, sticky="nesw")

    def continue_button_function(self):
        self.master.switch_window("1.3")
        self.write_personal_json()

    def change_entry_data_examiner(self):  # make the entries typeable
        self.first_name_entry_unchanged_overlay_label.grid_forget()
        self.first_name_entry_unchanged_overlay_label_frame.grid_forget()
        self.last_name_entry_unchanged_overlay_label.grid_forget()
        self.last_name_entry_unchanged_overlay_label_frame.grid_forget()
        self.birth_date_entry_unchanged_overlay_label.grid_forget()
        self.birth_date_entry_unchanged_overlay_label_frame.grid_forget()

        self.first_name_entry.configure(state="normal", placeholder_text="Vorname")
        self.last_name_entry.configure(state="normal", placeholder_text="Nachname")

        self.change_button.configure(state="disabled")
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

    def save_entry_data_examiner(self):
        personal_infos_examiner = [self.first_name_entry.get(),
                                   self.last_name_entry.get(),
                                   self.birth_date_entry.get()]
        last_chosen_examiner = json_reader("personal_var", "last_chosen_examiner", main_pi_location + "../JSON/")

        if (len(personal_infos_examiner[0].strip()) +
                len(personal_infos_examiner[1].strip()) >= 4):
            self.continue_button.configure(state="normal")
            json_writer("personal_var", ("personal_infos_examiner_" + last_chosen_examiner),
                        personal_infos_examiner, main_pi_location + "../JSON/")

            self.first_name_entry_unchanged_overlay_label_frame.grid(row=10, column=20, columnspan=2, rowspan=1,
                                                                     sticky="nesw")
            self.first_name_entry_unchanged_overlay_label.place(relx=0.1,
                                                                rely=0.3)
            self.last_name_entry_unchanged_overlay_label_frame.grid(row=27, column=20, columnspan=2, rowspan=1,
                                                                    sticky="nesw")
            self.last_name_entry_unchanged_overlay_label.place(relx=0.1,
                                                               rely=0.3)
            self.birth_date_entry_unchanged_overlay_label_frame.grid(row=44, column=20, columnspan=2, rowspan=1,
                                                                     sticky="nesw")
            self.birth_date_entry_unchanged_overlay_label.place(relx=0.1,
                                                                rely=0.3)
            self.update_labels(personal_infos_examiner)

            self.first_name_entry.configure(state="disabled")
            self.last_name_entry.configure(state="disabled")

            self.change_button.configure(state="normal")
            self.save_button.configure(state="disabled")
            self.continue_button.configure(state="normal")
        else:
            self.continue_button.configure(state="disabled")
            print("Sum of first name plus surname not at least 4 digits")

    def update_labels(self, infos):
        self.first_name_entry_unchanged_overlay_label.configure(text=infos[0])
        self.last_name_entry_unchanged_overlay_label.configure(text=infos[1])
        self.birth_date_entry_unchanged_overlay_label.configure(text=infos[2])

    def examiner_select(self, which):
        json_writer("personal_var", "last_chosen_examiner", which, main_pi_location + "../JSON/")
        personal_infos_examiner = json_reader("personal_var", f"personal_infos_examiner_{which}",
                                              main_pi_location + "../JSON/")
        self.update_labels(personal_infos_examiner)

    @staticmethod
    def write_personal_json():
        last_chosen_examiner = json_reader("personal_var", "last_chosen_examiner", main_pi_location + "../JSON/")
        personal_infos_examiner = json_reader("personal_var", f"personal_infos_examiner_{last_chosen_examiner}",
                                              main_pi_location + "../JSON/")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
        json_writer(personal_json_name, "personal_infos_examiner", personal_infos_examiner, personal_folder_path)

    def update_size(self, font_size):
        self.indicator_bar.configure(font=("bold", font_size), height=font_size)
        self.back_button.configure(width=font_size,
                                   height=font_size)
        back_arrow_image.configure(size=(font_size, font_size))
        self.first_name_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5)
        self.first_name_entry.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 10)
        self.first_name_entry_unchanged_overlay_label.configure(font=("bold", font_size), height=font_size * 1,
                                                                width=font_size * 9)
        self.first_name_entry_unchanged_overlay_label_frame.configure(height=font_size * 2,
                                                                      width=font_size * 10)
        self.last_name_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5)
        self.last_name_entry.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 10)
        self.last_name_entry_unchanged_overlay_label.configure(font=("bold", font_size), height=font_size * 1,
                                                               width=font_size * 9)
        self.last_name_entry_unchanged_overlay_label_frame.configure(height=font_size * 2,
                                                                     width=font_size * 10)
        self.birth_date_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5)
        self.birth_date_entry.configure(font=("bold", math.ceil(font_size) - 4))
        self.birth_date_entry_unchanged_overlay_label.configure(font=("bold", font_size), height=font_size * 1,
                                                                width=font_size * 9)
        self.birth_date_entry_unchanged_overlay_label_frame.configure(height=font_size * 2,
                                                                      width=font_size * 10)
        self.button_frame.configure(height=font_size*2)
        self.change_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4)
        self.save_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4)
        self.continue_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4)

        self.examiner_option_menu_frame.configure(height=font_size * 2)
        self.examiner_option_menu_label.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4)
        self.options_menu_examiner.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4)
