import sys
import os
import customtkinter as ctk
import logging as lg
import numpy as np

lg.getLogger(__name__)
log_file = "lgFile.log"
lg.basicConfig(
    filename=log_file,
    level=lg.DEBUG,
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filemode='w',
    )



crd = [
    50, #0
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


lg.info('END OF listing.PY' '\n' '------------------------------------------------------------------------------------------------------------')
