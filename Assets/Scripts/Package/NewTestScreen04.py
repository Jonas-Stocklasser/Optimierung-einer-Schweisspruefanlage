#!/usr/bin/python3
# Date: 23.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Neuer Test Fenster 4; ID=1.3

import customtkinter as ctk
import tkinter as tk
# Shared variables----------------------------------------
from .SharedVar import GetStartupVariables, GetItemVariables, back_arrow_image
from .JsonFunctions import json_writer, json_reader


class NewTestScreen04(ctk.CTkFrame):  # class for the NewTestScreen04 window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(GetStartupVariables.window_geometry[0] - 10),
                         height=(GetStartupVariables.window_geometry[1] - 10),
                         fg_color="transparent")

        self.app = parent

        self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   y=5)

        # indicator bar------------------------------------------------------------
        self.indicator_bar = ctk.CTkLabel(master=self,
                                          # top bar that indicates the screen where you are
                                          fg_color=GetStartupVariables.color_SET_blue,
                                          width=GetStartupVariables.window_geometry[0] - 70,
                                          height=40,
                                          corner_radius=10,
                                          text=("Neuer Test - Schritt 4:" +
                                                " Daten des Prüfstückes überprüfen"),
                                          text_color=GetStartupVariables.text_color_SET,
                                          font=("bold", 20),
                                          anchor="w")
        self.indicator_bar.place(x=0,
                                 y=0)
        # options menu item------------------------------------------------------------
        self.item_option_menu_frame = ctk.CTkFrame(master=self,  # frame for the entries
                                                   width=340,
                                                   height=70,
                                                   corner_radius=20)
        self.item_option_menu_frame.place(x=30,
                                          y=75)

        self.item_option_menu_label = ctk.CTkLabel(master=self.item_option_menu_frame,
                                                   fg_color=GetStartupVariables.color_SET_blue,
                                                   width=200,
                                                   height=50,
                                                   corner_radius=10,
                                                   text="Voreinstellungen",
                                                   text_color=GetStartupVariables.text_color_SET,
                                                   font=("bold", 20))
        self.item_option_menu_label.place(x=10,
                                          y=10)

        self.options_menu_item = ctk.CTkOptionMenu(master=self.item_option_menu_frame,
                                                   width=100,
                                                   height=50,
                                                   font=("bold", 20),
                                                   dropdown_font=("bold", 20),
                                                   corner_radius=5,
                                                   variable=tk.StringVar(value=GetItemVariables.last_chosen_item),
                                                   values=GetItemVariables.item_list,
                                                   command=self.item_select)
        # the command automatically passes the current value as an argument to the specified method
        self.options_menu_item.place(x=230,
                                     y=10)
        # entry frame 1------------------------------------------------------------
        self.entry_frame1 = ctk.CTkFrame(master=self,  # frame for the entries
                                         width=340,
                                         height=360,
                                         corner_radius=20)
        self.entry_frame1.place(x=30,
                                y=175)

        # entry frame 2------------------------------------------------------------
        self.entry_frame2 = ctk.CTkFrame(master=self,  # frame for the entries
                                         width=340,
                                         height=240,
                                         corner_radius=20)
        self.entry_frame2.place(x=380,
                                y=295)

        # back button------------------------------------------------------------
        self.back_button = ctk.CTkButton(master=self,  # back button
                                         width=40,
                                         height=40,
                                         corner_radius=10,
                                         text="",
                                         anchor="ne",
                                         image=back_arrow_image,
                                         command=lambda: self.master.open_top_level_window_really_switch(
                                             "1.2"))
        # the command does call the switch_window method because there is unsaved content to loose
        self.back_button.place(x=GetStartupVariables.window_geometry[0] - 65,
                               y=0)

        # title entry------------------------------------------------------------
        self.title_entry_label = ctk.CTkLabel(master=self.entry_frame1,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              width=100,
                                              height=40,
                                              corner_radius=10,
                                              text="Titel",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", 20))
        self.title_entry_label.place(x=10,
                                     y=10)

        self.title_entry = ctk.CTkEntry(master=self.entry_frame1,
                                        width=250,
                                        height=50,
                                        font=("bold", 20),
                                        state="disabled"
                                        )
        self.title_entry.place(x=10,
                               y=60)

        self.title_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame1,
                                                                      width=250,
                                                                      height=50,
                                                                      corner_radius=10)
        self.title_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=60)

        self.title_entry_unchanged_overlay_label = ctk.CTkLabel(master=self.title_entry_unchanged_overlay_label_frame,
                                                                width=230,
                                                                height=50,
                                                                anchor="w",
                                                                text=GetItemVariables.infos_item[0],
                                                                font=("bold", 20))
        self.title_entry_unchanged_overlay_label.place(x=10,
                                                       y=0)

        # info1 entry------------------------------------------------------------
        self.info1_entry_label = ctk.CTkLabel(master=self.entry_frame1,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              width=100,
                                              height=40,
                                              corner_radius=10,
                                              text="Info1",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", 20))
        self.info1_entry_label.place(x=10,
                                     y=130)

        self.info1_entry = ctk.CTkEntry(master=self.entry_frame1,
                                        width=250,
                                        height=50,
                                        font=("bold", 20),
                                        state="disabled"
                                        )
        self.info1_entry.place(x=10,
                               y=180)

        self.info1_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame1,
                                                                      width=250,
                                                                      height=50,
                                                                      corner_radius=10)
        self.info1_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=180)

        self.info1_entry_unchanged_overlay_label = ctk.CTkLabel(master=self.info1_entry_unchanged_overlay_label_frame,
                                                                width=230,
                                                                height=50,
                                                                anchor="w",
                                                                text=GetItemVariables.infos_item[1],
                                                                font=("bold", 20))
        self.info1_entry_unchanged_overlay_label.place(x=10,
                                                       y=0)

        # info2 entry------------------------------------------------------------
        self.info2_entry_label = ctk.CTkLabel(master=self.entry_frame1,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              width=100,
                                              height=40,
                                              corner_radius=10,
                                              text="Info2",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", 20))
        self.info2_entry_label.place(x=10,
                                     y=250)

        self.info2_entry = ctk.CTkEntry(master=self.entry_frame1,
                                        width=250,
                                        height=50,
                                        font=("bold", 20),
                                        state="disabled"
                                        )
        self.info2_entry.place(x=10,
                               y=300)

        self.info2_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame1,
                                                                      width=250,
                                                                      height=50,
                                                                      corner_radius=10)
        self.info2_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=300)

        self.info2_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info2_entry_unchanged_overlay_label_frame,
            width=230,
            height=50,
            anchor="w",
            text=GetItemVariables.infos_item[2],
            font=("bold", 20))
        self.info2_entry_unchanged_overlay_label.place(x=10,
                                                       y=00)

        # info3 entry------------------------------------------------------------
        self.info3_entry_label = ctk.CTkLabel(master=self.entry_frame2,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              width=100,
                                              height=40,
                                              corner_radius=10,
                                              text="Info3",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", 20))
        self.info3_entry_label.place(x=10,
                                     y=10)

        self.info3_entry = ctk.CTkEntry(master=self.entry_frame2,
                                        width=250,
                                        height=50,
                                        font=("bold", 20),
                                        state="disabled"
                                        )
        self.info3_entry.place(x=10,
                               y=60)

        self.info3_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame2,
                                                                      width=250,
                                                                      height=50,
                                                                      corner_radius=10)
        self.info3_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=60)

        self.info3_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info3_entry_unchanged_overlay_label_frame,
            width=230,
            height=50,
            anchor="w",
            text=GetItemVariables.infos_item[3],
            font=("bold", 20))
        self.info3_entry_unchanged_overlay_label.place(x=10,
                                                       y=0)

        # info4 entry------------------------------------------------------------
        self.info4_entry_label = ctk.CTkLabel(master=self.entry_frame2,
                                              fg_color=GetStartupVariables.color_SET_blue,
                                              width=100,
                                              height=40,
                                              corner_radius=10,
                                              text="Info4",
                                              text_color=GetStartupVariables.text_color_SET,
                                              font=("bold", 20))
        self.info4_entry_label.place(x=10,
                                     y=130)

        self.info4_entry = ctk.CTkEntry(master=self.entry_frame2,
                                        width=250,
                                        height=50,
                                        font=("bold", 20),
                                        state="disabled"
                                        )
        self.info4_entry.place(x=10,
                               y=180)

        self.info4_entry_unchanged_overlay_label_frame = ctk.CTkFrame(master=self.entry_frame2,
                                                                      width=250,
                                                                      height=50,
                                                                      corner_radius=10)
        self.info4_entry_unchanged_overlay_label_frame.place(x=10,
                                                             y=180)

        self.info4_entry_unchanged_overlay_label = ctk.CTkLabel(
            master=self.info4_entry_unchanged_overlay_label_frame,
            width=230,
            height=50,
            anchor="w",
            text=GetItemVariables.infos_item[4],
            font=("bold", 20))
        self.info4_entry_unchanged_overlay_label.place(x=10,
                                                       y=0)

        # change, save and continue button------------------------------------------------------------

        self.button_frame = ctk.CTkFrame(master=self,  # frame for the button
                                         width=380,
                                         height=70,
                                         corner_radius=20)
        self.button_frame.place(x=30,
                                y=570)

        self.change_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                           width=120,
                                           height=50,
                                           corner_radius=10,
                                           text="Ändern",
                                           font=("bold", 20),
                                           state="normal",
                                           command=lambda: self.change_entry_data_item())
        self.change_button.place(x=10,
                                 y=10)

        self.save_button = ctk.CTkButton(master=self.button_frame,  # continue button
                                         width=120,
                                         height=50,
                                         corner_radius=10,
                                         text="Speichern",
                                         font=("bold", 20),
                                         state="disabled",
                                         command=lambda: self.save_entry_data_item())
        self.save_button.place(x=140,
                               y=10)

        self.continue_button = ctk.CTkButton(master=self.button_frame,
                                             # continue button
                                             width=100,
                                             height=50,
                                             corner_radius=10,
                                             text="Weiter",
                                             font=("bold", 20),
                                             state="normal",
                                             command=self.continue_button_function)
        self.continue_button.place(x=270,
                                   y=10)

    def continue_button_function(self):
        self.master.switch_window("1.4")
        self.write_personal_json()

    def change_entry_data_item(self):
        self.title_entry_unchanged_overlay_label.place_forget()
        self.title_entry_unchanged_overlay_label_frame.place_forget()
        self.info1_entry_unchanged_overlay_label.place_forget()
        self.info1_entry_unchanged_overlay_label_frame.place_forget()
        self.info2_entry_unchanged_overlay_label.place_forget()
        self.info2_entry_unchanged_overlay_label_frame.place_forget()
        self.info3_entry_unchanged_overlay_label.place_forget()
        self.info3_entry_unchanged_overlay_label_frame.place_forget()
        self.info4_entry_unchanged_overlay_label.place_forget()
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
            last_chosen_item = json_reader("personal_var", "last_chosen_item", "../JSON/")
            json_writer("item_var", ("infos_item_" + last_chosen_item), infos_item, "../JSON/")

            self.title_entry_unchanged_overlay_label_frame.place(x=10, y=60)
            self.title_entry_unchanged_overlay_label.place(x=10, y=0)
            self.info1_entry_unchanged_overlay_label_frame.place(x=10, y=180)
            self.info1_entry_unchanged_overlay_label.place(x=10, y=0)
            self.info2_entry_unchanged_overlay_label_frame.place(x=10, y=300)
            self.info2_entry_unchanged_overlay_label.place(x=10, y=0)
            self.info3_entry_unchanged_overlay_label_frame.place(x=10, y=60)
            self.info3_entry_unchanged_overlay_label.place(x=10, y=0)
            self.info4_entry_unchanged_overlay_label_frame.place(x=10, y=180)
            self.info4_entry_unchanged_overlay_label.place(x=10, y=0)
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
        json_writer("item_var", "last_chosen_item", which, "../JSON/")
        last_chosen_item = json_reader("item_var", "last_chosen_item", "../JSON/")
        infos = json_reader("item_var", f"infos_item_{last_chosen_item}", "../JSON/")
        self.update_labels(infos)

    @staticmethod
    def write_personal_json():
        last_chosen_item = json_reader("item_var", "last_chosen_item", "../JSON/")
        infos_item = json_reader("item_var", f"infos_item_{last_chosen_item}", "../JSON/")
        personal_folder_path = json_reader("personal_var", "personal_folder_path", "../JSON/")
        personal_json_name = json_reader("personal_var", "personal_json_name", "../JSON/")
        json_writer(personal_json_name, "infos_item", infos_item, personal_folder_path)
