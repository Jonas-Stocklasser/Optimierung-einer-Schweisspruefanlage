#!/usr/bin/python3
# Date: 30.09.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Test Run 1; ID=4.0

import customtkinter as ctk
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .JsonFunctions import json_reader, json_writer
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, back_arrow_image, main_pi_location, w1temp_location
from datetime import datetime, timedelta
from fpdf import FPDF
from fpdf.enums import XPos, YPos

from ina219 import INA219

timer_id = None
firstControlStartup = 1
regelungSchalter = 0
duration = 0
pressureControlMiddle = 0
pressureControlDown = 0
pressureControlUp = 0
height = 2  # height of space between pressureControlUp and pressureControlDown in bar
maxAllowedPressure = 0

# initialisation of duration control
controlledTimeStart = datetime.now()
controlledTimeTotal = timedelta(minutes=99999)

# Zeitpunktinkrement
Zeitinkrement = 1  # in s between the measurement points

pressure_current = 4

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

pressure_values = [0, 0]
temperature_values = []
test_timesteps = [0, 0]


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

        # frames------------------------------------------------------------
        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=20,
                                         height=font_size * 1.5 + 20,
                                         width=window_geometry[0] / 7.4)
        self.button_frame.place(x=0,
                                y=font_size * 2)

        self.temp_frame = ctk.CTkFrame(master=self,  # frame for the button
                                       corner_radius=20,
                                       height=font_size * 1.5 + 20,
                                       width=font_size * 7 + 20)
        self.temp_frame.place(x=window_geometry[0] / 7,
                              y=font_size * 2)

        self.pdf_frame = ctk.CTkFrame(master=self,  # frame for the button
                                      corner_radius=20,
                                      height=font_size * 1.5 + 20,
                                      width=font_size * 10 + 20)
        self.pdf_frame.place(x=0,
                             y=window_geometry[0] / 1.65)

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

        # pdf button------------------------------------------------------------
        self.pdf_button = ctk.CTkButton(master=self.pdf_frame,  # stop button
                                        corner_radius=10,
                                        text="Prüfbericht erstellen",
                                        font=("bold", font_size),
                                        state="disabled",
                                        command=lambda: self.pdf_button_function(),
                                        width=font_size * 10,
                                        height=font_size * 1.5)
        self.pdf_button.place(x=10,
                              y=10)

        # temperature display label
        self.temp_label = ctk.CTkLabel(master=self.temp_frame,
                                       fg_color=GetStartupVariables.color_SET_blue,
                                       corner_radius=10,
                                       text="Ø 13.45°C",
                                       text_color=GetStartupVariables.text_color_SET,
                                       font=("bold", font_size),
                                       width=font_size * 7,
                                       height=font_size * 1.5)
        self.temp_label.place(x=10,
                              y=10)

        # mathplot------------------------------------------------------------
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
        global regelungSchalter
        global maxAllowedPressure
        global Zeitinkrement
        global controlledTimeTotal
        global controlledTimeStart
        global firstControlStartup

        # for testing
        #global pressure_current
        # ------

        # Abbruchbedingung Druckabfall pruefen
        pDiff = pressure_values[len(pressure_values) - 1] - pressure_values[len(pressure_values) - 2]
        if pDiff >= -10:
            timer_id = self.after(int(Zeitinkrement * 1000), self.to_do)
        elif pDiff < -10:
            self.stop_test(pDiff)
            self.master.error_message("!Achtung!",
                                      "Druckabfall über 10bar zwischen Messpunkten!\nPrüfstückbruch erkannt\nDurchführung beendet!")

        if test_timesteps == []:
            test_timesteps = [Zeitinkrement]
        else:
            last_entry = test_timesteps[len(test_timesteps) - 1]
            last_entry += Zeitinkrement
            test_timesteps.append(last_entry)

        temperature = self.get_temperature_w1()
        pressure_current = ina.current()

        # Pressure Calculation
        MBEWe = 60  # Messbereichsendwert Druck in Bar
        MBAWe = 0  # Messbereichsanfangswert Druck in Bar
        MBe = MBEWe - MBAWe  # Messbereich Druckin Bar
        MBEWa = 20  # Messbereichsendwert Strom in mA
        MBAWa = 4  # Messbereichsanfangswert Strom in mA
        MBa = MBEWa - MBAWa  # Messbereich Strom in mA

        pressure = (MBe / MBa) * (pressure_current - MBAWa) + MBAWe

        print(f"Pressure = {pressure}")
        pressure_values.append(pressure)
        temperature_values.append(temperature)

        mean_temp = round(np.mean(temperature_values), 2)
        self.temp_label.configure(text=f"Ø {mean_temp}°C")

        # Regelungszeit
        controlledTimeNow = datetime.now()
        print(controlledTimeNow)
        print(controlledTimeStart)
        print(controlledTimeTotal)
        print(f"diff= {controlledTimeNow - controlledTimeStart}")
        if controlledTimeNow - controlledTimeStart >= controlledTimeTotal and firstControlStartup == 0:
            regelungSchalter = 2

        # Regelung
        if regelungSchalter == 1:
            self.regelung("start")

        if regelungSchalter == 0:
            self.regelung("stop")

        if regelungSchalter == 2:
            self.regelung("pump")
        print(regelungSchalter)

        # Abbruchbedingung zu hoher Druck
        if pressure >= maxAllowedPressure:
            self.stop_button_function()
            print(maxAllowedPressure)
            self.master.error_message("!Achtung!",
                                      f"Prüfdruck zu hoch! {pressure}bar\nSensor könnte bei Fortfahren beschädigt werden!\nDurchführung beendet!")

        if pressure_current < 4:
            self.stop_button_function()
            self.master.error_message("!Achtung!",
                                      "Drucksensorstrom unter 4mA! Sensor auf Fehler prüfen!\nDurchführung beendet!")

        self.update_plot()


    def start_button_function(self):
        global timer_id
        global pressure_current
        global regelungSchalter
        global pressureControlMiddle
        global pressureControlDown
        global pressureControlUp
        global duration
        global height
        global maxAllowedPressure
        global firstControlStartup
        global controlledTimeTotal

        # Error when Sensor current is below 4mA
        if pressure_current < 4:
            self.master.error_message("!Achtung!",
                                      "Drucksensorstrom unter 4mA! Sensor auf Fehler prüfen!\nDurchführung beendet!")

        elif pressure_current >= 4:
            # getting the controller data out of the chosen item data ----------
            personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
            personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")

            infos_item = json_reader(personal_json_name, "infos_item", personal_folder_path)
            sigma = float(infos_item[1])
            en = float(infos_item[2])
            dn = float(infos_item[3])
            duration = float(infos_item[4])
            # calculated controlled pressure (from oenorm m 1861-6:2009)
            pressureControlMiddle = (20 * en * sigma) / (dn - en)
            pressureControlUp = pressureControlMiddle + height / 2
            pressureControlDown = pressureControlMiddle - height / 2

            exam_parameter = json_reader(personal_json_name, "exam_parameter", personal_folder_path)
            firstControlStartup = int(json_reader("startup_var", "firstControlStartup", main_pi_location + "../JSON/"))
            print(exam_parameter)

            maxAllowedPressure = float(exam_parameter[0])

            controlledTimeTotalUserdefined = int(exam_parameter[1])
            controlledTimeTotal = timedelta(minutes=controlledTimeTotalUserdefined)

            timer_id = self.after(int(Zeitinkrement * 1000), self.to_do)
            regelungSchalter = 1
            self.pdf_button.configure(state="disabled")
            self.start_button.configure(state="disabled")
            self.stop_button.configure(state="normal")
            print("Started")

    def stop_button_function(self):
        global timer_id
        global regelungSchalter

        self.after_cancel(timer_id)
        regelungSchalter = 0
        self.regelung("stop")
        timer_id = None
        self.write_personal_json()
        self.pdf_button.configure(state="normal")
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")

    def pdf_button_function(self):
        global pressure_values
        global test_timesteps

        print("PDF")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")

        # examinee data fetching ---------------------------------------------------------------------------------------
        personal_infos_examinee = json_reader(personal_json_name, "personal_infos_examinee", personal_folder_path)
        first_name_examinee = personal_infos_examinee[0]
        last_name_examinee = personal_infos_examinee[1]
        birth_date_examinee = personal_infos_examinee[2]

        # examiner data fetching ---------------------------------------------------------------------------------------
        visual_grade = json_reader(personal_json_name, "visual_grade", personal_folder_path)

        # create diagram png -------------------------------------------------------------------------------------------
        self.ax.clear()
        self.ax.set_title("Überdruckverlauf (letzte 60 Sekunden)")
        self.ax.set_xlabel("Testzeit [s]")
        self.ax.set_ylabel("Druck [Bar]")

        # Plot the new data
        self.ax.plot(test_timesteps, pressure_values, color='blue')

        plt.savefig(f"{personal_folder_path}/Druckverlauf.png", dpi=300)

        class PDF(FPDF):
            def header(self):
                self.set_y(5)
                self.set_font("helvetica", "", 10)
                w = self.w
                l_margin = self.l_margin
                r_margin = self.r_margin
                width = (w - l_margin - r_margin)
                self.cell(width / 3, 10, "Prüfbericht", border=False, align="L")
                self.cell(width / 3, 10, "KST-Schweißprüfung", border=False, align="C")
                self.cell(width / 3, 10, f"{last_name_examinee} {first_name_examinee}", border=False, align="R",
                          new_x=XPos.LMARGIN,
                          new_y=YPos.NEXT)
                self.ln(5)

            def footer(self):
                self.set_y(-15)
                w = self.w
                l_margin = self.l_margin
                r_margin = self.r_margin
                width = (w - l_margin - r_margin)
                exam_date = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"
                self.set_font("helvetica", "", 10)
                self.cell(width / 2, 10, f"Seite {self.page_no()} von {self.pages_count}", border=False, align="L")
                self.cell(width / 2, 10, f"{exam_date}", border=False, align="R")

        pdf = PDF("P", "mm", "A4")
        pdf.set_title(f"Prüfbericht - {last_name_examinee} {first_name_examinee}")
        pdf.set_auto_page_break(auto=True, margin=25)
        pdf.set_margin(margin=25)
        pdf.add_page()
        pdf.set_font("helvetica", "B", 16)

        # Title --------------------------------------------------------------------------------------------------------
        pdf.cell(0, 10, "Prüfbericht nach ÖNORM M 7861-6:2009", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

        # examinee data ------------------------------------------------------------------------------------------------
        pdf.set_font("helvetica", "U", 12)
        pdf.cell(0, 10, "Prüflingsdaten:", align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("helvetica", "", 12)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Vorname:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, first_name_examinee, border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Nachname:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, last_name_examinee, border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Geburtsdatum:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, birth_date_examinee, border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

        # piece data ---------------------------------------------------------------------------------------------------
        pdf.set_font("helvetica", "U", 12)
        pdf.cell(0, 10, "Erzeugnisdaten:", align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("helvetica", "", 12)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Art:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Art>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Lieferform:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Lieferform>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Bezeichnung:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Bezeichnung>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Herstellungsdatum:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Herstellungsdatum>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Herstellungsverfahren:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Herstellungsverfahren>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Grundwerkstoff:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Grundwerkstoff>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Zusatzwerkstoffe:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Zusatzwerkstoffe>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Abmessungen:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Abmessungen>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

        # exam data ----------------------------------------------------------------------------------------------------
        pdf.set_font("helvetica", "U", 12)
        pdf.cell(0, 10, "Prüfdaten:", align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("helvetica", "", 12)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Durchschnittstemperatur:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Durchschnittstemperatur>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Dauerprüfdruck:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Dauerprüfdruck>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Berstdruck:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Berstdruck>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(40, 10, "Prüfdauer:", border=False, align="L")
        pdf.cell(10, 10, "", border=False, align="L")
        pdf.cell(60, 10, "<Prüfdauer>", border=False, align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.add_page()

        # visual grade -------------------------------------------------------------------------------------------------
        pdf.set_font("helvetica", "U", 12)
        pdf.cell(0, 10, "Visuelle Beurteilung des Prüfstücks und der Schweißverbindungen:", align="L",
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("helvetica", "", 12)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.multi_cell(0, 10, visual_grade, border=False,
                       align="L")
        pdf.ln(5)

        # pressure diagram ---------------------------------------------------------------------------------------------
        image_height = 100
        text_height = 10
        remaining_space = pdf.h - pdf.b_margin - pdf.get_y()

        if remaining_space < (image_height + text_height):
            pdf.add_page()
        pdf.set_font("helvetica", "U", 12)
        pdf.cell(0, 10, "Abbildung des Druckverlaufes während der Prüfung:", align="L", new_x=XPos.LMARGIN,
                 new_y=YPos.NEXT)
        pdf.set_font("helvetica", "", 12)
        pdf.image(f"{personal_folder_path}/Druckverlauf.png", x=15, y=pdf.get_y() + 5, w=180)
        pdf.set_y(pdf.get_y() + image_height + 5)

        # grade of exam ------------------------------------------------------------------------------------------------
        pdf.set_font("helvetica", "U", 12)
        pdf.cell(0, 10, "Beurteilung der Prüfung:", align="L",
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("helvetica", "", 12)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.multi_cell(0, 10, "<Beutreilung der Prüfung>")
        pdf.ln(5)

        # result of exam -----------------------------------------------------------------------------------------------
        pdf.set_font("helvetica", "U", 12)
        pdf.cell(0, 10, "Ergebnis der Prüfung:", align="L",
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("helvetica", "", 12)

        pdf.cell(10, 10, "", border=False, align="L")
        pdf.multi_cell(0, 10, "<Ergebnis der Prüfung>")

        # save ---------------------------------------------------------------------------------------------------------
        pdf.output(f"{personal_folder_path}/Pruefbericht_{last_name_examinee}_{first_name_examinee}.pdf")

    def update_plot(self):
        # Limit to last 60 seconds
        display_timesteps = test_timesteps[-int(60 / Zeitinkrement):]
        display_pressures = pressure_values[-int(60 / Zeitinkrement):]

        # Clear the previous plot
        self.ax.clear()
        self.ax.set_title("Überdruckverlauf (letzte 60 Sekunden)")
        self.ax.set_xlabel("Testzeit [s]")
        self.ax.set_ylabel("Druck [Bar]")

        # Plot the new data
        self.ax.plot(display_timesteps, display_pressures, color='blue')

        # Redraw the canvas to update the plot
        self.canvas.draw()
        self.update_idletasks()
        self.update()

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

    def stop_test(self, pDiff):
        self.stop_button_function()
        print(f"\nVersuch wegen Druckabfalls beendet!\nDruckabfall zwischen letzten Messpunkten: {pDiff}")

    def regelung(self, what):
        global firstControlStartup
        global pressure_values
        global pressureControlUp
        global pressureControlMiddle
        global pressureControlDown
        global maxAllowedPressure
        global controlledTimeStart

        pressureNow = pressure_values[len(pressure_values) - 1]
        if what == "start":
            print("regelung start")
            if firstControlStartup == 1 and pressureNow <= pressureControlMiddle:
                GPIO.output(14, True)
                print("first ascend start")

            elif firstControlStartup == 1 and pressureNow >= pressureControlMiddle:
                GPIO.output(14, False)
                firstControlStartup = 0
                controlledTimeStart = datetime.now()
                print("first ascend end")

            elif firstControlStartup == 0 and pressureNow <= pressureControlDown:
                GPIO.output(14, True)
                print("lower barrier reached, pump on")

            elif firstControlStartup == 0 and pressureNow >= pressureControlUp:
                GPIO.output(14, False)
                print("upper barrier reached, pump off")

            elif pressureNow > maxAllowedPressure:
                self.stop_button_function()

        elif what == "pump":
            GPIO.output(14, True)
            print("Aufpumpen bis bersten")

        elif what == "stop":
            GPIO.output(14, False)
            print("regelung stop")

    @staticmethod
    def write_personal_json():
        global pressure_values
        global temperature_values
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
        json_writer(personal_json_name, "pressure_values", pressure_values, personal_folder_path)
        json_writer(personal_json_name, "temperature_values", temperature_values, personal_folder_path)

    # code testing -----------------------------------------------------------------------------------------------------
    # code test method
    @staticmethod
    def test_stop_functionality_too_low(current_window):  # press 1
        global pressure_current
        if current_window == "4.0" and GetStartupVariables.code_testing == "1":
            print(f"test: {pressure_current}")
            pressure_current = 4

    # code test method
    @staticmethod
    def test_stop_functionality_normal1(current_window):  # press 2
        global pressure_current
        if current_window == "4.0" and GetStartupVariables.code_testing == "1":
            print(f"test: {pressure_current}")
            pressure_current = 3.9

    # code test method
    @staticmethod
    def test_stop_functionality_normal2(current_window):  # press 3
        global pressure_current
        if current_window == "4.0" and GetStartupVariables.code_testing == "1":
            print(f"test: {pressure_current}")
            pressure_current = 15

    # code test method
    @staticmethod
    def test_stop_functionality_too_high(current_window):  # press 4
        global pressure_current
        if current_window == "4.0" and GetStartupVariables.code_testing == "1":
            print(f"test: {pressure_current}")
            pressure_current = 20

    # code test method
    @staticmethod
    def test_stop_functionality_pressure_up(current_window):  # press arrow key up
        global pressure_current
        if current_window == "4.0" and GetStartupVariables.code_testing == "1":
            print(f"test: {pressure_current}")
            pressure_current += 0.5

    # code test method
    @staticmethod
    def test_stop_functionality_pressure_down(current_window):  # press arrow key down
        global pressure_current
        if current_window == "4.0" and GetStartupVariables.code_testing == "1":
            print(f"test: {pressure_current}")
            pressure_current -= 0.5
