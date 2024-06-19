#!/usr/bin/python3
# Date: 09.02.24
# Author: Stocklasser
# DA Ideas
#

import customtkinter as ctk
# Shared variables----------------------------------------
from .sharedVar import geometry, colorSET, text_colorSET, \
    back_button_image  # import of shared variables located in the sharedVar file


class NewTestScreen(ctk.CTkFrame):  # class for the NewTestScreen window
    def __init__(self, parent):  # the parent is App()
        super().__init__(parent,  # parameters of the CTkFrame object
                         width=(geometry[0] - 10),
                         height=(geometry[1] - 10),
                         fg_color="transparent")
        self.place(x=5,  # placing the object at coordinates x5 - y5 relative to the top left corner of the parent
                   y=5)

        # calling the create_widgets method to create all widgets that are children of NewTestScreen
        self.create_widgets()

    def create_widgets(self):
        # top bar------------------------------------------------------------
        newtestscreen_indicator_bar = ctk.CTkLabel(master=self,  # top bar that indicates the screen where you are
                                                   fg_color=colorSET,
                                                   width=geometry[0] - 70,
                                                   height=40,
                                                   corner_radius=10,
                                                   text="New Test - Screen",
                                                   text_color=text_colorSET,
                                                   font=("bold", 20),
                                                   anchor="w")
        newtestscreen_indicator_bar.place(x=0,
                                          y=0)

        # back button------------------------------------------------------------

        newtestscreen_back_button = ctk.CTkButton(master=self,  # button for going back
                                                  width=40,
                                                  height=40,
                                                  corner_radius=10,
                                                  text="",
                                                  image=back_button_image,
                                                  command=lambda: self.master.open_top_level_window_really_switch("0"))
        # the command opens the top level window class "ReallySwitch" and passes "0" as the argument "which"
        newtestscreen_back_button.place(x=1215,
                                        y=0)

        # testfile config----------------------------------------
        # testfile general inputs frame----------------------------------------
        newtestscreen_input_frame = ctk.CTkFrame(master=self,  # Frame for the input fields and the next button
                                                 width=230,
                                                 height=270)
        newtestscreen_input_frame.place(x=525,
                                        y=(geometry[1] / 2) - 280)  # geometry is a sharedVar variable

        # input fields----------------------------------------
        firstname_label = ctk.CTkLabel(master=newtestscreen_input_frame,  # label for the firstname entry
                                       text="Firstname:",
                                       font=("Arial", 20))
        firstname_label.place(x=20,
                              y=20)

        firstname_var = ctk.StringVar()  # variable to store the following entry's input text

        firstname = ctk.CTkEntry(master=newtestscreen_input_frame,  # first name entry
                                 placeholder_text="First Name",
                                 textvariable=firstname_var)
        firstname.place(x=20,
                        y=50)

        # ----------------------------------------
        lastname_label = ctk.CTkLabel(master=newtestscreen_input_frame,  # label for the lastname entry
                                      text="Lastname:",
                                      font=("Arial", 20))
        lastname_label.place(x=20,
                             y=80)

        lastname_var = ctk.StringVar()  # variable to store the following entry's input text

        lastname = ctk.CTkEntry(master=newtestscreen_input_frame,  # lastname entry
                                placeholder_text="Last Name",
                                textvariable=lastname_var)
        lastname.place(x=20,
                       y=110)

        # ----------------------------------------
        birthdate_label = ctk.CTkLabel(master=newtestscreen_input_frame,  # label for the birthdate entry
                                       text="Birthdate [dd-mm-yy]:",
                                       font=("Arial", 20))
        birthdate_label.place(x=20,
                              y=140)

        birthdate_var = ctk.StringVar()  # variable to store the following entry's input text

        birthdate = ctk.CTkEntry(master=newtestscreen_input_frame,  # birthdate entry
                                 placeholder_text="Last Name",
                                 textvariable=birthdate_var)
        birthdate.place(x=20,
                        y=170)

        # ----------------------------------------
        next_button = ctk.CTkButton(master=newtestscreen_input_frame,  # next button to continue
                                    width=40,
                                    height=40,
                                    corner_radius=10,
                                    text="Next",
                                    command=lambda: print(str(lastname_var.get()) + "_"
                                                          + str(firstname_var.get()) + "_"
                                                          + str(birthdate_var.get())))
        # in this text the command generates a string which could be used as the name of a new folder,
        # here it is just printed
        next_button.place(x=20,
                          y=210)
