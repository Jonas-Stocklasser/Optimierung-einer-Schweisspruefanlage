#!/usr/bin/python3
# Date: 29.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 6; ID=1.5

import customtkinter as ctk
import tkinter as tk
from .JsonFunctions import json_reader, json_writer
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetExamParameterVariables, back_arrow_image


class NewTestScreen06(ctk.CTkFrame):  # class for the NewTestScreen window
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
                                          text=("Neuer Test - Schritt 6:" +
                                                " Prüfparameter einstellen"),
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
                                             "1.4"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=GetStartupVariables.window_geometry[0] - 65,
                               y=0)

        # options menu parameter------------------------------------------------------------
        self.parameter_option_menu_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                        width=340,
                                                        height=70,
                                                        corner_radius=20)
        self.parameter_option_menu_frame.place(x=30,
                                               y=75)

        self.parameter_option_menu_label = ctk.CTkLabel(
            master=self.parameter_option_menu_frame,
            fg_color=GetStartupVariables.color_SET_blue,
            width=200,
            height=50,
            corner_radius=10,
            text="Voreinstellungen",
            text_color=GetStartupVariables.text_color_SET,
            font=("bold", 20))
        self.parameter_option_menu_label.place(x=10,
                                               y=10)

        self.options_menu_parameter = ctk.CTkOptionMenu(master=self.parameter_option_menu_frame,
                                                        width=100,
                                                        height=50,
                                                        font=("bold", 20),
                                                        dropdown_font=("bold", 20),
                                                        corner_radius=5,
                                                        variable=tk.StringVar(
                                                            value=GetExamParameterVariables.last_chosen_parameter_list),
                                                        values=GetExamParameterVariables.parameter_list_indexes,
                                                        command=self.parameter_list_select)
        # the command automatically passes the current value as an argument to the specified method
        self.options_menu_parameter.place(x=230,
                                          y=10)
        # entry frame------------------------------------------------------------
        self.entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                        width=340,
                                        height=240,
                                        corner_radius=20)
        self.entry_frame.place(x=30,
                               y=175)

        # pressure entry------------------------------------------------------------
        self.pressure_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                 fg_color=GetStartupVariables.color_SET_blue,
                                                 width=100,
                                                 height=40,
                                                 corner_radius=10,
                                                 text="Maximaler Prüfdruck",
                                                 text_color=GetStartupVariables.text_color_SET,
                                                 font=("bold", 20))
        self.pressure_entry_label.place(x=10,
                                        y=10)

        self.pressure_entry = ctk.CTkEntry(master=self.entry_frame,
                                           width=250,
                                           height=50,
                                           font=("bold", 20),
                                           state="disabled"
                                           )
        self.pressure_entry.place(x=10,
                                  y=60)

        self.pressure_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                         width=250,
                                                                         height=50,
                                                                         corner_radius=10)
        self.pressure_entry_unchanged_overlay_label_frame.place(x=10,
                                                                y=60)

        self.pressure_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.pressure_entry_unchanged_overlay_label_frame,
            width=230,
            height=50,
            anchor="w",
            text=f"{GetExamParameterVariables.parameter_list[0]} bar",
            font=("bold", 20))
        self.pressure_entry_unchanged_overlay_label.place(x=10,
                                                          y=0)

        # duration entry------------------------------------------------------------
        self.duration_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                 fg_color=GetStartupVariables.color_SET_blue,
                                                 width=100,
                                                 height=40,
                                                 corner_radius=10,
                                                 text="Maximale Prüfdauer",
                                                 text_color=GetStartupVariables.text_color_SET,
                                                 font=("bold", 20))
        self.duration_entry_label.place(x=10,
                                        y=130)

        self.duration_entry = ctk.CTkEntry(master=self.entry_frame,
                                           width=250,
                                           height=50,
                                           font=("bold", 20),
                                           state="disabled"
                                           )
        self.duration_entry.place(x=10,
                                  y=180)

        self.duration_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                         width=250,
                                                                         height=50,
                                                                         corner_radius=10)
        self.duration_entry_unchanged_overlay_label_frame.place(x=10,
                                                                y=180)

        self.duration_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.duration_entry_unchanged_overlay_label_frame,
            width=230,
            height=50,
            anchor="w",
            text=f"{GetExamParameterVariables.parameter_list[1]} min",
            font=("bold", 20))
        self.duration_entry_unchanged_overlay_label.place(x=10,
                                                          y=0)

        # save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         width=380,
                                         height=70,
                                         corner_radius=20)
        self.button_frame.place(x=30,
                                y=450)

        self.change_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                           width=120,
                                           height=50,
                                           corner_radius=10,
                                           text="Ändern",
                                           font=("bold", 20),
                                           state="normal",
                                           command=lambda: self.change_entry_data_exam_parameter())
        self.change_button.place(x=10,
                                 y=10)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # save button
                                         width=120,
                                         height=50,
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", 20),
                                         state="disabled",
                                         command=lambda: self.save_entry_data_exam_parameter())
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
        self.master.switch_window("2.0")
        self.write_personal_json()

    def change_entry_data_exam_parameter(self):
        self.pressure_entry_unchanged_overlay_label.place_forget()
        self.pressure_entry_unchanged_overlay_label_frame.place_forget()
        self.duration_entry_unchanged_overlay_label.place_forget()
        self.pressure_entry_unchanged_overlay_label_frame.place_forget()

        self.pressure_entry.configure(state="normal", placeholder_text="Druck in Bar")
        self.duration_entry.configure(state="normal", placeholder_text="Maximale Dauer in Minuten")

        self.change_button.configure(state="disabled")
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

    def save_entry_data_exam_parameter(self):
        parameter_list = [self.pressure_entry.get(),
                          self.duration_entry.get()]
        last_chosen_parameter_list = json_reader("exam_parameter_var", "last_chosen_parameter_list", "../Other/")

        if (len(parameter_list[0].strip()) +
                len(parameter_list[1].strip()) >= 3):
            self.continue_button.configure(state="normal")
            json_writer("exam_parameter_var", ("parameter_list_" + last_chosen_parameter_list),
                        parameter_list, "../Other/")

            self.pressure_entry_unchanged_overlay_label_frame.place(x=10, y=60)
            self.pressure_entry_unchanged_overlay_label.place(x=10, y=0)
            self.duration_entry_unchanged_overlay_label_frame.place(x=10, y=180)
            self.duration_entry_unchanged_overlay_label.place(x=10, y=0)
            self.update_labels(parameter_list)

            self.pressure_entry.configure(state="disabled")
            self.duration_entry.configure(state="disabled")

            self.change_button.configure(state="normal")
            self.save_button.configure(state="disabled")
            self.continue_button.configure(state="normal")
        else:
            self.continue_button.configure(state="disabled")
            print("Entry to short, 3 characters min.")

    def update_labels(self, infos):
        self.pressure_entry_unchanged_overlay_label.configure(text=f"{infos[0]} bar")
        self.duration_entry_unchanged_overlay_label.configure(text=f"{infos[1]} min")

    def parameter_list_select(self, which):
        json_writer("exam_parameter_var", "last_chosen_parameter_list", which, "../Other/")
        parameter_list = json_reader("exam_parameter_var", f"parameter_list_{which}", "../Other/")
        self.update_labels(parameter_list)

    @staticmethod
    def write_personal_json():
        last_chosen_parameter_list = json_reader("exam_parameter_var", "last_chosen_parameter_list", "../Other/")
        parameter_list = json_reader("exam_parameter_var", f"parameter_list_{last_chosen_parameter_list}",
                                     "../Other/")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", "../Other/")
        personal_json_name = json_reader("personal_var", "personal_json_name", "../Other/")
        json_writer(personal_json_name, "exam_parameter", parameter_list, personal_folder_path)
