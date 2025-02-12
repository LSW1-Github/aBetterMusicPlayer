import sys
import os
import customtkinter as ctk
import logging as lg
import numpy as np
import listing as lst


################################


lg.getLogger(__name__)
log_file = "lgFile.log"
lg.basicConfig(
    filename=log_file,
    level=lg.DEBUG,
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filemode='w',
    )
################################

def fonts():
    try:
        font = (
            'Times New Roman',
            24,
            "bold"
                ) 
        lg.info(f'fonts()')
        return font
    except Exception as e:
        lg.exception(f"Error in fonts: {e}")
        print(f"Error in fonts: {e}")

"""
################################

        

################################
################################
################################
################################




################################




"""
