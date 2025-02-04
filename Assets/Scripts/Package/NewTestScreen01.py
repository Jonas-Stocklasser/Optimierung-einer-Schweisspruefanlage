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


class NewTestScreen01(ctk.CTkFrame):  # class for the NewTestScreen01 window
    def __init__(self, parent, window_geometry):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         fg_color="transparent",
                         width=window_geometry[0] - 10,
                         height=window_geometry[1] - 10
                         )

        self.app = parent

        font_size = window_geometry[1] / 40
        back_arrow_image.configure(size=(font_size * 0.8, font_size * 0.8))

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=10,
                                          text="Neuer Test - Schritt 1:" +
                                               " Speicherort generierter Daten angeben",
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
                                         command=lambda: self.master.confirm_go_back("0"),
                                         width=font_size * 1.5,
                                         height=font_size * 1.5)
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=(window_geometry[0] - font_size * 1.5 - 25),
                               y=0)

        # frame------------------------------------------------------------
        self.frame = ctk.CTkFrame(master=self,  # frame for the widgets
                                  corner_radius=20,
                                  width=font_size * 45 + 20,
                                  height=font_size * 1.5 + 20
                                  )
        self.frame.place(x=0,
                         y=font_size * 2)

        # path choose------------------------------------------------------------
        self.path_label = ctk.CTkLabel(master=self.frame,
                                       fg_color=GetStartupVariables.color_SET_blue,
                                       corner_radius=10,
                                       text="Pfad:",
                                       text_color=GetStartupVariables.text_color_SET,
                                       font=("bold", font_size),
                                       width=window_geometry[0] / 15,
                                       height=font_size * 1.5)
        self.path_label.place(x=10,
                              y=10)

        self.path_display_label_frame = ctk.CTkFrame(master=self.frame,
                                                     corner_radius=10,
                                                     width=window_geometry[0] / 1.5,
                                                     height=font_size * 1.5)
        self.path_display_label_frame.place(x=window_geometry[0] / 15 + 20,
                                            y=10)

        self.path_display_label = ctk.CTkLabel(master=self.path_display_label_frame,
                                               text=GetStartupVariables.save_path,
                                               anchor="w",
                                               font=("bold", font_size),
                                               width=window_geometry[0] / 1.5 - 20,
                                               height=font_size * 1.5
                                               )
        self.path_display_label.place(x=10,
                                      y=0)

        self.change_button = ctk.CTkButton(master=self.frame,  # back button
                                           fg_color=GetStartupVariables.color_SET_blue,
                                           corner_radius=10,
                                           text="...",
                                           command=self.change_path,
                                           font=("bold", font_size),
                                           width=font_size * 1.5,
                                           height=font_size * 1.5)
        self.change_button.place(x=window_geometry[0] / 15 + 30 + window_geometry[0] / 1.5,
                                 y=10)

        self.continue_button = ctk.CTkButton(master=self.frame,  # back button
                                             fg_color=GetStartupVariables.color_SET_blue,
                                             font=("bold", font_size),
                                             corner_radius=10,
                                             text="Weiter",
                                             width=font_size * 3,
                                             height=font_size * 1.5,
                                             command=lambda: self.app.switch_window("1.1"))
        self.continue_button.place(x=window_geometry[0] / 15 + 40 + window_geometry[0] / 1.5 + font_size * 2,
                                   y=10)

        # frame2------------------------------------------------------------
        self.frame2 = ctk.CTkFrame(master=self,  # frame for the widgets
                                   corner_radius=20,
                                   width=window_geometry[0] / 1.35,
                                   height=font_size * 1.5 + 20)
        self.frame2.place(x=0,
                          y=font_size * 5)

        self.help_label = ctk.CTkLabel(master=self.frame2,
                                       fg_color=GetStartupVariables.color_SET_blue,
                                       corner_radius=10,
                                       text="USB-Stick ist wahrscheinlich in /media/admin/; USB-Stick in schwarzen Port stecken!",
                                       text_color=GetStartupVariables.text_color_SET,
                                       font=("bold", font_size),
                                       width=window_geometry[0] / 2,
                                       height=font_size * 1.5)
        self.help_label.place(x=10,
                              y=10)

    def change_path(self):  # method to change the save-path
        save_path = filedialog.askdirectory()
        if len(save_path) >= 1:
            self.path_display_label.configure(text=save_path)

            json_writer("startup_var", "save_path", save_path, main_pi_location + "../JSON/")
