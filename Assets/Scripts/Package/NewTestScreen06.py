#!/usr/bin/python3
# Date: 29.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 6; ID=1.5

import customtkinter as ctk
import tkinter as tk
import math
from .JsonFunctions import json_reader, json_writer
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetExamParameterVariables, back_arrow_image, main_pi_location

window_geometry = GetStartupVariables.window_geometry
font_size = window_geometry[1] / 40


class NewTestScreen06(ctk.CTkFrame):  # class for the NewTestScreen06 window
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
                                          text=("Neuer Test - Schritt 6:" +
                                                " Prüfparameter einstellen"),
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
                                         command=lambda: self.master.confirm_go_back("1.4"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.grid(row=1, column=78, columnspan=2, rowspan=1, sticky="nesw")

        # options menu parameter------------------------------------------------------------
        self.parameter_option_menu_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                        corner_radius=10)
        self.parameter_option_menu_frame.grid(row=4, column=2, columnspan=15, rowspan=2, sticky="nesw")

        # Grid configuration
        self.parameter_option_menu_frame.grid_columnconfigure(0, weight=3)
        self.parameter_option_menu_frame.grid_columnconfigure(1, weight=20)
        self.parameter_option_menu_frame.grid_columnconfigure(2, weight=3)
        self.parameter_option_menu_frame.grid_columnconfigure(3, weight=20)
        self.parameter_option_menu_frame.grid_columnconfigure(4, weight=3)
        self.parameter_option_menu_frame.grid_rowconfigure(0, weight=3)
        self.parameter_option_menu_frame.grid_rowconfigure(1, weight=10)
        self.parameter_option_menu_frame.grid_rowconfigure(2, weight=3)

        self.parameter_option_menu_label = ctk.CTkLabel(
            master=self.parameter_option_menu_frame,
            fg_color=GetStartupVariables.color_SET_blue,
            corner_radius=10,
            text="Voreinstellungen",
            text_color=GetStartupVariables.text_color_SET,
            font=("bold", font_size))
        self.parameter_option_menu_label.grid(row=1, column=1, columnspan=1, rowspan=1, sticky="nesw")

        self.options_menu_parameter = ctk.CTkOptionMenu(master=self.parameter_option_menu_frame,
                                                        font=("bold", font_size),
                                                        dropdown_font=("bold", font_size),
                                                        corner_radius=5,
                                                        variable=tk.StringVar(
                                                            value=GetExamParameterVariables.last_chosen_parameter_list),
                                                        values=GetExamParameterVariables.parameter_list_indexes,
                                                        command=self.parameter_list_select)
        # the command automatically passes the current value as an argument to the specified method
        self.options_menu_parameter.grid(row=1, column=3, columnspan=1, rowspan=1, sticky="new")
        # entry frame------------------------------------------------------------
        self.entry_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                        corner_radius=20)
        self.entry_frame.grid(row=8, column=2, columnspan=10, rowspan=3, sticky="nesw")

        # Grid configuration
        self.entry_frame.grid_columnconfigure(0, weight=10)
        self.entry_frame.grid_columnconfigure(tuple(range(1, 80)), weight=10)
        self.entry_frame.grid_columnconfigure(81, weight=10)
        self.entry_frame.grid_rowconfigure(0, weight=4)
        self.entry_frame.grid_rowconfigure(tuple(range(1, 49)), weight=10)
        self.entry_frame.grid_rowconfigure(50, weight=4)

        # pressure entry------------------------------------------------------------
        self.pressure_entry_label = ctk.CTkLabel(master=self.entry_frame,
                                                 fg_color=GetStartupVariables.color_SET_blue,
                                                 corner_radius=10,
                                                 text="Maximaler Prüfdruck",
                                                 text_color=GetStartupVariables.text_color_SET,
                                                 font=("bold", font_size))
        self.pressure_entry_label.grid(row=10, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.pressure_entry = ctk.CTkEntry(master=self.entry_frame,
                                           font=("bold", font_size),
                                           state="disabled"
                                           )
        self.pressure_entry.grid(row=15, column=20, columnspan=2, rowspan=1, sticky="nesw")

        self.pressure_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame,
                                                                         corner_radius=10)
        self.pressure_entry_unchanged_overlay_label_frame.grid(row=15, column=20, columnspan=2, rowspan=1,
                                                               sticky="nesw")

        self.pressure_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.pressure_entry_unchanged_overlay_label_frame,
            anchor="w",
            text=f"{GetExamParameterVariables.parameter_list} bar",
            font=("bold", font_size))
        self.pressure_entry_unchanged_overlay_label.place(relx=0.1,
                                                          rely=0.3)

        # change, save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=20)
        self.button_frame.grid(row=13, column=2, columnspan=18, rowspan=2, sticky="nesw")

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
                                           command=lambda: self.change_entry_data_exam_parameter())
        self.change_button.grid(row=1, column=1, columnspan=1, rowspan=1, sticky="nesw")

        self.save_button = ctk.CTkButton(master=self.button_frame,  # save button
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", font_size),
                                         state="disabled",
                                         command=lambda: self.save_entry_data_exam_parameter())
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
        self.master.switch_window("2.0")
        self.write_personal_json()

    def change_entry_data_exam_parameter(self):
        self.pressure_entry_unchanged_overlay_label.place_forget()
        self.pressure_entry_unchanged_overlay_label_frame.grid_forget()

        self.pressure_entry.configure(state="normal", placeholder_text="Druck in Bar")

        self.change_button.configure(state="disabled")
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

    def save_entry_data_exam_parameter(self):
        parameter_list = self.pressure_entry.get()
        last_chosen_parameter_list = json_reader("exam_parameter_var", "last_chosen_parameter_list",
                                                 main_pi_location + "../JSON/")

        if len(parameter_list) >= 2:
            self.continue_button.configure(state="normal")
            json_writer("exam_parameter_var", ("parameter_list_" + last_chosen_parameter_list),
                        parameter_list, main_pi_location + "../JSON/")

            self.pressure_entry_unchanged_overlay_label_frame.grid(row=15, column=20, columnspan=2, rowspan=1,
                                                                   sticky="nesw")
            self.pressure_entry_unchanged_overlay_label.place(relx=0.1,
                                                              rely=0.3)
            self.update_labels(parameter_list)

            self.pressure_entry.configure(state="disabled")

            self.change_button.configure(state="normal")
            self.save_button.configure(state="disabled")
            self.continue_button.configure(state="normal")
        else:
            self.continue_button.configure(state="disabled")
            print("Entry to short, 3 characters min.")

    def update_labels(self, infos):
        self.pressure_entry_unchanged_overlay_label.configure(text=f"{infos} bar")

    def parameter_list_select(self, which):
        json_writer("exam_parameter_var", "last_chosen_parameter_list", which, main_pi_location + "../JSON/")
        parameter_list = json_reader("exam_parameter_var", f"parameter_list_{which}", main_pi_location + "../JSON/")
        self.update_labels(parameter_list)

    @staticmethod
    def write_personal_json():
        last_chosen_parameter_list = json_reader("exam_parameter_var", "last_chosen_parameter_list",
                                                 main_pi_location + "../JSON/")
        parameter_list = json_reader("exam_parameter_var", f"parameter_list_{last_chosen_parameter_list}",
                                     main_pi_location + "../JSON/")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
        json_writer(personal_json_name, "exam_parameter", parameter_list, personal_folder_path)

    def update_size(self, font_size):
        self.indicator_bar.configure(font=("bold", font_size), height=font_size)
        self.back_button.configure(width=font_size,
                                   height=font_size)
        back_arrow_image.configure(size=(font_size, font_size))

        self.pressure_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5)
        self.pressure_entry.configure(font=("bold", math.ceil(font_size) - 4))
        self.pressure_entry_unchanged_overlay_label.configure(font=("bold", font_size), height=font_size * 1,
                                                           width=font_size * 9)
        self.pressure_entry_unchanged_overlay_label_frame.configure(height=font_size * 2,
                                                                 width=font_size * 10)
        self.button_frame.configure(height=font_size*2)
        self.change_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4)
        self.save_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4)
        self.continue_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4)

        self.parameter_option_menu_frame.configure(height=font_size * 2)
        self.parameter_option_menu_label.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4)
        self.options_menu_parameter.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4)
