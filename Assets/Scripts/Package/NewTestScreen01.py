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
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          width=window_geometry[0] - 70,
                                          height=window_geometry[1] / 20,
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 1:" +
                                                " Speicherort generierter Daten angeben"),
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", font_size),
                                          anchor="w")
        self.indicator_bar.place(x=0,
                                 y=0)

        # frame------------------------------------------------------------
        self.frame = ctk.CTkFrame(master=self,  # frame for the widgets
                                  width=window_geometry[0] - 80,
                                  height=window_geometry[1] / 15,
                                  corner_radius=20)
        self.frame.place(x=30,
                         y=window_geometry[1] / 15)

        # frame2------------------------------------------------------------
        self.frame2 = ctk.CTkFrame(master=self,  # frame for the widgets
                                   width=window_geometry[0] - 80,
                                   height=window_geometry[1] / 15,
                                   corner_radius=20)
        self.frame2.place(x=30,
                          y=window_geometry[1] / 6.5)

        self.help_label = ctk.CTkLabel(master=self.frame2,
                                       fg_color=GetStartupVariables.color_SET_blue,
                                       width=window_geometry[0] - 100,
                                       height=window_geometry[1] / 15 - 20,
                                       corner_radius=10,
                                       text="USB-Stick ist wahrscheinlich in /media/admin/; USB-Stick in schwarzen Port stecken!",
                                       text_color=GetStartupVariables.text_color_SET,
                                       font=("bold", font_size))
        self.help_label.place(x=10,
                              y=10)

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         width=40,
                                         height=window_geometry[1] / 20,
                                         corner_radius=10,
                                         text="",
                                         anchor="ne",
                                         image=back_arrow_image,
                                         command=lambda: self.master.confirm_go_back("0"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=GetStartupVariables.window_geometry[0] - 65,
                               y=0)

        # path choose------------------------------------------------------------
        self.path_label = ctk.CTkLabel(master=self.frame,
                                       fg_color=GetStartupVariables.color_SET_blue,
                                       width=window_geometry[0] / 20,
                                       height=window_geometry[1] / 15 - 20,
                                       corner_radius=10,
                                       text="Pfad:",
                                       text_color=GetStartupVariables.text_color_SET,
                                       font=("bold", font_size))
        self.path_label.place(x=10,
                              y=10)

        self.path_display_label_frame = ctk.CTkFrame(master=self.frame,
                                                     width=window_geometry[0] / 1.5,
                                                     height=window_geometry[1] / 15 - 20,
                                                     corner_radius=10)
        self.path_display_label_frame.place(x=window_geometry[0] / 13,
                                            y=10)

        self.path_display_label = ctk.CTkLabel(master=self.path_display_label_frame,
                                               width=window_geometry[0] / 1.5 - 20,
                                               height=window_geometry[1] / 15 - 20,
                                               text=GetStartupVariables.save_path,
                                               anchor="w",
                                               font=("bold", font_size))
        self.path_display_label.place(x=10,
                                      y=0)

        self.change_button = ctk.CTkButton(master=self.frame,  # back button
                                           width=window_geometry[0] / 15 - 30,
                                           height=window_geometry[1] / 15 - 20,
                                           fg_color=GetStartupVariables.color_SET_blue,
                                           corner_radius=10,
                                           text="...",
                                           command=self.change_path)
        self.change_button.place(x=window_geometry[0] / 1.325,
                                 y=10)

        self.continue_button = ctk.CTkButton(master=self.frame,  # back button
                                             width=window_geometry[0] / 9,
                                             height=window_geometry[1] / 15 - 20,
                                             fg_color=GetStartupVariables.color_SET_blue,
                                             font=("bold", font_size),
                                             corner_radius=10,
                                             text="Weiter",
                                             command=lambda: self.app.switch_window("1.1"))
        self.continue_button.place(x=window_geometry[0] / 1.24,
                                   y=10)

    def change_path(self):  # method to change the save-path
        GetStartupVariables.save_path = filedialog.askdirectory()
        self.path_display_label.configure(text=GetStartupVariables.save_path)

        json_writer("startup_var", "save_path", GetStartupVariables.save_path, main_pi_location + "../JSON/")
