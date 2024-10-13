#!/usr/bin/python3
# Date: 30.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Test Vorbereitung 1; ID=2.0

import customtkinter as ctk
import tkinter as tk
from .JsonFunctions import json_reader, json_writer
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetExamParameterVariables, back_arrow_image


class TestPreparations01(ctk.CTkFrame):  # class for the TestPreparations window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(GetStartupVariables.window_geometry[0] - 10),
                         height=(GetStartupVariables.window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        # self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   # y=5)

        # top bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          width=GetStartupVariables.window_geometry[0] - 70,
                                          height=40,
                                          corner_radius=10,
                                          text=("Testvorbereitung - Schritt 1:" +
                                                " ---"),
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
                                             "1.5"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=GetStartupVariables.window_geometry[0] - 65,
                               y=0)

        # text_frame------------------------------------------------------------
        self.left_frame = ctk.CTkFrame(master=self,  # frame for the text
                                       width=500,
                                       height=605,
                                       corner_radius=20)
        self.left_frame.place(x=30,
                              y=75)

        self.text_frame = ctk.CTkFrame(master=self.left_frame,  # frame for the text
                                       width=480,
                                       height=525,
                                       corner_radius=10)
        self.text_frame.place(x=10,
                              y=10)

        # image_frame------------------------------------------------------------
        self.right_frame = ctk.CTkFrame(master=self,  # frame for the image
                                        width=500,
                                        height=605,
                                        corner_radius=20)
        self.right_frame.place(x=580,
                               y=75)

        # continue_button------------------------------------------------------------
        self.continue_button = ctk.CTkButton(master=self.left_frame,
                                             # continue button
                                             width=100,
                                             height=50,
                                             corner_radius=10,
                                             text="Weiter",
                                             font=("bold", 20),
                                             state="normal",
                                             command=self.continue_button_function)
        self.continue_button.place(x=10,
                                   y=545)

        self.instruction_label = ctk.CTkLabel(master=self.text_frame,
                                              width=450,
                                              height=505,
                                              text="Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - \n"
                                                   "Instruction Placeholder - Instruction Placeholder - ",
                                              anchor="nw",
                                              font=("bold", 20))
        self.instruction_label.place(x=15,
                                     y=10)

    def continue_button_function(self):
        self.master.switch_window("0")
