#!/usr/bin/python3
# Date: 09.02.24
# Author: Stocklasser
# DA Ideas
#

import customtkinter as ctk
import pandas as pd
from PIL import Image   # library for image handling

# Pictures----------------------------------------
start_image = ctk.CTkImage(Image.open("../Images/Placeholder.png"), size=(600, 600))
back_arrow_image = ctk.CTkImage(dark_image=Image.open("../Images/Back_Arrow.png"), size=(30, 30))


# Startup variables----------------------------------------
class GetStartupVariables():
    with open("../Other/startup_var.csv", mode="r", encoding="latin1") as file:
        data = pd.read_csv(file)
    name_of_app = data.iloc[1, 1]  # [row index, column index]]
    window_geometry = eval(data.iloc[0, 1])     # eval converts it to a list
    color_SET = data.iloc[2, 1]
    text_color_SET = data.iloc[3, 1]
    start_window = data.iloc[4, 1]
    appearance_mode = eval(data.iloc[5, 1])


name_of_app = GetStartupVariables.name_of_app
window_geometry = GetStartupVariables.window_geometry
color_SET = GetStartupVariables.color_SET
text_color_SET = GetStartupVariables.text_color_SET
start_window = GetStartupVariables.start_window
appearance_mode = GetStartupVariables.appearance_mode
