#!/usr/bin/python3
# Date: 18.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 2; ID=1.1

import customtkinter as ctk
import tkinter as tk
# Shared variables----------------------------------------
from .sharedVar import window_geometry, color_SET, text_color_SET, back_arrow_image, personal_infos_examiner, \
    last_chosen_examiner, examiner_list


class NewTestScreen_02(ctk.CTkFrame):  # class for the NewTestScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   y=5)

        # calling the create_widgets method to create all widgets that are children of OptionsScreen
        self.create_widgets()

    def create_widgets(self):
        # top bar------------------------------------------------------------
        newtestscreen02_indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                                     fg_color=color_SET,
                                                     width=window_geometry[0] - 70,
                                                     height=40,
                                                     corner_radius=10,
                                                     text=("Neuer Test - Schritt 2:" +
                                                           " persönliche Daten des Prüfers eingeben"),
                                                     text_color=text_color_SET,
                                                     font=("bold", 20),
                                                     anchor="w")
        newtestscreen02_indicator_bar.place(x=0,
                                            y=0)
        # options menu examiner------------------------------------------------------------
        newtestscreen02_examiner_option_menu_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                                  width=120,
                                                                  height=70)
        newtestscreen02_examiner_option_menu_frame.place(x=30,
                                                         y=75)

        options_menu_examiner = ctk.CTkOptionMenu(master=newtestscreen02_examiner_option_menu_frame,
                                                  width=100,
                                                  height=50,
                                                  font=("bold", 20),
                                                  dropdown_font=("bold", 20),
                                                  corner_radius=5,
                                                  variable=tk.StringVar(value=last_chosen_examiner),
                                                  values=examiner_list,
                                                  command=self.master.appearance_mode_switch)
        # the command automatically passes the current value as an argument to the specified method
        options_menu_examiner.place(x=10,
                                    y=10)
        # entry frame------------------------------------------------------------
        newtestscreen02_entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                   width=340,
                                                   height=360)
        newtestscreen02_entry_frame.place(x=30,
                                          y=175)

        # back button------------------------------------------------------------
        newtestscreen02_back_button = ctk.CTkButton(master=self,  # back button
                                                    width=40,
                                                    height=40,
                                                    corner_radius=10,
                                                    text="",
                                                    anchor="ne",
                                                    image=back_arrow_image,
                                                    command=lambda: self.master.open_top_level_window_really_switch(
                                                        "1.0"))
        # the command does call the switch_window method because there is unsaved content to loose
        newtestscreen02_back_button.place(x=window_geometry[0] - 65,
                                          y=0)

        # first name entry------------------------------------------------------------
        newtestscreen02_first_name_entry_label = ctk.CTkLabel(master=newtestscreen02_entry_frame,
                                                              fg_color=color_SET,
                                                              width=100,
                                                              height=40,
                                                              corner_radius=10,
                                                              text="Vorname",
                                                              text_color=text_color_SET,
                                                              font=("bold", 20))
        newtestscreen02_first_name_entry_label.place(x=10,
                                                     y=10)

        newtestscreen02_first_name_entry = ctk.CTkEntry(master=newtestscreen02_entry_frame,
                                                        width=250,
                                                        height=50,
                                                        font=("bold", 20),
                                                        state="disabled"
                                                        )
        newtestscreen02_first_name_entry.place(x=10,
                                               y=60)

        newtestscreen02_first_name_entry_unchanged_overlay_label = ctk.CTkLabel(master=newtestscreen02_entry_frame,
                                                                                width=250,
                                                                                height=50,
                                                                                fg_color="transparent",
                                                                                anchor="w",
                                                                                corner_radius=10,
                                                                                text=personal_infos_examiner[0],
                                                                                text_color=text_color_SET,
                                                                                font=("bold", 20))
        newtestscreen02_first_name_entry_unchanged_overlay_label.place(x=10,
                                                                       y=60)

        # last name entry------------------------------------------------------------
        newtestscreen02_last_name_entry_label = ctk.CTkLabel(master=newtestscreen02_entry_frame,
                                                             fg_color=color_SET,
                                                             width=100,
                                                             height=40,
                                                             corner_radius=10,
                                                             text="Nachname",
                                                             text_color=text_color_SET,
                                                             font=("bold", 20))
        newtestscreen02_last_name_entry_label.place(x=10,
                                                    y=130)

        newtestscreen02_last_name_entry = ctk.CTkEntry(master=newtestscreen02_entry_frame,
                                                       width=250,
                                                       height=50,
                                                       font=("bold", 20),
                                                       state="disabled"
                                                       )
        newtestscreen02_last_name_entry.place(x=10,
                                              y=180)

        newtestscreen02_last_name_entry_unchanged_overlay_label = ctk.CTkLabel(master=newtestscreen02_entry_frame,
                                                                               width=250,
                                                                               height=50,
                                                                               fg_color="transparent",
                                                                               anchor="w",
                                                                               corner_radius=10,
                                                                               text=personal_infos_examiner[1],
                                                                               text_color=text_color_SET,
                                                                               font=("bold", 20))
        newtestscreen02_last_name_entry_unchanged_overlay_label.place(x=10,
                                                                      y=180)

        # birth date entry------------------------------------------------------------
        newtestscreen02_birth_date_entry_label = ctk.CTkLabel(master=newtestscreen02_entry_frame,
                                                              fg_color=color_SET,
                                                              width=100,
                                                              height=40,
                                                              corner_radius=10,
                                                              text="Geburtsdatum",
                                                              text_color=text_color_SET,
                                                              font=("bold", 20))
        newtestscreen02_birth_date_entry_label.place(x=10,
                                                     y=250)

        newtestscreen02_birth_date_entry = ctk.CTkEntry(master=newtestscreen02_entry_frame,
                                                        width=250,
                                                        height=50,
                                                        font=("bold", 20),
                                                        state="disabled"
                                                        )
        newtestscreen02_birth_date_entry.place(x=10,
                                               y=300)

        newtestscreen02_birth_date_entry_unchanged_overlay_label = ctk.CTkLabel(master=newtestscreen02_entry_frame,
                                                                                width=250,
                                                                                height=50,
                                                                                fg_color="transparent",
                                                                                anchor="w",
                                                                                corner_radius=10,
                                                                                text=personal_infos_examiner[2],
                                                                                text_color=text_color_SET,
                                                                                font=("bold", 20))
        newtestscreen02_birth_date_entry_unchanged_overlay_label.place(x=10,
                                                                       y=300)

        # save and continue button------------------------------------------------------------

        newtestscreen02_button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                                    width=380,
                                                    height=70)
        newtestscreen02_button_frame.place(x=30,
                                           y=570)

        newtestscreen02_change_button = ctk.CTkButton(master=newtestscreen02_button_frame,  # continue button
                                                      width=120,
                                                      height=50,
                                                      corner_radius=10,
                                                      text="Ändern",
                                                      font=("bold", 20),
                                                      state="normal",
                                                      command=lambda: changeEntryDataExaminer())
        newtestscreen02_change_button.place(x=10,
                                            y=10)

        newtestscreen02_save_button = ctk.CTkButton(master=newtestscreen02_button_frame,  # continue button
                                                    width=120,
                                                    height=50,
                                                    corner_radius=10,
                                                    text="Speichern",
                                                    font=("bold", 20),
                                                    state="disabled",
                                                    command=lambda: saveEntryDataExaminer())
        newtestscreen02_save_button.place(x=140,
                                          y=10)

        newtestscreen02_continue_button = ctk.CTkButton(master=newtestscreen02_button_frame,  # continue button
                                                        width=100,
                                                        height=50,
                                                        corner_radius=10,
                                                        text="Weiter",
                                                        font=("bold", 20),
                                                        state="normal",
                                                        command=lambda: self.master.switch_window("0"))
        newtestscreen02_continue_button.place(x=270,
                                              y=10)

        def changeEntryDataExaminer():
            newtestscreen02_first_name_entry_unchanged_overlay_label.place_forget()
            newtestscreen02_last_name_entry_unchanged_overlay_label.place_forget()
            newtestscreen02_birth_date_entry_unchanged_overlay_label.place_forget()

            newtestscreen02_first_name_entry.configure(state="normal", placeholder_text="Vorname")
            newtestscreen02_last_name_entry.configure(state="normal", placeholder_text="Nachname")
            newtestscreen02_birth_date_entry.configure(state="normal", placeholder_text="dd.mm.yyyy")

            newtestscreen02_change_button.configure(state="disabled")
            newtestscreen02_save_button.configure(state="normal")
            newtestscreen02_continue_button.configure(state="disabled")

        def saveEntryDataExaminer():
            personal_infos_examiner = [newtestscreen02_first_name_entry.get(),
                                       newtestscreen02_last_name_entry.get(),
                                       newtestscreen02_birth_date_entry.get()]

            if (len(personal_infos_examiner[0].strip()) +
                    len(personal_infos_examiner[1].strip()) +
                    len(personal_infos_examiner[2].strip()) >= 14):
                newtestscreen02_continue_button.configure(state="normal")
                self.app.changeListInJson("personal_var", ("personal_infos_examiner_" + last_chosen_examiner),
                                          personal_infos_examiner)

                newtestscreen02_first_name_entry_unchanged_overlay_label.place(x=10, y=60)
                newtestscreen02_last_name_entry_unchanged_overlay_label.place(x=10, y=180)
                newtestscreen02_birth_date_entry_unchanged_overlay_label.place(x=10, y=300)
                updateLabels(personal_infos_examiner)

                newtestscreen02_first_name_entry.configure(state="disabled")
                newtestscreen02_last_name_entry.configure(state="disabled")
                newtestscreen02_birth_date_entry.configure(state="disabled")

                newtestscreen02_change_button.configure(state="normal")
                newtestscreen02_save_button.configure(state="disabled")
                newtestscreen02_continue_button.configure(state="normal")
            else:
                newtestscreen02_continue_button.configure(state="disabled")
                print("Date-Format wrong or the sum of first name plus surname not at least 4 digits")

        def updateLabels(infos):
            newtestscreen02_first_name_entry_unchanged_overlay_label.configure(text=infos[0])
            newtestscreen02_last_name_entry_unchanged_overlay_label.configure(text=infos[1])
            newtestscreen02_birth_date_entry_unchanged_overlay_label.configure(text=infos[2])
