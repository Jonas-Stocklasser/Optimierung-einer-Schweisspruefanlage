#!/usr/bin/python3
# Date: 28.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 5; ID=1.4
from tkinter import messagebox

import customtkinter as ctk
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location
from .JsonFunctions import json_writer, json_reader

font_size = 0.1

class NewTestScreen05(ctk.CTkFrame):  # class for the NewTestScreen05 window
    def __init__(self, parent, window_geometry):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        global font_size

        self.app = parent

        font_size = window_geometry[1] / 40
        back_arrow_image.configure(size=(font_size * 0.8, font_size * 0.8))

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 5:" +
                                                " Visuelle Beurteilung des Prüfstücks und der Schweißverbindungen"),
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", font_size),
                                          anchor="w",
                                          width=window_geometry[0] - 30 - font_size * 1.5,
                                          height=font_size * 1.5)
        self.indicator_bar.place(x=0,
                                 y=0)

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         corner_radius=10,
                                         text="",
                                         anchor="center",
                                         image=back_arrow_image,
                                         command=lambda: self.master.confirm_go_back("1.3"),
                                         width=font_size * 1.5,
                                         height=font_size * 1.5)
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=(window_geometry[0] - font_size * 1.5 - 25),
                               y=0)

        # option frame ------------------------------------------------------------
        self.option_frame = ctk.CTkFrame(master=self,  # frame for the textbox
                                         corner_radius=20,
                                         width=window_geometry[0] / 1.5,
                                         height=window_geometry[1] / 1.3)
        self.option_frame.place(x=0,
                                y=font_size * 2)

        # visual grading options
        self.schweisswulst_label = ctk.CTkLabel(master=self.option_frame,
                                                fg_color=GetStartupVariables.color_SET_blue,
                                                corner_radius=10,
                                                text="Schweißwulst",
                                                text_color=GetStartupVariables.text_color_SET,
                                                font=("bold", font_size),
                                                width=font_size * 20,
                                                height=font_size * 1.5)
        self.schweisswulst_label.place(x=10,
                                       y=10)

        self.schweisswulst_checkbox_ok = ctk.CTkCheckBox(master=self.option_frame,
                                                         width=font_size * 1.5,
                                                         height=font_size * 1.5,
                                                         corner_radius=5,
                                                         text="OK",
                                                         offvalue="",
                                                         onvalue="OK",
                                                         font=("bold", font_size),
                                                         command=lambda: self.schweisswulst_ok_function())
        self.schweisswulst_checkbox_ok.place(x=10,
                                             y=20 + font_size * 1.5)

        self.schweisswulst_checkbox_not_ok = ctk.CTkCheckBox(master=self.option_frame,
                                                             width=font_size * 1.5,
                                                             height=font_size * 1.5,
                                                             corner_radius=5,
                                                             text="Fehler",
                                                             offvalue="",
                                                             onvalue="Fehler",
                                                             font=("bold", font_size),
                                                             command=lambda: self.schweisswulst_not_ok_function())
        self.schweisswulst_checkbox_not_ok.place(x=10 + font_size * 5,
                                                 y=20 + font_size * 1.5)

        self.schweisswulst_not_ok_entry = ctk.CTkEntry(master=self.option_frame,
                                                       font=("bold", font_size),
                                                       state="disabled",
                                                       width=font_size * 20,
                                                       height=font_size * 1.5
                                                       )
        self.schweisswulst_not_ok_entry.place(x=20 + font_size * 10,
                                              y=20 + font_size * 1.5)

        # save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=20,
                                         height=font_size * 1.5 + 20,
                                         width=font_size * 6 + 20 + font_size * 5 + 10)
        self.button_frame.place(x=0,
                                y=font_size * 2 + window_geometry[1] / 1.3 + 10)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", font_size),
                                         state="normal",
                                         command=lambda: self.save_textbox_data(),
                                         height=font_size * 1.5,
                                         width=font_size * 6)
        self.save_button.place(x=10,
                               y=10)

        self.continue_button = ctk.CTkButton(master=self.button_frame,
                                             # continue button
                                             corner_radius=10,
                                             text="Weiter",
                                             font=("bold", font_size),
                                             state="disabled",
                                             command=lambda: self.master.switch_window("1.5"),
                                             height=font_size * 1.5,
                                             width=font_size * 5)
        self.continue_button.place(x=font_size * 6 + 20,
                                   y=10)

    def save_textbox_data(self):
        visual_grade = self.textbox.get("1.0", "end")

        if visual_grade != "\n" and visual_grade != "Visuelle Einschätzung des Prüfers eingeben...\n" and visual_grade != "Visuelle Einschätzung des Prüfers eingeben...":
            self.continue_button.configure(state="normal")
            if visual_grade.startswith("Visuelle Einschätzung des Prüfers eingeben..."):
                visual_grade = visual_grade[len("Visuelle Einschätzung des Prüfers eingeben..."):].strip()
            personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
            personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
            json_writer(personal_json_name, "visual_grade", visual_grade, personal_folder_path)
        else:
            messagebox.showinfo("Eingabefehler", "Bitte geben Sie etwas ein!")
            print("Type something! An empty field is not permitted!")

    def reset_input_new_test(self):
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", "Visuelle Einschätzung des Prüfers eingeben...")
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

    def schweisswulst_ok_function(self):
        self.schweisswulst_checkbox_not_ok.deselect()
        self.schweisswulst_not_ok_entry.configure(state="disabled")

    def schweisswulst_not_ok_function(self):
        global font_size
        self.schweisswulst_checkbox_ok.deselect()
        self.schweisswulst_not_ok_entry.configure(state="normal",
                                                  placeholder_text="Kurzbeschreibung des Fehlers",
                                                  font=("bold", font_size))
