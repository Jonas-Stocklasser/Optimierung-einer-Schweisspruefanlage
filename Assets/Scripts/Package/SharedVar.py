#!/usr/bin/python3
# Date: 19.06.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# Shared Variables

import customtkinter as ctk
from PIL import Image  # library for image handling
from .JsonFunctions import json_reader

# Pictures----------------------------------------
start_image = ctk.CTkImage(Image.open("../Images/Placeholder.png"), size=(600, 600))
back_arrow_image = ctk.CTkImage(dark_image=Image.open("../Images/Back_Arrow.png"), size=(30, 30))
pruefstueck_image = ctk.CTkImage(dark_image=Image.open("../Images/Pruefstueck_Dark.png") ,light_image=Image.open("../Images/Pruefstueck_Light.png"), size=(576, 324))


# Startup variables----------------------------------------
class GetStartupVariables:
    name_of_app = json_reader("startup_var", "name_of_app", "../JSON/")
    window_geometry = json_reader("startup_var", "window_geometry", "../JSON/")
    color_SET_blue = json_reader("startup_var", "color_SET_blue", "../JSON/")
    color_SET_gray = json_reader("startup_var", "color_SET_gray", "../JSON/")
    text_color_SET = json_reader("startup_var", "text_color_SET", "../JSON/")
    start_window = json_reader("startup_var", "start_window", "../JSON/")
    appearance_mode = json_reader("startup_var", "appearance_mode", "../JSON/")
    window_size = json_reader("startup_var", "window_size", "../JSON/")
    save_path = json_reader("startup_var", "save_path", "../JSON/")


# Personal variables----------------------------------------
class GetPersonalVariables:
    last_chosen_examiner = json_reader("personal_var", "last_chosen_examiner", "../JSON/")
    personal_infos_examiner = json_reader("personal_var", f"personal_infos_examiner_{last_chosen_examiner}",
                                          "../JSON/")
    examiner_list = json_reader("personal_var", "examiner_list", "../JSON/")


# Item variables----------------------------------------
class GetItemVariables:
    last_chosen_item = json_reader("item_var", "last_chosen_item", "../JSON/")
    infos_item = json_reader("item_var", f"infos_item_{last_chosen_item}", "../JSON/")
    item_list = json_reader("item_var", "item_list", "../JSON/")


# Exam Parameter variables----------------------------------------
class GetExamParameterVariables:
    last_chosen_parameter_list = json_reader("exam_parameter_var", "last_chosen_parameter_list", "../JSON/")
    parameter_list = json_reader("exam_parameter_var", f"parameter_list_{last_chosen_parameter_list}", "../JSON/")
    parameter_list_indexes = json_reader("exam_parameter_var", "parameter_list_indexes", "../JSON/")
