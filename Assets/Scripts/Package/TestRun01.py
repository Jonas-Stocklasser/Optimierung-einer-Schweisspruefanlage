#!/usr/bin/python3
# Date: 30.09.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Test Run 1; ID=4.0

import customtkinter as ctk
import random
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .JsonFunctions import json_reader, json_writer
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location, w1temp_location

from ina219 import INA219

timer_id = None

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, False)
output = 0

ina = INA219(shunt_ohms=0.1,
             max_expected_amps=0.6,
             address=0x40,
             busnum=1)

ina.configure(voltage_range=ina.RANGE_16V,
              gain=ina.GAIN_AUTO,
              bus_adc=ina.ADC_128SAMP,
              shunt_adc=ina.ADC_128SAMP)

pressure_values = []
temperature_values = []
test_timesteps = []


class TestRun01(ctk.CTkFrame):  # class for the TestRun01 window
    def __init__(self, parent, window_geometry):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        font_size = window_geometry[1] / 40
        back_arrow_image.configure(size=(font_size * 0.8, font_size * 0.8))

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          corner_radius=10,
                                          text="Testdurchlauf",
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
                                         command=lambda: self.master.confirm_go_back("2.0"),
                                         width=font_size * 1.5,
                                         height=font_size * 1.5)
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=(window_geometry[0] - font_size * 1.5 - 25),
                               y=0)

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=20,
                                         height=font_size * 1.5 + 20,
                                         width=window_geometry[0] / 7.4)
        self.button_frame.place(x=0,
                                y=font_size * 2)

        # start button------------------------------------------------------------
        self.start_button = ctk.CTkButton(master=self.button_frame,  # start button
                                          corner_radius=10,
                                          text="Start",
                                          font=("bold", font_size),
                                          state="normal",
                                          command=lambda: self.start_button_function(),
                                          width=font_size * 1.5,
                                          height=font_size * 1.5)
        self.start_button.place(x=10,
                                y=10)

        # stop button------------------------------------------------------------
        self.stop_button = ctk.CTkButton(master=self.button_frame,  # stop button
                                         corner_radius=10,
                                         text="Stop",
                                         font=("bold", font_size),
                                         state="disabled",
                                         command=lambda: self.stop_button_function(),
                                         width=font_size * 1.5,
                                         height=font_size * 1.5)
        self.stop_button.place(x=font_size * 3 + 20,
                               y=10)

        # mathplot
        self.figure, self.ax = plt.subplots(figsize=(font_size / 2, font_size / 3.8))
        self.ax.set_title("Überdruckverlauf (letzte 60 Sekunden)")
        self.ax.set_xlabel("Testzeit [s]")
        self.ax.set_ylabel("Druck [Bar]")

        # Embedding the matplotlib plot into tkinter using FigureCanvasTkAgg
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().place(x=0, y=font_size * 5)

    def to_do(self):
        print("Measure")
        global timer_id
        global pressure_values
        global temperature_values
        global test_timesteps

        if test_timesteps == []:
            test_timesteps = [1]
        else:
            last_entry = test_timesteps[len(test_timesteps) - 1]
            last_entry += 1
            test_timesteps.append(last_entry)

        temperature = self.get_temperature_w1()
        pressure_current = ina.current()
        # pressure_current = 15 # only in use while testing with pycharm
        # Pressure Calculation
        MBEWe = 60  # Messbereichsendwert Druck in Bar
        MBAWe = 0  # Messbereichsanfangswert Druck in Bar
        MBe = MBEWe - MBAWe  # Messbereich Druckin Bar
        MBEWa = 20  # Messbereichsendwert Strom in mA
        MBAWa = 4  # Messbereichsanfangswert Strom in mA
        MBa = MBEWa - MBAWa  # Messbereich Strom in mA

        pressure = (MBe / MBa) * (pressure_current - MBAWa) + MBAWe

        if pressure >= 0.1:
            GPIO.output(14, True)
        else:
            GPIO.output(14, False)

        print(f"Pressure = {pressure}")
        pressure_values.append(pressure)
        temperature_values.append(temperature)

        self.update_plot()

        timer_id = self.after(1000, self.to_do)
        self.write_personal_json()

    def start_button_function(self):
        global timer_id
        timer_id = self.after(1000, self.to_do)
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        print("Started")

    def stop_button_function(self):
        global timer_id
        self.after_cancel(timer_id)
        timer_id = None
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")

    def update_plot(self):
        # Limit to last 60 values
        display_timesteps = test_timesteps[-60:]
        display_pressures = pressure_values[-60:]

        # Clear the previous plot
        self.ax.clear()
        self.ax.set_title("Überdruckverlauf (letzte 60 Sekunden)")
        self.ax.set_xlabel("Testzeit [s]")
        self.ax.set_ylabel("Druck [Bar]")

        # Plot the new data
        self.ax.plot(display_timesteps, display_pressures, color='blue')

        # Redraw the canvas to update the plot
        self.canvas.draw()

    def get_temperature_w1(self):
        f = open(w1temp_location, "r")
        lines = f.readlines()
        f.close()
        temp_pos = lines[1].find("t=")
        if temp_pos != 1:
            temperature = float(int(lines[1][temp_pos + 2:]) / 1000)
        return temperature

    def cancel_after_on_closing(self):
        global timer_id
        if timer_id is not None:
            self.after_cancel(timer_id)
            timer_id = None

    @staticmethod
    def write_personal_json():
        global pressure_values
        global temperature_values
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
        json_writer(personal_json_name, "pressure_values", pressure_values, personal_folder_path)
        json_writer(personal_json_name, "temperature_values", temperature_values, personal_folder_path)
