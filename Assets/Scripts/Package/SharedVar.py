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


# Startup variables----------------------------------------
class GetStartupVariables:
    name_of_app = json_reader("startup_var", "name_of_app", "../Other/")
    window_geometry = json_reader("startup_var", "window_geometry", "../Other/")
    color_SET_blue = json_reader("startup_var", "color_SET_blue", "../Other/")
    color_SET_gray = json_reader("startup_var", "color_SET_gray", "../Other/")
    text_color_SET = json_reader("startup_var", "text_color_SET", "../Other/")
    start_window = json_reader("startup_var", "start_window", "../Other/")
    appearance_mode = json_reader("startup_var", "appearance_mode", "../Other/")
    window_size = json_reader("startup_var", "window_size", "../Other/")
    save_path = json_reader("startup_var", "save_path", "../Other/")


# Personal variables----------------------------------------
class GetPersonalVariables:
    last_chosen_examiner = json_reader("personal_var", "last_chosen_examiner", "../Other/")
    personal_infos_examiner = json_reader("personal_var", f"personal_infos_examiner_{last_chosen_examiner}",
                                          "../Other/")
    examiner_list = json_reader("personal_var", "examiner_list", "../Other/")


# Item variables----------------------------------------
class GetItemVariables:
    last_chosen_item = json_reader("item_var", "last_chosen_item", "../Other/")
    infos_item = json_reader("item_var", f"infos_item_{last_chosen_item}", "../Other/")
    item_list = json_reader("item_var", "item_list", "../Other/")


# Exam Parameter variables----------------------------------------
class GetExamParameterVariables:
    last_chosen_parameter_list = json_reader("exam_parameter_var", "last_chosen_parameter_list", "../Other/")
    parameter_list = json_reader("exam_parameter_var", f"parameter_list_{last_chosen_parameter_list}", "../Other/")
    parameter_list_indexes = json_reader("exam_parameter_var", "parameter_list_indexes", "../Other/")
