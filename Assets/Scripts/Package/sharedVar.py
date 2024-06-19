#!/usr/bin/python3
# Date: 09.02.24
# Author: Stocklasser
# DA Ideas
#

import customtkinter as ctk
from PIL import Image   # library for image handling

# Pictures----------------------------------------
start_image = ctk.CTkImage(Image.open("../Images/Placeholder.png"), size=(600, 600))
back_arrow_image = ctk.CTkImage(dark_image=Image.open("../Images/Back_Arrow.png"), size=(30, 30))

# Shared variables----------------------------------------
window_geometry = [1280, 720]

nameofapp = "Schweißprüfung"
colorSET = "#3B8ED0"
text_colorSET = "#DCE4EE"
startwindow = "0"  # 0 = Start
