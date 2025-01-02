#!/usr/bin/python3
# Date: 23.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 4; ID=1.3

import customtkinter as ctk
import tkinter as tk
import math
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetItemVariables, back_arrow_image, main_pi_location
from .JsonFunctions import json_writer, json_reader


class NewTestScreen04(ctk.CTkFrame):  # class for the NewTestScreen04 window
    def __init__(self, parent, window_geometry):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(window_geometry[0] - 10),
                         height=(window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        font_size = window_geometry[1] / 40

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
                                          text=("Neuer Test - Schritt 4:" +
                                                " Daten des Prüfstückes überprüfen"),
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", font_size),
                                          anchor="w")
        self.indicator_bar.grid(row=1, column=1, columnspan=77, rowspan=1, sticky="nesw")

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         corner_radius=font_size / 2,
                                         text="",
                                         anchor="center",
                                         image=back_arrow_image,
                                         command=lambda: self.master.confirm_go_back("1.2"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.grid(row=1, column=78, columnspan=2, rowspan=1, sticky="nesw")

        # options menu item------------------------------------------------------------
        self.item_option_menu_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                   corner_radius=font_size / 2)
        self.item_option_menu_frame.grid(row=4, column=2, columnspan=15, rowspan=2, sticky="nesw")

        # Grid configuration
        self.item_option_menu_frame.grid_columnconfigure(0, weight=3)
        self.item_option_menu_frame.grid_columnconfigure(1, weight=20)
        self.item_option_menu_frame.grid_columnconfigure(2, weight=3)
        self.item_option_menu_frame.grid_columnconfigure(3, weight=20)
        self.item_option_menu_frame.grid_columnconfigure(4, weight=3)
        self.item_option_menu_frame.grid_rowconfigure(0, weight=3)
        self.item_option_menu_frame.grid_rowconfigure(1, weight=10)
        self.item_option_menu_frame.grid_rowconfigure(2, weight=3)

        self.item_option_menu_label = ctk.CTkLabel(master=self.item_option_menu_frame,
                                                   fg_color=GetStartupVariables.color_SET_blue,
                                                   corner_radius=font_size / 2,
                                                   text="Voreinstellungen",
                                                   text_color=GetStartupVariables.text_color_SET,
                                                   font=("bold", font_size))
        self.item_option_menu_label.grid(row=1, column=1, columnspan=1, rowspan=1, sticky="nesw")

        self.options_menu_item = ctk.CTkOptionMenu(master=self.item_option_menu_frame,
                                                   font=("bold", font_size),
                                                   dropdown_font=("bold", font_size),
                                                   corner_radius=font_size / 4,
                                                   variable=tk.StringVar(
                                                       value=GetItemVariables.last_chosen_item),
                                                   values=GetItemVariables.item_list,
                                                   command=self.item_select)
        # the command automatically passes the current value as an argument to the specified method
        self.options_menu_item.grid(row=1, column=3, columnspan=1, rowspan=1, sticky="new")

        # entry frame 1------------------------------------------------------------
        self.entry_frame1 = ctk.CTkFrame(master=self,  # frame for the entries
                                         corner_radius=font_size)
        self.entry_frame1.grid(row=8, column=2, columnspan=10, rowspan=15, sticky="nesw")

        # Grid configuration
        self.entry_frame1.grid_columnconfigure(0, weight=10)
        self.entry_frame1.grid_columnconfigure(tuple(range(1, 80)), weight=10)
        self.entry_frame1.grid_columnconfigure(81, weight=10)
        self.entry_frame1.grid_rowconfigure(0, weight=4)
        self.entry_frame1.grid_rowconfigure(tuple(range(1, 49)), weight=10)
        self.entry_frame1.grid_rowconfigure(50, weight=4)

        # entry frame 2------------------------------------------------------------
        self.entry_frame2 = ctk.CTkFrame(master=self,  # frame for the entries
                                         corner_radius=font_size)
        self.entry_frame2.grid(row=8, column=13, columnspan=10, rowspan=15, sticky="nesw")

        # Grid configuration
        self.entry_frame2.grid_columnconfigure(0, weight=10)
        self.entry_frame2.grid_columnconfigure(tuple(range(1, 80)), weight=10)
        self.entry_frame2.grid_columnconfigure(81, weight=10)
        self.entry_frame2.grid_rowconfigure(0, weight=4)
        self.entry_frame2.grid_rowconfigure(tuple(range(1, 49)), weight=10)
        self.entry_frame2.grid_rowconfigure(50, weight=4)

        # title entry------------------------------------------------------------
        self.title_entry_label = ctk.CTkLabel(master=self.entry_frame1,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=font_size / 2,
                                              text="Titel",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size))
        self.title_entry_label.grid(row=5, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.title_entry = ctk.CTkEntry(master=self.entry_frame1,
                                        font=("bold", font_size),
                                        state="disabled"
                                        )
        self.title_entry.grid(row=10, column=20, columnspan=2, rowspan=1, sticky="nesw")

        self.title_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame1,
                                                                      corner_radius=font_size / 2)
        self.title_entry_unchanged_overlay_label_frame.grid(row=10, column=20, columnspan=2, rowspan=1,
                                                            sticky="nesw")

        self.title_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.title_entry_unchanged_overlay_label_frame,
            anchor="w",
            text=GetItemVariables.infos_item[0],
            font=("bold", font_size))
        self.title_entry_unchanged_overlay_label.place(relx=0.1,
                                                       rely=0.3)

        # info1 entry------------------------------------------------------------
        self.info1_entry_label = ctk.CTkLabel(master=self.entry_frame1,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=font_size / 2,
                                              text="Info1",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size))
        self.info1_entry_label.grid(row=22, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.info1_entry = ctk.CTkEntry(master=self.entry_frame1,
                                        font=("bold", font_size),
                                        state="disabled")
        self.info1_entry.grid(row=27, column=20, columnspan=2, rowspan=1, sticky="nesw")

        self.info1_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame1,
                                                                      corner_radius=font_size / 2)
        self.info1_entry_unchanged_overlay_label_frame.grid(row=27, column=20, columnspan=2, rowspan=1,
                                                            sticky="nesw")

        self.info1_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info1_entry_unchanged_overlay_label_frame,
            anchor="w",
            text=GetItemVariables.infos_item[1],
            font=("bold", font_size))
        self.info1_entry_unchanged_overlay_label.place(relx=0.1,
                                                       rely=0.3)

        # info2 entry------------------------------------------------------------
        self.info2_entry_label = ctk.CTkLabel(master=self.entry_frame1,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=font_size / 2,
                                              text="Info2",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size))
        self.info2_entry_label.grid(row=39, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.info2_entry = ctk.CTkEntry(master=self.entry_frame1,
                                        font=("bold", font_size),
                                        state="disabled"
                                        )
        self.info2_entry.grid(row=44, column=20, columnspan=2, rowspan=1, sticky="nesw")

        self.info2_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame1,
                                                                      corner_radius=font_size / 2)
        self.info2_entry_unchanged_overlay_label_frame.grid(row=44, column=20, columnspan=2, rowspan=1,
                                                            sticky="nesw")

        self.info2_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info2_entry_unchanged_overlay_label_frame,
            anchor="w",
            text=GetItemVariables.infos_item[2],
            font=("bold", font_size))
        self.info2_entry_unchanged_overlay_label.place(relx=0.1,
                                                       rely=0.3)

        # info3 entry------------------------------------------------------------
        self.info3_entry_label = ctk.CTkLabel(master=self.entry_frame2,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=font_size / 2,
                                              text="Info3",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size))
        self.info3_entry_label.grid(row=5, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.info3_entry = ctk.CTkEntry(master=self.entry_frame2,
                                        font=("bold", font_size),
                                        state="disabled"
                                        )
        self.info3_entry.grid(row=10, column=20, columnspan=2, rowspan=1, sticky="nesw")

        self.info3_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame2,
                                                                      corner_radius=font_size / 2)
        self.info3_entry_unchanged_overlay_label_frame.grid(row=10, column=20, columnspan=2, rowspan=1,
                                                            sticky="nesw")

        self.info3_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info3_entry_unchanged_overlay_label_frame,
            anchor="w",
            text=GetItemVariables.infos_item[3],
            font=("bold", font_size))
        self.info3_entry_unchanged_overlay_label.place(relx=0.1,
                                                       rely=0.3)

        # info4 entry------------------------------------------------------------
        self.info4_entry_label = ctk.CTkLabel(master=self.entry_frame2,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              corner_radius=font_size / 2,
                                              text="Info4",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", font_size))
        self.info4_entry_label.grid(row=22, column=20, columnspan=1, rowspan=1, sticky="nesw")

        self.info4_entry = ctk.CTkEntry(master=self.entry_frame2,
                                        font=("bold", font_size),
                                        state="disabled"
                                        )
        self.info4_entry.grid(row=27, column=20, columnspan=2, rowspan=1, sticky="nesw")

        self.info4_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame2,
                                                                      corner_radius=font_size / 2)
        self.info4_entry_unchanged_overlay_label_frame.grid(row=27, column=20, columnspan=2, rowspan=1,
                                                            sticky="nesw")

        self.info4_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info4_entry_unchanged_overlay_label_frame,
            anchor="w",
            text=GetItemVariables.infos_item[4],
            font=("bold", font_size))
        self.info4_entry_unchanged_overlay_label.place(relx=0.1,
                                                       rely=0.3)

        # change, save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         corner_radius=font_size)
        self.button_frame.grid(row=25, column=2, columnspan=18, rowspan=2, sticky="nesw")

        # Grid configuration
        self.button_frame.grid_columnconfigure(0, weight=3)
        self.button_frame.grid_columnconfigure(1, weight=20)
        self.button_frame.grid_columnconfigure(2, weight=3)
        self.button_frame.grid_columnconfigure(3, weight=20)
        self.button_frame.grid_columnconfigure(4, weight=3)
        self.button_frame.grid_columnconfigure(5, weight=20)
        self.button_frame.grid_columnconfigure(6, weight=3)
        self.button_frame.grid_rowconfigure(0, weight=3)
        self.button_frame.grid_rowconfigure(1, weight=10)
        self.button_frame.grid_rowconfigure(2, weight=3)

        self.change_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                           corner_radius=font_size / 2,
                                           text="Ändern",
                                           font=("bold", font_size),
                                           state="normal",
                                           command=lambda: self.change_entry_data_item())
        self.change_button.grid(row=1, column=1, columnspan=1, rowspan=1, sticky="nesw")

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         corner_radius=font_size / 2,
                                         text="Speichern",
                                         font=("bold", font_size),
                                         state="disabled",
                                         command=lambda: self.save_entry_data_item())
        self.save_button.grid(row=1, column=3, columnspan=1, rowspan=1, sticky="nesw")

        self.continue_button = ctk.CTkButton(master=self.button_frame,
                                             # continue button
                                             corner_radius=font_size / 2,
                                             text="Weiter",
                                             font=("bold", font_size),
                                             state="normal",
                                             command=self.continue_button_function)
        self.continue_button.grid(row=1, column=5, columnspan=1, rowspan=1, sticky="nesw")

    def continue_button_function(self):
        self.master.switch_window("1.4")
        self.write_personal_json()

    def change_entry_data_item(self):
        self.title_entry_unchanged_overlay_label.grid_forget()
        self.title_entry_unchanged_overlay_label_frame.place_forget()
        self.info1_entry_unchanged_overlay_label.grid_forget()
        self.info1_entry_unchanged_overlay_label_frame.place_forget()
        self.info2_entry_unchanged_overlay_label.grid_forget()
        self.info2_entry_unchanged_overlay_label_frame.place_forget()
        self.info3_entry_unchanged_overlay_label.grid_forget()
        self.info3_entry_unchanged_overlay_label_frame.place_forget()
        self.info4_entry_unchanged_overlay_label.grid_forget()
        self.info4_entry_unchanged_overlay_label_frame.place_forget()

        self.title_entry.configure(state="normal", placeholder_text="Titel")
        self.info1_entry.configure(state="normal", placeholder_text="Info1")
        self.info2_entry.configure(state="normal", placeholder_text="Info2")
        self.info3_entry.configure(state="normal", placeholder_text="Info3")
        self.info4_entry.configure(state="normal", placeholder_text="Info4")

        self.change_button.configure(state="disabled")
        self.save_button.configure(state="normal")
        self.continue_button.configure(state="disabled")

    def save_entry_data_item(self):
        infos_item = [self.title_entry.get(),
                      self.info1_entry.get(),
                      self.info2_entry.get(),
                      self.info3_entry.get(),
                      self.info4_entry.get()]

        if (len(infos_item[0].strip()) +
                len(infos_item[1].strip()) +
                len(infos_item[2].strip()) +
                len(infos_item[3].strip()) +
                len(infos_item[4].strip()) >= 10):
            self.continue_button.configure(state="normal")
            last_chosen_item = json_reader("personal_var", "last_chosen_item", main_pi_location + "../JSON/")
            json_writer("item_var", ("infos_item_" + last_chosen_item), infos_item, main_pi_location + "../JSON/")

            self.title_entry_unchanged_overlay_label_frame.grid(row=10, column=20, columnspan=2, rowspan=1,
                                                                sticky="nesw")
            self.title_entry_unchanged_overlay_label.place(relx=0.1,
                                                           rely=0.3)
            self.info1_entry_unchanged_overlay_label_frame.grid(row=27, column=20, columnspan=2, rowspan=1,
                                                                sticky="nesw")
            self.info1_entry_unchanged_overlay_label.place(relx=0.1,
                                                           rely=0.3)
            self.info2_entry_unchanged_overlay_label_frame.grid(row=44, column=20, columnspan=2, rowspan=1,
                                                                sticky="nesw")
            self.info2_entry_unchanged_overlay_label.place(relx=0.1,
                                                           rely=0.3)
            self.info3_entry_unchanged_overlay_label_frame.grid(row=10, column=20, columnspan=2, rowspan=1,
                                                                sticky="nesw")
            self.info3_entry_unchanged_overlay_label.place(relx=0.1,
                                                           rely=0.3)
            self.info4_entry_unchanged_overlay_label_frame.grid(row=27, column=20, columnspan=2, rowspan=1,
                                                                sticky="nesw")
            self.info4_entry_unchanged_overlay_label.place(relx=0.1,
                                                           rely=0.3)
            self.update_labels(infos_item)

            self.title_entry.configure(state="disabled")
            self.info1_entry.configure(state="disabled")
            self.info2_entry.configure(state="disabled")
            self.info3_entry.configure(state="disabled")
            self.info4_entry.configure(state="disabled")

            self.change_button.configure(state="normal")
            self.save_button.configure(state="disabled")
            self.continue_button.configure(state="normal")
        else:
            self.continue_button.configure(state="disabled")
            print("Date-Format wrong or the sum of first name plus surname not at least 4 digits")

    def update_labels(self, infos):
        self.title_entry_unchanged_overlay_label.configure(text=infos[0])
        self.info1_entry_unchanged_overlay_label.configure(text=infos[1])
        self.info2_entry_unchanged_overlay_label.configure(text=infos[2])
        self.info3_entry_unchanged_overlay_label.configure(text=infos[3])
        self.info4_entry_unchanged_overlay_label.configure(text=infos[4])

    def item_select(self, which):
        json_writer("item_var", "last_chosen_item", which, main_pi_location + "../JSON/")
        last_chosen_item = json_reader("item_var", "last_chosen_item", main_pi_location + "../JSON/")
        infos = json_reader("item_var", f"infos_item_{last_chosen_item}", main_pi_location + "../JSON/")
        self.update_labels(infos)

    @staticmethod
    def write_personal_json():
        last_chosen_item = json_reader("item_var", "last_chosen_item", main_pi_location + "../JSON/")
        infos_item = json_reader("item_var", f"infos_item_{last_chosen_item}", main_pi_location + "../JSON/")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", main_pi_location + "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", main_pi_location + "../JSON/")
        json_writer(personal_json_name, "infos_item", infos_item, personal_folder_path)

    def update_size(self, font_size):
        self.indicator_bar.configure(font=("bold", font_size), height=font_size, corner_radius=font_size / 2)
        self.back_button.configure(width=font_size,
                                   height=font_size, corner_radius=font_size / 2)
        back_arrow_image.configure(size=(font_size, font_size))
        self.title_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5,
                                         corner_radius=font_size / 2)
        self.title_entry.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 10,
                                   corner_radius=font_size / 2)
        self.title_entry_unchanged_overlay_label.configure(font=("bold", font_size), height=font_size * 1,
                                                           width=font_size * 9, corner_radius=font_size / 2)
        self.title_entry_unchanged_overlay_label_frame.configure(height=font_size * 2,
                                                                 width=font_size * 10, corner_radius=font_size / 2)
        self.info1_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5,
                                         corner_radius=font_size / 2)
        self.info1_entry.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 10,
                                   corner_radius=font_size / 2)
        self.info1_entry_unchanged_overlay_label.configure(font=("bold", font_size), height=font_size * 1,
                                                           width=font_size * 9, corner_radius=font_size / 2)
        self.info1_entry_unchanged_overlay_label_frame.configure(height=font_size * 2,
                                                                 width=font_size * 10, corner_radius=font_size / 2)
        self.info2_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5,
                                         corner_radius=font_size / 2)
        self.info2_entry.configure(font=("bold", math.ceil(font_size) - 4), corner_radius=font_size / 2)
        self.info2_entry_unchanged_overlay_label.configure(font=("bold", font_size), height=font_size * 1,
                                                           width=font_size * 9, corner_radius=font_size / 2)
        self.info2_entry_unchanged_overlay_label_frame.configure(height=font_size * 2,
                                                                 width=font_size * 10, corner_radius=font_size / 2)

        self.info3_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5,
                                         corner_radius=font_size / 2)
        self.info3_entry.configure(font=("bold", math.ceil(font_size) - 4), corner_radius=font_size / 2)
        self.info3_entry_unchanged_overlay_label.configure(font=("bold", font_size), height=font_size * 1,
                                                           width=font_size * 9, corner_radius=font_size / 2)
        self.info3_entry_unchanged_overlay_label_frame.configure(height=font_size * 2,
                                                                 width=font_size * 10, corner_radius=font_size / 2)

        self.info4_entry_label.configure(font=("bold", font_size), height=font_size * 2, width=font_size * 5,
                                         corner_radius=font_size / 2)
        self.info4_entry.configure(font=("bold", math.ceil(font_size) - 4), corner_radius=font_size / 2)
        self.info4_entry_unchanged_overlay_label.configure(font=("bold", font_size), height=font_size * 1,
                                                           width=font_size * 9, corner_radius=font_size / 2)
        self.info4_entry_unchanged_overlay_label_frame.configure(height=font_size * 2,
                                                                 width=font_size * 10, corner_radius=font_size / 2)
        self.button_frame.configure(height=font_size * 2, corner_radius=font_size)
        self.change_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4,
                                     corner_radius=font_size / 2)
        self.save_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4,
                                   corner_radius=font_size / 2)
        self.continue_button.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4,
                                       corner_radius=font_size / 2)

        self.item_option_menu_frame.configure(height=font_size * 2, corner_radius=font_size / 2)
        self.item_option_menu_label.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4,
                                              corner_radius=font_size / 2)
        self.options_menu_item.configure(font=("bold", font_size), height=font_size * 1.5, width=font_size * 4,
                                         corner_radius=font_size / 4)

        self.entry_frame1.configure(corner_radius=font_size)
        self.entry_frame2.configure(corner_radius=font_size)
