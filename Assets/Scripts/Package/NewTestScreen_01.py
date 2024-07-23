#!/usr/bin/python3
# Date: 18.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 1; ID=1.0

import customtkinter as ctk
# Shared variables----------------------------------------
from .sharedVar import window_geometry, color_SET, text_color_SET, back_arrow_image


class NewTestScreen_01(ctk.CTkFrame):  # class for the NewTestScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   y=5)

        # top bar------------------------------------------------------------
        self.newtestscreen01_indicator_bar = ctk.CTkLabel(master=self,
                                                          # top bar that indicates the screen where you are
                                                          fg_color=color_SET,
                                                          width=window_geometry[0] - 70,
                                                          height=40,
                                                          corner_radius=10,
                                                          text=("Neuer Test - Schritt 1:" +
                                                                " persönliche Daten des Prüflings eingeben"),
                                                          text_color=text_color_SET,
                                                          font=("bold", 20),
                                                          anchor="w")
        self.newtestscreen01_indicator_bar.place(x=0,
                                                 y=0)

        # button frame------------------------------------------------------------
        self.newtestscreen01_entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                        width=340,
                                                        height=360)
        self.newtestscreen01_entry_frame.place(x=30,
                                               y=75)

        # back button------------------------------------------------------------
        self.newtestscreen01_back_button = ctk.CTkButton(master=self,  # back button
                                                         width=40,
                                                         height=40,
                                                         corner_radius=10,
                                                         text="",
                                                         anchor="ne",
                                                         image=back_arrow_image,
                                                         command=lambda: self.master.open_top_level_window_really_switch(
                                                             "0"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.newtestscreen01_back_button.place(x=window_geometry[0] - 65,
                                               y=0)

        # first name entry------------------------------------------------------------
        self.newtestscreen01_first_name_entry_label = ctk.CTkLabel(master=self.newtestscreen01_entry_frame,
                                                                   fg_color=color_SET,
                                                                   width=100,
                                                                   height=40,
                                                                   corner_radius=10,
                                                                   text="Vorname",
                                                                   text_color=text_color_SET,
                                                                   font=("bold", 20))
        self.newtestscreen01_first_name_entry_label.place(x=10,
                                                          y=10)

        self.newtestscreen01_first_name_entry = ctk.CTkEntry(master=self.newtestscreen01_entry_frame,
                                                             placeholder_text="Vorname",
                                                             width=250,
                                                             height=50,
                                                             font=("bold", 20)
                                                             )
        self.newtestscreen01_first_name_entry.place(x=10,
                                                    y=60)

        # last name entry------------------------------------------------------------
        self.newtestscreen01_last_name_entry_label = ctk.CTkLabel(master=self.newtestscreen01_entry_frame,
                                                                  fg_color=color_SET,
                                                                  width=100,
                                                                  height=40,
                                                                  corner_radius=10,
                                                                  text="Nachname",
                                                                  text_color=text_color_SET,
                                                                  font=("bold", 20))
        self.newtestscreen01_last_name_entry_label.place(x=10,
                                                         y=130)

        self.newtestscreen01_last_name_entry = ctk.CTkEntry(master=self.newtestscreen01_entry_frame,
                                                            placeholder_text="Nachname",
                                                            width=250,
                                                            height=50,
                                                            font=("bold", 20)
                                                            )
        self.newtestscreen01_last_name_entry.place(x=10,
                                                   y=180)

        # birth date entry------------------------------------------------------------
        self.newtestscreen01_birth_date_entry_label = ctk.CTkLabel(master=self.newtestscreen01_entry_frame,
                                                                   fg_color=color_SET,
                                                                   width=100,
                                                                   height=40,
                                                                   corner_radius=10,
                                                                   text="Geburtsdatum",
                                                                   text_color=text_color_SET,
                                                                   font=("bold", 20))
        self.newtestscreen01_birth_date_entry_label.place(x=10,
                                                          y=250)

        self.newtestscreen01_birth_date_entry = ctk.CTkEntry(master=self.newtestscreen01_entry_frame,
                                                             placeholder_text="dd.mm.yyyy",
                                                             width=250,
                                                             height=50,
                                                             font=("bold", 20)
                                                             )
        self.newtestscreen01_birth_date_entry.place(x=10,
                                                    y=300)

        # save and continue button------------------------------------------------------------

        self.newtestscreen01_button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                                         width=250,
                                                         height=70)
        self.newtestscreen01_button_frame.place(x=30,
                                                y=500)

        self.newtestscreen01_save_button = ctk.CTkButton(master=self.newtestscreen01_button_frame,  # continue button
                                                         width=120,
                                                         height=50,
                                                         corner_radius=10,
                                                         text="Speichern",
                                                         font=("bold", 20),
                                                         command=lambda: saveEntryDataExaminee())
        self.newtestscreen01_save_button.place(x=10,
                                               y=10)

        self.newtestscreen01_continue_button = ctk.CTkButton(master=self.newtestscreen01_button_frame,
                                                             # continue button
                                                             width=100,
                                                             height=50,
                                                             corner_radius=10,
                                                             text="Weiter",
                                                             font=("bold", 20),
                                                             state="disabled",
                                                             command=lambda: self.master.switch_window("1.1"))
        self.newtestscreen01_continue_button.place(x=140,
                                                   y=10)

        def saveEntryDataExaminee():
            personal_infos_examinee = [self.newtestscreen01_first_name_entry.get(),
                                       self.newtestscreen01_last_name_entry.get(),
                                       self.newtestscreen01_birth_date_entry.get()]

            if (len(personal_infos_examinee[0].strip()) +
                    len(personal_infos_examinee[1].strip()) +
                    len(personal_infos_examinee[2].strip()) >= 14):
                self.newtestscreen01_continue_button.configure(state="normal")
                self.app.changeListInJson("personal_var", "personal_infos_examinee", personal_infos_examinee)
            else:
                self.newtestscreen01_continue_button.configure(state="disabled")
                print("Date-Format wrong or the sum of first name plus surname not at least 4 digits")
