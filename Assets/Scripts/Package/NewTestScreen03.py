#!/usr/bin/python3
# Date: 21.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 3; ID=1.2

import customtkinter as ctk
import tkinter as tk
import tkcalendar as tkc
from .JsonFunctions import json_reader, json_writer
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetPersonalVariables, back_arrow_image


class NewTestScreen03(ctk.CTkFrame):  # class for the NewTestScreen03 window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(GetStartupVariables.window_geometry[0] - 10),
                         height=(GetStartupVariables.window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   y=5)

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          width=GetStartupVariables.window_geometry[0] - 70,
                                          height=40,
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 3:" +
                                                " persönliche Daten des Prüfers eingeben"),
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", 20),
                                          anchor="w")
        self.indicator_bar.place(x=0,
                                 y=0)
        # option menu examiner------------------------------------------------------------
        self.examiner_option_menu_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                       width=340,
                                                       height=70,
                                                       corner_radius=20)
        self.examiner_option_menu_frame.place(x=30,
                                              y=75)

        self.examiner_option_menu_label = ctk.CTkLabel(
            master=self.examiner_option_menu_frame,
            fg_color=GetStartupVariables.color_SET_blue,
            width=200,
            height=50,
            corner_radius=10,
            text="Voreinstellungen",
            text_color=GetStartupVariables.text_color_SET,
            font=("bold", 20))
        self.examiner_option_menu_label.place(x=10,
                                              y=10)

        self.options_menu_examiner = ctk.CTkOptionMenu(master=self.examiner_option_menu_frame,
                                                       width=100,
                                                       height=50,
                                                       font=("bold", 20),
                                                       dropdown_font=("bold", 20),
                                                       corner_radius=5,
                                                       variable=tk.StringVar(
                                                           value=GetPersonalVariables.last_chosen_examiner),
                                                       values=GetPersonalVariables.examiner_list,
                                                       command=self.examiner_select)
        # the command automatically passes the current value as an argument to the specified method
        self.options_menu_examiner.place(x=230,
                                         y=10)
        # entry frame------------------------------------------------------------
        self.entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                        width=340,
                                        height=360,
                                        corner_radius=20)
        self.entry_frame.place(x=30,
                               y=175)

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         width=40,
                                         height=40,
                                         corner_radius=10,
                                         text="",
                                         anchor="ne",
                                         image=back_arrow_image,
                                         command=lambda: self.master.open_top_level_window_really_switch(
                                             "1.1"))
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
                                             width=250,
                                             height=50,
                                             font=("bold", 20),
                                             state="disabled"
                                             )
        self.first_name_entry.place(x=10,
                                    y=60)

        self.first_name_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                           width=250,
                                                                           height=50,
                                                                          corner_radius=10)
        self.first_name_entry_unchanged_overlay_label_frame.place(x=10,
                                                                  y=60)

        self.first_name_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.first_name_entry_unchanged_overlay_label_frame,
            width=230,
            height=50,
            anchor="w",
            text=GetPersonalVariables.personal_infos_examiner[0],
            font=("bold", 20))
        self.first_name_entry_unchanged_overlay_label.place(x=10,
                                                            y=0)

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
                                            width=250,
                                            height=50,
                                            font=("bold", 20),
                                            state="disabled")
        self.last_name_entry.place(x=10,
                                   y=180)

        self.last_name_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                          width=250,
                                                                          height=50,
                                                                          corner_radius=10)
        self.last_name_entry_unchanged_overlay_label_frame.place(x=10,
                                                                 y=180)

        self.last_name_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.last_name_entry_unchanged_overlay_label_frame,
            width=230,
            height=50,
            anchor="w",
            text=GetPersonalVariables.personal_infos_examiner[1],
            font=("bold", 20))
        self.last_name_entry_unchanged_overlay_label.place(x=10,
                                                           y=0)

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
                                              year=1976,
                                              month=2,
                                              day=1,
                                              state="readonly")
        self.birth_date_entry.place(x=15,
                                    y=375)

        self.birth_date_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                           width=250,
                                                                           height=50,
                                                                           corner_radius=10)
        self.birth_date_entry_unchanged_overlay_label_frame.place(x=10,
                                                                  y=300)

        self.birth_date_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.birth_date_entry_unchanged_overlay_label_frame,
            width=230,
            height=50,
            anchor="w",
            text=GetPersonalVariables.personal_infos_examiner[2],
            font=("bold", 20))
        self.birth_date_entry_unchanged_overlay_label.place(x=10,
                                                            y=0)

        # change, save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         width=380,
                                         height=70,
                                         corner_radius=20)
        self.button_frame.place(x=30,
                                y=570)

        self.change_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                           width=120,
                                           height=50,
                                           corner_radius=10,
                                           text="Ändern",
                                           font=("bold", 20),
                                           state="normal",
                                           command=lambda: self.change_entry_data_examiner())
        self.change_button.place(x=10,
                                 y=10)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         width=120,
                                         height=50,
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", 20),
                                         state="disabled",
                                         command=lambda: self.save_entry_data_examiner())
        self.save_button.place(x=140,
                               y=10)

        self.continue_button = ctk.CTkButton(master=self.button_frame,
                                             # continue button
                                             width=100,
                                             height=50,
                                             corner_radius=10,
                                             text="Weiter",
                                             font=("bold", 20),
                                             state="normal",
                                             command=self.continue_button_function)
        self.continue_button.place(x=270,
                                   y=10)

    def continue_button_function(self):
        self.master.switch_window("1.3")
        self.write_personal_json()

    def change_entry_data_examiner(self):  # make the entrys typable
        self.first_name_entry_unchanged_overlay_label.place_forget()
        self.first_name_entry_unchanged_overlay_label_frame.place_forget()
        self.last_name_entry_unchanged_overlay_label.place_forget()
        self.last_name_entry_unchanged_overlay_label_frame.place_forget()
        self.birth_date_entry_unchanged_overlay_label.place_forget()
        self.birth_date_entry_unchanged_overlay_label_frame.place_forget()

        self.first_name_entry.configure(state="normal", placeholder_text="Vorname")
        self.last_name_entry.configure(state="normal", placeholder_text="Nachname")

        self.change_button.configure(state="disabled")
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

    def save_entry_data_examiner(self):
        personal_infos_examiner = [self.first_name_entry.get(),
                                   self.last_name_entry.get(),
                                   self.birth_date_entry.get()]
        last_chosen_examiner = json_reader("personal_var", "last_chosen_examiner", "../JSON/")

        if (len(personal_infos_examiner[0].strip()) +
                len(personal_infos_examiner[1].strip()) >= 4):
            self.continue_button.configure(state="normal")
            json_writer("personal_var", ("personal_infos_examiner_" + last_chosen_examiner),
                        personal_infos_examiner, "../JSON/")

            self.first_name_entry_unchanged_overlay_label_frame.place(x=10, y=60)
            self.first_name_entry_unchanged_overlay_label.place(x=10, y=0)
            self.last_name_entry_unchanged_overlay_label_frame.place(x=10, y=180)
            self.last_name_entry_unchanged_overlay_label.place(x=10, y=0)
            self.birth_date_entry_unchanged_overlay_label_frame.place(x=10, y=300)
            self.birth_date_entry_unchanged_overlay_label.place(x=10, y=0)
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
        json_writer("personal_var", "last_chosen_examiner", which, "../JSON/")
        personal_infos_examiner = json_reader("personal_var", f"personal_infos_examiner_{which}", "../JSON/")
        self.update_labels(personal_infos_examiner)

    @staticmethod
    def write_personal_json():
        last_chosen_examiner = json_reader("personal_var", "last_chosen_examiner", "../JSON/")
        personal_infos_examiner = json_reader("personal_var", f"personal_infos_examiner_{last_chosen_examiner}",
                                              "../JSON/")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", "../JSON/")
        json_writer(personal_json_name, "personal_infos_examiner", personal_infos_examiner, personal_folder_path)
