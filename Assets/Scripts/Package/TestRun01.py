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
from time import sleep
import board
import busio
from adafruit_ina219 import INA219

window_geometry = GetStartupVariables.window_geometry

timer_id = None

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, False)
output = 0

i2c = busio.I2C(board.SCL, board.SDA)
ina = INA219(i2c)
ina.current_lsb = 0.1
ina.shunt_resistance = 0.1

pressure_values = []
temperature_values = []
test_timesteps = []


class TestRun01(ctk.CTkFrame):  # class for the TestRun01 window
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
                                          text="Testdurchlauf",
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", 20),
                                          anchor="w")
        self.indicator_bar.place(x=0,
                                 y=0)

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         width=40,
                                         height=window_geometry[1] / 20,
                                         corner_radius=10,
                                         text="",
                                         anchor="ne",
                                         image=back_arrow_image,
                                         command=lambda: self.master.confirm_go_back("2.0"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=GetStartupVariables.window_geometry[0] - 65,
                               y=0)

        # start button------------------------------------------------------------
        self.start_button = ctk.CTkButton(master=self,  # start button
                                          width=100,
                                          height=50,
                                          corner_radius=10,
                                          text="Start",
                                          font=("bold", 20),
                                          state="normal",
                                          command=lambda: self.start_button_function())
        self.start_button.place(x=5,
                                y=50)

        # stop button------------------------------------------------------------
        self.stop_button = ctk.CTkButton(master=self,  # stop button
                                         width=100,
                                         height=50,
                                         corner_radius=10,
                                         text="Stop",
                                         font=("bold", 20),
                                         state="disabled",
                                         command=lambda: self.stop_button_function())
        self.stop_button.place(x=150,
                               y=50)

        # Toggle relais button------------------------------------------------------------
        self.toggle_relais_button = ctk.CTkButton(master=self,
                                                  width=100,
                                                  height=50,
                                                  corner_radius=10,
                                                  text="Toggle Relais",
                                                  font=("bold", 20),
                                                  state="normal",
                                                  command=lambda: self.toggle_relais_button_function())
        self.toggle_relais_button.place(x=400,
                                        y=50)

        # mathplot
        self.figure, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_title("Temperaturverlauf (letzte 60 Sekunden)")
        self.ax.set_xlabel("Testzeit [s]")
        self.ax.set_ylabel("Temperatur [°C]")

        # Embedding the matplotlib plot into tkinter using FigureCanvasTkAgg
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().place(x=350, y=150)  # Position the plot in the window

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
            print(f"last entry = {last_entry}")
            last_entry += 1
            test_timesteps.append(last_entry)
            print(test_timesteps)

        temperature = self.get_temperature_w1()
        pressure = ina.current()
        print(f"pressure-amp: {pressure}mA\nbus-voltage: {ina.bus_voltage()}V\nshunt-voltage: {ina.shunt_voltage()}mV")

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

    def stop_button_function(self):
        global timer_id
        self.after_cancel(timer_id)
        timer_id = None
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")

    def update_plot(self):
        # Limit to last 60 values
        display_timesteps = test_timesteps[-60:]
        display_temperatures = temperature_values[-60:]

        # Clear the previous plot
        self.ax.clear()
        self.ax.set_title("Temperaturverlauf (letzte 60 Sekunden)")
        self.ax.set_xlabel("Testzeit [s]")
        self.ax.set_ylabel("Temperatur [°C]")

        # Plot the new data
        self.ax.plot(display_timesteps, display_temperatures, color='blue')

        # Redraw the canvas to update the plot
        self.canvas.draw()

    def get_temperature_w1(self):
        f = open(w1temp_location, "r")
        lines = f.readlines()
        f.close()
        temp_pos = lines[1].find("t=")
        if temp_pos != 1:
            temperature = float(int(lines[1][temp_pos + 2:]) / 1000)
            print(f"temperatur = {temperature}")
        return temperature

    def cancel_after_on_closing(self):
        global timer_id
        if timer_id is not None:
            self.after_cancel(timer_id)
            timer_id = None

    def toggle_relais_button_function(self):
        global output
        if output == 0:
            GPIO.output(14, True)
            output = 1
        elif output == 1:
            GPIO.output(14, False)
            output = 0

    @staticmethod
    def write_personal_json():
        global pressure_values
        global temperature_values
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
        json_writer(personal_json_name, "pressure_values", pressure_values, personal_folder_path)
        json_writer(personal_json_name, "temperature_values", temperature_values, personal_folder_path)
