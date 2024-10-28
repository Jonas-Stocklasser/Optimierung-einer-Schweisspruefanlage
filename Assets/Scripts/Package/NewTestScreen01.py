#!/usr/bin/python3
# Date: 26.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 1; ID=1.0

import customtkinter as ctk
from tkinter import messagebox
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location
from tkinter import filedialog
from .JsonFunctions import json_writer

window_geometry = GetStartupVariables.window_geometry
font_size = window_geometry[1] / 40


class NewTestScreen01(ctk.CTkFrame):  # class for the NewTestScreen01 window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         fg_color="transparent")

        # Grid configuration
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(tuple(range(1, 80)), weight=10)
        self.grid_columnconfigure(81, weight=3)
        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(tuple(range(1, 60)), weight=10)
        self.grid_rowconfigure(61, weight=4)

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=10,
                                          text="Neuer Test - Schritt 1:" +
                                                " Speicherort generierter Daten angeben",
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
                                         command=lambda: self.master.switch_window("0"))
        # the command doesn't call the switch_window method because there is no unsaved content to loose
        self.back_button.grid(row=1, column=78, columnspan=2, rowspan=1, sticky="nesw")

        # frame------------------------------------------------------------
        self.frame = ctk.CTkFrame(master=self,  # frame for the widgets
                                  corner_radius=10)
        self.frame.grid(row=4, column=2, columnspan=15, rowspan=4, sticky="nesw")

        # path choose------------------------------------------------------------
        self.path_label = ctk.CTkLabel(master=self.frame,
                                       fg_color=GetStartupVariables.color_SET_blue,
                                       corner_radius=10,
                                       text="Pfad:",
                                       text_color=GetStartupVariables.text_color_SET,
                                       font=("bold", font_size))
        #self.path_label.place(x=10,
         #                     y=10)

        self.path_display_label_frame = ctk.CTkFrame(master=self.frame,
                                                     corner_radius=10)
        #self.path_display_label_frame.place(x=window_geometry[0] / 13,
         #                                   y=10)

        self.path_display_label = ctk.CTkLabel(master=self.path_display_label_frame,
                                               text=GetStartupVariables.save_path,
                                               anchor="w",
                                               font=("bold", font_size))
        #self.path_display_label.place(x=10,
        #                              y=0)

        self.change_button = ctk.CTkButton(master=self.frame,  # back button
                                           fg_color=GetStartupVariables.color_SET_blue,
                                           corner_radius=10,
                                           text="...",
                                           command=self.change_path)
        #self.change_button.place(x=window_geometry[0] / 1.325,
         #                        y=10)

        self.continue_button = ctk.CTkButton(master=self.frame,  # back button
                                             fg_color=GetStartupVariables.color_SET_blue,
                                             font=("bold", font_size),
                                             corner_radius=10,
                                             text="Weiter",
                                             command=lambda: self.app.switch_window("1.1"))
        #self.continue_button.place(x=window_geometry[0] / 1.24,
           #                        y=10)

        # frame2------------------------------------------------------------
        self.frame2 = ctk.CTkFrame(master=self,  # frame for the widgets
                                   corner_radius=10)
        self.frame2.grid(row=5, column=2, columnspan=15, rowspan=4, sticky="nesw")

        self.help_label = ctk.CTkLabel(master=self.frame2,
                                       fg_color=GetStartupVariables.color_SET_blue,
                                       corner_radius=10,
                                       text="USB-Stick ist wahrscheinlich in /media/admin/; USB-Stick in schwarzen Port stecken!",
                                       text_color=GetStartupVariables.text_color_SET,
                                       font=("bold", font_size))
        self.help_label.place(relx=0.5, rely=0.5, anchor="center")

    def change_path(self):  # method to change the save-path
        GetStartupVariables.save_path = filedialog.askdirectory()
        self.path_display_label.configure(text=GetStartupVariables.save_path)

        json_writer("startup_var", "save_path", GetStartupVariables.save_path, main_pi_location + "../JSON/")

    def update_font_size(self, font_size):
        self.indicator_bar.configure(font=("bold", font_size), height=font_size)
        self.back_button.configure(width=font_size,
                                   height=font_size)
        back_arrow_image.configure(size=(font_size, font_size))
        self.help_label.configure(font=("bold", font_size), height=font_size)
