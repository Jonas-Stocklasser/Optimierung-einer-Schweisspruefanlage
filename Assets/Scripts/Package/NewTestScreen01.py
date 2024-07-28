#!/usr/bin/python3
# Date: 26.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 1; ID=1.0

import customtkinter as ctk
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image
from tkinter import filedialog
from .JsonFunctions import json_writer


class NewTestScreen01(ctk.CTkFrame):  # class for the NewTestScreen window
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
                                          text=("Neuer Test - Schritt 1:" +
                                                " Speicherort generierter Daten angeben"),
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", 20),
                                          anchor="w")
        self.indicator_bar.place(x=0,
                                 y=0)

        # button frame------------------------------------------------------------
        self.frame = ctk.CTkFrame(master=self,  # frame for the widgets
                                  width=1110,
                                  height=60)
        self.frame.place(x=30,
                         y=75)

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         width=40,
                                         height=40,
                                         corner_radius=10,
                                         text="",
                                         anchor="ne",
                                         image=back_arrow_image,
                                         command=lambda: self.master.open_top_level_window_really_switch(
                                             "0"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=GetStartupVariables.window_geometry[0] - 65,
                               y=0)

        # path choose------------------------------------------------------------
        self.path_label = ctk.CTkLabel(master=self.frame,
                                       fg_color=GetStartupVariables.color_SET_blue,
                                       width=100,
                                       height=40,
                                       corner_radius=10,
                                       text="Pfad:",
                                       text_color=GetStartupVariables.text_color_SET,
                                       font=("bold", 20))
        self.path_label.place(x=10,
                              y=10)

        self.path_display_label = ctk.CTkLabel(master=self.frame,
                                               fg_color=GetStartupVariables.color_SET_gray,
                                               width=820,
                                               height=40,
                                               corner_radius=10,
                                               text=GetStartupVariables.save_path,
                                               anchor="w",
                                               text_color=GetStartupVariables.text_color_SET,
                                               font=("bold", 20))
        self.path_display_label.place(x=120,
                                      y=10)

        self.change_button = ctk.CTkButton(master=self.frame,  # back button
                                           width=40,
                                           height=40,
                                           fg_color=GetStartupVariables.color_SET_blue,
                                           corner_radius=10,
                                           text="...",
                                           command=self.change_path)
        self.change_button.place(x=950,
                                 y=10)

        self.continue_button = ctk.CTkButton(master=self.frame,  # back button
                                             width=100,
                                             height=40,
                                             fg_color=GetStartupVariables.color_SET_blue,
                                             font=("bold", 20),
                                             corner_radius=10,
                                             text="Weiter",
                                             command=lambda: self.app.switch_window("1.1"))
        self.continue_button.place(x=1000,
                                   y=10)

    def change_path(self):
        GetStartupVariables.save_path = filedialog.askdirectory()
        self.path_display_label.configure(text=GetStartupVariables.save_path)

        json_writer("startup_var", "save_path", GetStartupVariables.save_path, "../Other/")
