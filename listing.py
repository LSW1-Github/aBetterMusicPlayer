import sys
import os
import customtkinter as ctk
import logging
import numpy as np

lg = logging.getLogger(__name__)
logging.basicConfig(filename='log.log',
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S"
                    )


crd = [
    90, #0
    ]

clrs = [
    "black", #0
    "white", #1
    "transparent", #2
    "green", #3
    "blue", #4
    "red", #5
    "light green", #6
    "pink", #7
    "light blue", #8
    "dark green" #9
    ]

def create_firstTextbox(root):
    try:
        firstTextbox = ctk.CTkTextbox(
                master = self.firstFrame,
                width = 400,
                height = 100,
                corner_radius=lst.crd[0],
                border_width = 5,
                border_spacing = 3,
                fg_color = lst.clrs[1],
                border_color = lst.clrs[0],
                text_color = lst.clrs[0],
                scrollbar_button_color = lst.clrs[7],
                scrollbar_button_hover_color = lst.clrs[3],
                font=self.sefont,
                activate_scrollbars = "normal",
                )
            
        firstTextbox.grid(
            row=0,
            column=2,
            padx=50,
            pady=50,
            ipady=50,
            ipadx=50,
            )
        lg.info(f"firstTextbox created successfully: {firstTextbox}")

        return firstTextbox
    except Exception as e:
        lg.Exception(f"Error in create_firstTextbox: {e}")
