#!/usr/bin/python3
# Date: 09.02.24
# Author: Stocklasser
# DA Ideas
#

import customtkinter as ctk
from PIL import Image  # library for image handling

# Shared variables----------------------------------------
geometry = [1280, 720]          # all shared variables are here
nameofapp = "DEMO_IDEAS - Stocklasser"
colorSET = "#3a7ebf"
text_colorSET = "#DCE4EE"
startwindow = "0"  # 0 = HOME
start_example_picture = ctk.CTkImage(dark_image=Image.open("../Images/start_example_picture.png"), size=(600, 600))
back_button_image = ctk.CTkImage(dark_image=Image.open("../Images/back_button_image.png"), size=(30, 30))
