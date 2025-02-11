import sys
import os
import customtkinter as ctk
import logging
import numpy as np
import listing as lst


################################



lg = logging.getLogger(__name__)
logging.basicConfig(filename='log.log',
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S"
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

################################
def create_musicFrame (root):
    try:
        frame = ctk.CTkFrame(
            master=root,
            bg_color=lst.clrs[2],
            fg_color=lst.clrs[2],
            corner_radius=lst.crd[0],
            width = 50,
            height = 50,
            )
        frame.grid(
            row=3,
            column=0,
            padx=20,
            pady=20,
            ipady=20,
            ipadx=20,
            )
        lg.info(f"Frame created successfully: {frame}")
        return frame
    except Exception as e:
        lg.exception(f"Error in create_musicFrame: {e}")

def create_addMultipleSongs(root):
    try:
        addMultipleSongsButton = ctk.CTkButton(
            master=root,
            command=addMultipleSongs,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[2],
            fg_color=lst.clrs[0],
            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            text = "addMultipleSongs",
            )
        addMultipleSongsButton.grid(
            row=0,
            column=1,
            padx=20,
            pady=20,
            ipady=20,
            ipadx=20,
            )
        lg.info(f"addMultipleSongsButton created successfully: {addMultipleSongsButton}")
        return addMultipleSongsButton
    except Exception as e:
        lg.exception(f"Error in create_addMultipleSongs: {e}")

def create_addSongButton(root):
    try:
        addSongButton= ctk.CTkButton(
            master=root,
            command=addSong,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[2],
            fg_color=lst.clrs[0],
            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            text = "addSong",
            )
        addSongButton.grid(
            row=0,
            column=2,
            padx=20,
            pady=20,
            ipady=20,
            ipadx=20,
            )
        lg.info(f"addSongButton created successfully: {addSongButton}")
        return addSongButton
    except Exception as e:
        lg.exception(f"Error in create_addSongButton: {e}")
     
def create_loadLibraryButton (root):
    try:
        loadLibraryButton = ctk.CTkButton(
            master=root,
            command=loadLibrary,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[2],
            fg_color=lst.clrs[0],
            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            text = "loadLibrary",
            )
        loadLibraryButton.grid(
            row=0,
            column=3,
            padx=20,
            pady=20,
            ipady=20,
            ipadx=20,
            )
        lg.info(f"loadLibraryButton created successfully: {loadLibraryButton}")
        return loadLibraryButton
    except Exception as e:
        lg.exception(f"Error in loadLibraryButton: {e}")

def create_nextButton(root):
    try:
        nextButton = ctk.CTkButton(
            master=root,
            command=nextBUTT,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[0],
            fg_color=lst.clrs[0],
            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            text = "nextButton",
            )
        nextButton.grid(
            row=0,
            column=4,
            padx=20,
            pady=20,
            ipady=20,
            ipadx=20,
            )
    except Exception as e:
        lg.exception(f'Error in create_nextButton: {e}')
     
def create_pauseButton(root):
    try:
        pauseButton = ctk.CTkButton(
            master=root,
            command=pauseBUTT,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[0],
            fg_color=lst.clrs[0],
            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            text = "pauseButton",
            )
        pauseButton.grid(
            row=0,
            column=5,
            padx=20,
            pady=20,
            ipady=20,
            ipadx=20,
            )
    except Exception as e:
        lg.exception(f'Error in create_pauseButton: {e}')

def create_playAlbumButton(root):
    try:
        playAlbumButton = ctk.CTkButton(
            master=root,
            command=playAlbum,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[0],
            fg_color=lst.clrs[0],
            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            text = "playAlbum",
            )
        playAlbumButton.grid(
            row=0,
            column=6,
            padx=20,
            pady=20,
            ipady=20,
            ipadx=20,
            sticky="n",
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
        fg_color=lst.clrs[0],
        border_color=lst.clrs[8],
        width = 50,
        height = 50,
        border_width = 5,
        border_spacing = 5,
        text = "playButton",
        )
        playButton.grid(
                    row=0,
                    column=7,
                    padx=20,
                    pady=20,
                    ipady=20,
                    ipadx=20,
                    )
    except Exception as e:
        lg.exception(f'Error in playButton: {e}')
        
def create_stopButton(root):
    try:
        stopButton = ctk.CTkButton(
            master=root,
            command=stopBUTT,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[0],
            fg_color=lst.clrs[0],
            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            text = "stopButton",
            )

        stopButton.grid(
            row=0,
            column=8,
            padx=20,
            pady=20,
            ipady=20,
            ipadx=20,
            )
    except Exception as e:
        lg.exception(f'Error in create_stopButton: {e}')

def unloadButton(root):
    try:
        unloadButton = ctk.CTkButton(
            master=root,
            command=unload,
            corner_radius=lst.crd[0],
            font=fonts(),
            bg_color=lst.clrs[0],
            fg_color=lst.clrs[0],
            border_color=lst.clrs[8],
            width = 50,
            height = 50,
            border_width = 5,
            border_spacing = 5,
            text = "unload",
            )

        unloadButton.grid(
            row=0,
            column=9,
            padx=20,
            pady=20,
            ipady=20,
            ipadx=20,
            )

    except Exception as e:
        lg.exception(f'Error in unloadButton: {e}')
        

################################
################################
################################
################################



def addMultipleSongs():
    try:
        lst.firstTextbox.insert('0.1', 'MULTIPLE SONGS ADDED TO LIBRARY,' '\n')
        lg.info(f'addMultipleSongs - MULTIPLE SONGS ADDED TO LIBRARY')
    except Exception as e:
        lg.exception(f"Error in addMultipleSongs: {e}")

def addSong():
    try:
        lst.firstTextbox.insert('0.1', 'SONG IS NOW ADDED TO LIBRARY,' '\n')
        lg.info(f'addSong - SONG IS NOW ADDED TO LIBRARY')
    except Exception as e:
        lg.exception(f"Error in addSong: {e}")

def loadLibrary():
    try:
        lst.firstTextbox.insert('0.1', 'LOAD LIBRARY,' '\n')
        lg.info(f'loadLibrary - '"LOAD LIBRARY")
    except Exception as e:
        lg.exception(f"Error in loadLibrary: {e}")

def nextBUTT():
    try:
        lst.firstTextbox.insert('0.1', 'NEXT TRACK,' '\n')
        lg.info(f'nextBUTT - '"NEXT TRACK")
    except Exception as e:
        lg.exception(f'Error in nextBUTT: {e}')
        
def playAlbum():
    try:
        lst.firstTextbox.insert('0.1', 'PLAY ALBUM,' '\n')
        lg.info(f'playAlbum - PLAY ALBUM')
    except Exception as e:
        lg.exception(f'Error in playAlbum: {e}')

def playBUTT():
    try:
        
        lst.firstTextbox.insert('0.1', 'NOW PLAYING,' '\n')
        lg.info(f'playBUTT - '"NOW PLAYING")

    except Exception as e:
        lg.exception(f'Error in playBUTT: {e}')

def pauseBUTT():
    try:
        lst.firstTextbox.insert('0.1', 'NOW PAUSED,' '\n')
        lg.info(f'pauseBUTT - '"NOW PAUSED")
    except Exception as e:
        lg.exception(f'Error in pauseBUTT: {e}')
        
def replayBUTT():
    try:
        lst.firstTextbox.insert('0.1', 'REPLAYING TRACK,' '\n')
        lg.info(f'replayBUTT - REPLAYING TRACK')
    except Exception as e:
        lg.exception(f'Error in replayBUTT: {e}')

def stopBUTT():
    try:
        lst.firstTextbox.insert('0.1', 'NOW STOPPED,' '\n')
        lg.info(f'stopBUTT - '"NOW STOPPED")
    except Exception as e:
        lg.exception(f'Error in stopBUTT: {e}')







################################
