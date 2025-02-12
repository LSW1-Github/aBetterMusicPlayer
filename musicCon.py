import sys
import os
import customtkinter as ctk
import logging as lg
import numpy as np
import listing as lst


################################


lg.getLogger(__name__)
lg.basicConfig(filename='log.log',
                    level=lg.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filemode='a',
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
def create_musicFrame (root):
    try:
        frame = ctk.CTkFrame(
            master=root,
            bg_color=lst.clrs[2],
            fg_color=lst.clrs[2],
            width = 100,
            height = 100,
            )
        frame.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            ipady=5,
            ipadx=5,
            )

        lg.info(f"Frame created successfully: {frame}")
        return frame
    except Exception as e:
        lg.exception(f"Error in create_musicFrame: {e}")

def create_addMultipleSongs(root):
    try:
        addMultipleSongsButton = ctk.CTkButton(
            master=root,
            command=addMultipleSongsBUTT,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[2],
            fg_color=lst.clrs[0],
            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            )
        addMultipleSongsButton.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            ipady=5,
            ipadx=5,
            )

        lg.info(f"addMultipleSongsButton created successfully: {addMultipleSongsButton}")
        return addMultipleSongsButton
    except Exception as e:
        lg.exception(f"Error in create_addMultipleSongs: {e}")

def create_addSongButton(root):
    try:
        addSongButton= ctk.CTkButton(
            master=root,
            command=addSongBUTT,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[2],
            fg_color=lst.clrs[0],
            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            )
        addSongButton.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            ipady=5,
            ipadx=5,
            )

        lg.info(f"addSongButton created successfully: {addSongButton}")
        return addSongButton
    except Exception as e:
        lg.exception(f"Error in create_addSongButton: {e}")
     
def create_loadLibraryButton (root):
    try:
        loadLibraryButton = ctk.CTkButton(
            master=root,
            command=loadLibraryBUTT,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[0],
            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            )
        loadLibraryButton.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            ipady=5,
            ipadx=5,
            )

        lg.info(f"loadLibraryButton created successfully: {loadLibraryButton}")
        return loadLibraryButton
    except Exception as e:
        lg.exception(f"Error in create_loadLibraryButton: {e}")








     
def create_pauseButton(root):
    try:
        pauseButton = ctk.CTkButton(
            master=root,
            command=pauseBUTT,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[0],

            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            )
        pauseButton.grid(
            row=0,
            column=2,
            padx=5,
            pady=5,
            ipady=5,
            ipadx=5,
            )

    except Exception as e:
        lg.exception(f'Error in create_pauseButton: {e}')

def create_playAlbumButton(root):
    try:
        playAlbumButton = ctk.CTkButton(
            master=root,
            command=playAlbumBUTT,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[0],

            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            )
        playAlbumButton.grid(
            row=0,
            column=3,
            padx=5,
            pady=5,
            ipady=5,
            ipadx=5,
            )

        lg.info(f"playAlbumButton created successfully: {playAlbumButton}")
        return playAlbumButton
    except Exception as e:
        lg.exception(f"Error in create_playAlbumButton: {e}")

def create_playButton(root):
    try:
        playButton = ctk.CTkButton(
        master=root,
        command=playBUTT,
        corner_radius=lst.crd[0],
        font=fonts(),
        bg_color=lst.clrs[0],

        border_color=lst.clrs[8],
        width = 50,
        height = 50,
        border_width = 5,
        border_spacing = 5,
        )
        playButton.grid(
            row=0,
            column=4,
            padx=5,
            pady=5,
            ipady=5,
            ipadx=5,
            )

    except Exception as e:
        lg.exception(f'Error in playButton: {e}')
        

################################
################################
################################
################################




################################


def addMultipleSongsBUTT():
    try:
        lg.info(f'addMultipleSongsBUTT - MULTIPLE SONGS ADDED TO LIBRARY')
    except Exception as e:
        lg.exception(f"Error in addMultipleSongsBUTT: {e}")

def addSongBUTT():
    try:
        lg.info(f'addSong - SONG IS NOW ADDED TO LIBRARY')
    except Exception as e:
        lg.exception(f"Error in addSong: {e}")

def loadLibraryBUTT():
    try:
        lg.info(f'loadLibraryBUTT - LOAD LIBRARY')
    except Exception as e:
        lg.exception(f"Error in loadLibraryBUTT: {e}")



def pauseBUTT():
    try:
        lg.info(f'pauseBUTT - '"NOW PAUSED")
    except Exception as e:
        lg.exception(f'Error in pauseBUTT: {e}')



def playAlbumBUTT():
    try:
        lg.info(f'playAlbum - PLAY ALBUM')
    except Exception as e:
        lg.exception(f'Error in playAlbum: {e}')


def playBUTT():
    try:
        lg.info(f'playBUTT - '"NOW PLAYING")

    except Exception as e:
        lg.exception(f'Error in playBUTT: {e}')

"""
