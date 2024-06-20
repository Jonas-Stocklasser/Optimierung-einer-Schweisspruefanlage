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
class GetStartupVariables:
    with open("../Other/startup_var.json") as file:
        data = pd.read_json(file)
    name_of_app = data.loc[data['var'] == "name_of_app", "val"].values[0]
    window_geometry = data.loc[data['var'] == "window_geometry", "val"].values[0]
    color_SET = data.loc[data['var'] == "color_SET", "val"].values[0]
    text_color_SET = data.loc[data['var'] == "text_color_SET", "val"].values[0]
    start_window = data.loc[data['var'] == "start_window", "val"].values[0]
    appearance_mode = data.loc[data['var'] == "appearance_mode", "val"].values[0]
    window_size = data.loc[data["var"] == "window_size", "val"].values[0]
    x_size = 0
    y_size = 1
    if window_size == "HD":
        x_size = 0
        y_size = 1
    elif window_size == "FullHD":
        x_size = 2
        y_size = 3


name_of_app = GetStartupVariables.name_of_app
window_geometry = GetStartupVariables.window_geometry
color_SET = GetStartupVariables.color_SET
text_color_SET = GetStartupVariables.text_color_SET
start_window = GetStartupVariables.start_window
appearance_mode = GetStartupVariables.appearance_mode
window_size = GetStartupVariables.window_size
x_size = GetStartupVariables.x_size
y_size = GetStartupVariables.y_size
