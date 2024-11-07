#!/usr/bin/python3
# Date: 30.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Test Vorbereitung 1; ID=2.0

import customtkinter as ctk
import tkinter as tk
from .JsonFunctions import json_reader, json_writer
import RPi.GPIO as GPIO
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetExamParameterVariables, back_arrow_image

window_geometry = GetStartupVariables.window_geometry
font_size = window_geometry[1] / 40
key_held = False


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, False)

class TestPreparations01(ctk.CTkFrame):  # class for the TestPreparations01 window
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
                                          corner_radius=font_size / 2,
                                          text=("Testvorbereitung - Schritt 1:" +
                                                " Anweisungen befolgen und entlüften"),
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", font_size),
                                          anchor="center")
        self.indicator_bar.grid(row=1, column=1, columnspan=77, rowspan=1, sticky="nesw")

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         corner_radius=font_size / 2,
                                         text="",
                                         anchor="center",
                                         image=back_arrow_image,
                                         command=lambda: self.master.confirm_go_back("1.5"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.grid(row=1, column=78, columnspan=2, rowspan=1, sticky="nesw")

        # text_frame------------------------------------------------------------
        self.left_frame = ctk.CTkFrame(master=self,  # frame for the text
                                       corner_radius=font_size / 2)
        self.left_frame.grid(row=4, column=3, columnspan=35, rowspan=50, sticky="nesw")

        # Grid configuration
        self.left_frame.grid_columnconfigure(0, weight=3)
        self.left_frame.grid_columnconfigure(tuple(range(1, 80)), weight=10)
        self.left_frame.grid_columnconfigure(81, weight=3)
        self.left_frame.grid_rowconfigure(0, weight=4)
        self.left_frame.grid_rowconfigure(tuple(range(1, 60)), weight=10)
        self.left_frame.grid_rowconfigure(61, weight=4)

        self.text_frame = ctk.CTkFrame(master=self.left_frame,  # frame for the text
                                       corner_radius=font_size / 2)
        self.text_frame.grid(row=5, column=10, columnspan=60, rowspan=45, sticky="nesw")

        # image_frame------------------------------------------------------------
        self.right_frame = ctk.CTkFrame(master=self,  # frame for the image
                                        corner_radius=font_size / 2)
        self.right_frame.grid(row=4, column=41, columnspan=35, rowspan=50, sticky="nesw")

        # continue_button------------------------------------------------------------
        self.continue_button = ctk.CTkButton(master=self.left_frame,
                                             # continue button
                                             corner_radius=font_size / 2,
                                             text="Weiter",
                                             font=("bold", font_size),
                                             state="normal",
                                             command=self.continue_button_function)
        self.continue_button.grid(row=55, column=10, columnspan=10, rowspan=2, sticky="nesw")

        self.instruction_label = ctk.CTkLabel(master=self.text_frame,
                                              text="Anweisungen des ausgedruckten\nDokuments befolgen\n"
                                                   "1. Prüfstück mit Wasser füllen\n"
                                                   "2. Flansch auf Prüfstück aufsetzen\n"
                                                   "3. Prüfstück am Flansch aufhängen\n"
                                                   "4. Prüfstück entlüften\n"
                                                   "5. Prüfstück in das Becken hinablassen\n"
                                                   "6. Prüfvorgang starten (erst nach Entlüftung!)\n"
                                                   "\n"
                                                   "-----------------------------------------------------------\n"
                                                   "Pumpe toggeln - ENTER\n"
                                                   "-----------------------------------------------------------\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "\n",
                                              anchor="n",
                                              font=("bold", font_size))
        self.instruction_label.place(relx=0.01,
                                     rely=0.01)

    def continue_button_function(self):
        self.master.switch_window("4.0")

    def update_size(self, font_size):
        self.indicator_bar.configure(font=("bold", font_size), height=font_size, corner_radius=font_size / 2)
        self.back_button.configure(width=font_size,
                                   height=font_size, corner_radius=font_size / 2)
        back_arrow_image.configure(size=(font_size, font_size), corner_radius=font_size / 2)
        self.continue_button.configure(font=("bold", font_size), width=font_size * 3, height=font_size * 1.5,
                                       corner_radius=font_size / 2)
        self.instruction_label.configure(font=("bold", font_size * 0.9), corner_radius=font_size / 2)

    @staticmethod
    def unair_on():
        global key_held
        if not key_held:
            print("Entlüftung start")
            # GPIO.output(14, True)
            key_held = True

    @staticmethod
    def unair_off():
        global key_held
        if key_held:
            print("Entlüftung ende")
            # GPIO.output(14, False)
            key_held = False
