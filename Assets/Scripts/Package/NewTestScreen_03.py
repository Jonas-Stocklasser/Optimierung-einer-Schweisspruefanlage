#!/usr/bin/python3
# Date: 21.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 3; ID=1.2

import customtkinter as ctk
import tkinter as tk
import pandas as pd
import tkcalendar as tkc
# Shared variables----------------------------------------
from .sharedVar import window_geometry, color_SET_blue, text_color_SET, back_arrow_image, personal_infos_examiner, \
    last_chosen_examiner, examiner_list, color_SET_gray


class NewTestScreen_03(ctk.CTkFrame):  # class for the NewTestScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   y=5)

        # top bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=color_SET_blue,
                                          width=window_geometry[0] - 70,
                                          height=40,
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 3:" +
                                                " persönliche Daten des Prüfers eingeben"),
                                          text_color=text_color_SET,
                                          font=("bold", 20),
                                          anchor="w")
        self.indicator_bar.place(x=0,
                                 y=0)
        # options menu examiner------------------------------------------------------------
        self.examiner_option_menu_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                       width=340,
                                                       height=70)
        self.examiner_option_menu_frame.place(x=30,
                                              y=75)

        self.examiner_option_menu_label = ctk.CTkLabel(
            master=self.examiner_option_menu_frame,
            fg_color=color_SET_blue,
            width=200,
            height=50,
            corner_radius=10,
            text="Voreinstellungen",
            text_color=text_color_SET,
            font=("bold", 20))
        self.examiner_option_menu_label.place(x=10,
                                              y=10)

        self.options_menu_examiner = ctk.CTkOptionMenu(master=self.examiner_option_menu_frame,
                                                       width=100,
                                                       height=50,
                                                       font=("bold", 20),
                                                       dropdown_font=("bold", 20),
                                                       corner_radius=5,
                                                       variable=tk.StringVar(value=last_chosen_examiner),
                                                       values=examiner_list,
                                                       command=self.examinerSelect)
        # the command automatically passes the current value as an argument to the specified method
        self.options_menu_examiner.place(x=230,
                                         y=10)
        # entry frame------------------------------------------------------------
        self.entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                        width=340,
                                        height=360)
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
        self.back_button.place(x=window_geometry[0] - 65,
                               y=0)

        # first name entry------------------------------------------------------------
        self.first_name_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                   fg_color=color_SET_blue,
                                                   width=100,
                                                   height=40,
                                                   corner_radius=10,
                                                   text="Vorname",
                                                   text_color=text_color_SET,
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

        self.first_name_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.entry_frame,
            width=250,
            height=50,
            fg_color=color_SET_gray,
            anchor="w",
            corner_radius=10,
            text=personal_infos_examiner[0],
            text_color=text_color_SET,
            font=("bold", 20))
        self.first_name_entry_unchanged_overlay_label.place(x=10,
                                                            y=60)

        # last name entry------------------------------------------------------------
        self.last_name_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                  fg_color=color_SET_blue,
                                                  width=100,
                                                  height=40,
                                                  corner_radius=10,
                                                  text="Nachname",
                                                  text_color=text_color_SET,
                                                  font=("bold", 20))
        self.last_name_entry_label.place(x=10,
                                         y=130)

        self.last_name_entry = ctk.CTkEntry(master=self.entry_frame,
                                            width=250,
                                            height=50,
                                            font=("bold", 20),
                                            state="disabled"
                                            )
        self.last_name_entry.place(x=10,
                                   y=180)

        self.last_name_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.entry_frame,
            width=250,
            height=50,
            fg_color=color_SET_gray,
            anchor="w",
            corner_radius=10,
            text=personal_infos_examiner[1],
            text_color=text_color_SET,
            font=("bold", 20))
        self.last_name_entry_unchanged_overlay_label.place(x=10,
                                                           y=180)

        # birth date entry------------------------------------------------------------
        self.birth_date_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                   fg_color=color_SET_blue,
                                                   width=100,
                                                   height=40,
                                                   corner_radius=10,
                                                   text="Geburtsdatum",
                                                   text_color=text_color_SET,
                                                   font=("bold", 20))
        self.birth_date_entry_label.place(x=10,
                                          y=250)

        self.birth_date_entry = tkc.DateEntry(master=self.entry_frame,
                                              font=("bold", 20),
                                              date_pattern='dd.mm.yyyy',
                                              year=2000,
                                              month=1,
                                              day=1)
        self.birth_date_entry.place(x=15,
                                    y=375)

        self.birth_date_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.entry_frame,
            width=250,
            height=50,
            fg_color=color_SET_gray,
            anchor="w",
            corner_radius=10,
            text=personal_infos_examiner[2],
            text_color=text_color_SET,
            font=("bold", 20))
        self.birth_date_entry_unchanged_overlay_label.place(x=10,
                                                            y=300)

        # save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         width=380,
                                         height=70)
        self.button_frame.place(x=30,
                                y=570)

        self.change_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                           width=120,
                                           height=50,
                                           corner_radius=10,
                                           text="Ändern",
                                           font=("bold", 20),
                                           state="normal",
                                           command=lambda: self.changeEntryDataExaminer())
        self.change_button.place(x=10,
                                 y=10)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         width=120,
                                         height=50,
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", 20),
                                         state="disabled",
                                         command=lambda: self.saveEntryDataExaminer())
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
                                             command=lambda: self.master.switch_window("1.3"))
        self.continue_button.place(x=270,
                                   y=10)

    def changeEntryDataExaminer(self):
        self.first_name_entry_unchanged_overlay_label.place_forget()
        self.last_name_entry_unchanged_overlay_label.place_forget()
        self.birth_date_entry_unchanged_overlay_label.place_forget()

        self.first_name_entry.configure(state="normal", placeholder_text="Vorname")
        self.last_name_entry.configure(state="normal", placeholder_text="Nachname")

        self.change_button.configure(state="disabled")
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

    def saveEntryDataExaminer(self):
        global personal_infos_examiner
        global last_chosen_examiner
        personal_infos_examiner = [self.first_name_entry.get(),
                                   self.last_name_entry.get(),
                                   self.birth_date_entry.get()]

        if (len(personal_infos_examiner[0].strip()) +
                len(personal_infos_examiner[1].strip()) +
                len(personal_infos_examiner[2].strip()) >= 14):
            self.continue_button.configure(state="normal")
            self.app.changeListInJson("personal_var", ("personal_infos_examiner_" + last_chosen_examiner),
                                      personal_infos_examiner)

            self.first_name_entry_unchanged_overlay_label.place(x=10, y=60)
            self.last_name_entry_unchanged_overlay_label.place(x=10, y=180)
            self.birth_date_entry_unchanged_overlay_label.place(x=10, y=300)
            self.updateLabels(personal_infos_examiner)

            self.first_name_entry.configure(state="disabled")
            self.last_name_entry.configure(state="disabled")

            self.change_button.configure(state="normal")
            self.save_button.configure(state="disabled")
            self.continue_button.configure(state="normal")
        else:
            self.continue_button.configure(state="disabled")
            print("Date-Format wrong or the sum of first name plus surname not at least 4 digits")

    def updateLabels(self, infos):
        self.first_name_entry_unchanged_overlay_label.configure(text=infos[0])
        self.last_name_entry_unchanged_overlay_label.configure(text=infos[1])
        self.birth_date_entry_unchanged_overlay_label.configure(text=infos[2])

    def examinerSelect(self, which):
        global last_chosen_examiner
        data = pd.read_json("../Other/personal_var.json", encoding="latin1")
        index = data[data['var'] == "last_chosen_examiner"].index
        data.loc[index[0], 'val'] = which
        with open("../Other/personal_var.json", "w") as file:
            data.to_json(file, orient="records", indent=2)

        with open("../Other/personal_var.json") as file:
            data = pd.read_json(file)
        last_chosen_examiner = data.loc[data['var'] == "last_chosen_examiner", "val"].values[0]
        personal_infos_examiner = \
            data.loc[data['var'] == ("personal_infos_examiner_" + last_chosen_examiner), "val"].values[0]
        self.updateLabels(personal_infos_examiner)
