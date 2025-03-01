import sys
import os
import subprocess
import customtkinter as ctk
import logging as lg
import numpy as np
import musicCon as msCn
from musicCon import *
import listing as lst
from listing import *
import pygame
from pygame import *

mus = pygame.mixer

lg_file = "lgFile.log"
lg.basicConfig(
    filename=lg_file,
    level=lg.DEBUG,
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filemode='w',
    )
lg = lg.getLogger(__name__)

placement = [
    0,#0
    1, #1
    2, #2
    3, #3
    4, #4
    5, #5
    ]


class main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x720")
        lg.info('APPLICATION STARTED' '\n' '------------------------------------------------------------------------------------------------------------')
        
        try:
            mus.init(frequency=48000, buffer=1024) 
            lg.info(f' mus.init = {mus.init}')
            self.boooop = 0.00
            self.sefont = msCn.fonts()
            lg.info(f"{self.sefont} LOADED.")
            ############# FIRST FRAME ####################
            self.firstFrame = ctk.CTkFrame(
                master=self.root,
                bg_color=lst.clrs[2],
                fg_color= lst.clrs[6],
                width = 100,
                height = 100,
                )
            self.firstFrame.grid(
                row=placement[0],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            ############# FIRST FRAME ####################
            ############# FIRST FRAME ####################
            self.switch_var = ctk.StringVar(value="on")
            self.switch = ctk.CTkSwitch(
                master=self.firstFrame,
                text="MUTED",
                width=120,
                height=100,
                switch_width = 90,
                switch_height = 60,
                corner_radius=lst.crd[0],
                border_width = 3,
                fg_color = lst.clrs[6],
                bg_color=lst.clrs[2],
                progress_color= lst.clrs[0],
                button_color= lst.clrs[7],
                button_hover_color= lst.clrs[8],
                command=self.switch_event,
                variable=self.switch_var,
                font=self.sefont,
                text_color = clrs[0],
                border_color=lst.clrs[8],
                onvalue="on",
                offvalue="off",
                state="normal",
                )
            self.switch.grid(
                row=placement[0],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            
            self.openLogButton = ctk.CTkButton(
                master=self.firstFrame,
                command=self.openLog,
                corner_radius=lst.crd[0],
                fg_color="grey",
                font=self.sefont,
                text="openLog",
                text_color = clrs[0],
                border_color=lst.clrs[8],
                width = 50,
                height = 50,
                border_width = 5,
                border_spacing = 5,
                )
            self.openLogButton.grid(
                row=placement[0],
                column=placement[1],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            ############# SECOND FRAME ####################
            ############# SECOND FRAME ####################
            self.secondFrame = ctk.CTkFrame(
                master=self.root,
                bg_color=lst.clrs[2],
                fg_color=lst.clrs[0],
                width = 100,
                height = 100,
                )

            self.secondFrame.grid(
                row=placement[1],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            ############# SECOND FRAME ####################
            ############# SECOND FRAME ####################
            self.firstTextbox = ctk.CTkTextbox(
                master = self.secondFrame,
                width = 700,
                height = 400,
                corner_radius= crd[0],
                border_width = 5,
                border_spacing = 3,
                fg_color = clrs[1],
                border_color = clrs[0],
                text_color = clrs[0],
                scrollbar_button_color = clrs[7],
                scrollbar_button_hover_color = clrs[3],
                font=self.sefont,
                activate_scrollbars = "normal",
                )

            self.firstTextbox.grid(
                row=placement[0],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            ############# THIRD FRAME ####################
            ############# THIRD FRAME ####################
            self.thirdFrame = ctk.CTkFrame(
                master=self.root,
                bg_color=lst.clrs[2],
                fg_color=lst.clrs[0],
                width = 100,
                height = 100,
                )

            self.thirdFrame.grid(
                row=placement[2],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            ############# THIRD FRAME ####################
            ############# THIRD FRAME ####################
            self.boopButton = ctk.CTkButton(
                master=self.thirdFrame,
                command=self.boop,
                corner_radius=lst.crd[0],
                fg_color="grey",
                font=self.sefont,
                text="BOOP",
                text_color = lst.clrs[0],
                border_color=lst.clrs[8],
                width = 50,
                height = 50,
                border_width = 5,
                border_spacing = 5,
                )
            self.boopButton.grid(
                row=placement[0],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            ############# FOURTH FRAME ####################
            ############# FOURTH FRAME ####################
            self.fourthFrame = ctk.CTkFrame(
                master=self.root,
                bg_color=lst.clrs[2],
                fg_color=lst.clrs[0],
                width = 100,
                height = 100,
                )

            self.fourthFrame.grid(
                row=placement[3],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            ############# FOURTH FRAME ####################
            ############# FOURTH FRAME ####################
            self.addMultipleSongsButton = ctk.CTkButton(
                master=self.fourthFrame,
                command=self.addMultipleSongsBUTT,
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                border_color=lst.clrs[8],
                width = 50,
                height = 50,
                border_width = 5,
                border_spacing = 5,
                text="Add Multiple Songs Button"
                )
            self.addMultipleSongsButton.grid(
                row=placement[0],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )

            self.addSongButton= ctk.CTkButton(
                master=self.fourthFrame,
                command=self.addSongBUTT,
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                border_color=lst.clrs[8],
                width = 50,
                height = 50,
                border_width = 5,
                border_spacing = 5,
                text="Add Song Button"
                )
            self.addSongButton.grid(
                row=placement[0],
                column=placement[1],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            ############# MUSIC FRAME ####################
            ############# MUSIC FRAME ####################
            self.musicFrame = ctk.CTkFrame(
                master=self.root,
                bg_color=lst.clrs[2],
                fg_color=lst.clrs[2],
                width = 100,
                height = 100,
                )
            self.musicFrame.grid(
                row=placement[4],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            ############# MUSIC FRAME ####################
            ############# MUSIC FRAME ####################
            self.loadLibraryButton = ctk.CTkButton(
                master=self.musicFrame,
                command=self.loadLibraryBUTT,
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                border_color=lst.clrs[8],
                width = 50,
                height = 50,
                border_width = 5,
                border_spacing = 5,
                text="Load Library Button"
                )
            self.loadLibraryButton.grid(
                row=placement[0],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )

            self.pauseButton = ctk.CTkButton(
                master=self.musicFrame,
                command=self.pauseBUTT,
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                border_color=lst.clrs[8],
                width = 50,
                height = 50,
                border_width = 5,
                border_spacing = 5,
                text="Pause Button"
                )
            self.pauseButton.grid(
                row=placement[0],
                column=placement[1],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )

            self.playAlbumButton = ctk.CTkButton(
                master=self.musicFrame,
                command=self.playAlbumBUTT,
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                border_color=lst.clrs[8],
                width = 50,
                height = 50,
                border_width = 5,
                border_spacing = 5,
                text="Play Album Button"
                )
            self.playAlbumButton.grid(
                row=placement[0],
                column=placement[2],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )

            self.playButton = ctk.CTkButton(
                master=self.musicFrame,
                command=self.playBUTT,
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                border_color=lst.clrs[8],
                width = 50,
                height = 50,
                border_width = 5,
                border_spacing = 5,
                text="Play Button"
                )
            self.playButton.grid(
                row=placement[0],
                column=placement[3],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )

            self.checkMixerButton = ctk.CTkButton(
                master=self.musicFrame,
                command=self.checkMixerStatus,
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                border_color=lst.clrs[8],
                width = 50,
                height = 50,
                border_width = 5,
                border_spacing = 5,
                text="Mixer Status"
                )
            self.checkMixerButton.grid(
                row=placement[1],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
                

            self.activateMixerButton = ctk.CTkButton(
                master=self.musicFrame,
                command=self.activateMixerStatus,
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                border_color=lst.clrs[8],
                width = 50,
                height = 50,
                border_width = 5,
                border_spacing = 5,
                text="Activate Mixer"
                )
            self.activateMixerButton.grid(
                row=placement[1],
                column=placement[1],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )




            self.shutDownMixerButton = ctk.CTkButton(
                master=self.musicFrame,
                command=self.shutDownMixerStatus,
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                border_color=lst.clrs[8],
                width = 50,
                height = 50,
                border_width = 5,
                border_spacing = 5,
                text="shut Down Mixer"
                )
            self.shutDownMixerButton.grid(
                row=placement[1],
                column=placement[2],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )






            ############# MUSIC FRAME ####################
            ############# MUSIC FRAME ####################
            ############# FIFTH FRAME #####################
            ############# FIFTH FRAME #####################
            ############# FIFTH FRAME #####################

            self.fifthFrame = ctk.CTkFrame(
                master=self.root,
                width=800,
                height=600,
                )
            self.fifthFrame.grid(
                row=placement[1],
                column=placement[1],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            ############# FIFTH FRAME #####################
            ############# FIFTH FRAME #####################
            ############# FIFTH FRAME #####################
            ############# FIFTH FRAME #####################

            self.artistLabel = ctk.CTkLabel(
                master=self.fifthFrame,
                width=20,
                height=3,
                text="Artist",
                bg_color=clrs[1],
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                )
            self.artistLabel.grid(
                row=placement[0],
                column=placement[0],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            
            self.albumLabel = ctk.CTkLabel(
                master=self.fifthFrame,
                width=20,
                height=3,
                text="Album",
                bg_color=clrs[1],
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                )
            self.albumLabel.grid(
                row=placement[0],
                column=placement[1],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )

            self.trackLabel = ctk.CTkLabel(
                master=self.fifthFrame,
                width=20,
                height=3,
                text="Track",
                bg_color=clrs[1],
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                )
            self.trackLabel.grid(
                row=placement[0],
                column=placement[2],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )

            self.yearLabel = ctk.CTkLabel(
                master=self.fifthFrame,
                width=20,
                height=3,
                text="Year",
                bg_color=clrs[1],
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                )
            self.yearLabel.grid(
                row=placement[0],
                column=placement[3],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )

            self.genreLabel = ctk.CTkLabel(
                master=self.fifthFrame,
                width=20,
                height=3,
                text="Genre",
                bg_color=clrs[1],
                corner_radius=lst.crd[0],
                font=self.sefont,
                text_color = clrs[0],
                )
            self.genreLabel.grid(
                row=placement[0],
                column=placement[4],
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )

            ############# FIFTH FRAME #####################
            ############# FIFTH FRAME #####################
            ############# FIFTH FRAME #####################
            ############# FIFTH FRAME #####################
        except Exception as e:
            lg.exception(f"Error in __init__: {e}")
            lg.info(f"Error in __init__: {e}")
            print(f"Error in __init__: {e}")


    def unload(self):
        try:
            self.firstTextbox.insert('0.1', 'UNLOADED LIBRARY,' '\n')
        except Exception as e:
            lg.exception(f"Error in unload: {e}")
            lg.info(f"Error in unload: {e}")
            print(f"Error in unload: {e}")

    def switch_event(self):
        try:
            isQuite = self.switch.cget("text")
            if isQuite =="MUTED":
                self.firstTextbox.insert("0.1", 'Unmuted,' '\n')
                self.switch.configure(text="")
            else:
                self.switch.configure(text="MUTED")
                self.firstTextbox.insert("0.1", 'Muted,' '\n')
                lg.info("MUTED")
        except Exception as e:
            lg.exception(f"Error in switch_event: {e}")
            lg.info(f"Error in switch_event: {e}")
            print(f"Error in switch_event: {e}")

    def boop(self):
        try:
            self.boooop += 10.0
            self.firstTextbox.insert("0.1", f' Boop ={self.boooop},' '\n')
            lg.info(f' {self.boooop}')
        except Exception as e:
            lg.exception(f"Error in boop: {e}")
            lg.info(f"Error in boop: {e}")
            print(f"Error in boop: {e}")

    def addSongBUTT(self):
        try:
            self.firstTextbox.insert("0.1", f'addSong - SONG IS NOW ADDED TO LIBRARY' '\n')
            lg.info(f'addSong - SONG IS NOW ADDED TO LIBRARY')
            self.firstTextbox.insert("0.1", 'addSong - SONG IS NOW ADDED TO LIBRARY,' '\n')

        except Exception as e:
            lg.exception(f"Error in addSong: {e}")

    def loadLibraryBUTT(self):
        try:
            lg.info(f'loadLibraryBUTT - LOAD LIBRARY')
            self.firstTextbox.insert("0.1", 'loadLibraryBUTT - LOAD LIBRARY,' '\n')
        except Exception as e:
            lg.exception(f"Error in loadLibraryBUTT: {e}")

    def pauseBUTT(self):
        try:
            self.firstTextbox.insert("0.1", f'addSong - SONG IS NOW ADDED TO LIBRARY' '\n')
            lg.info(f'pauseBUTT - '"NOW PAUSED")
            self.firstTextbox.insert("0.1", 'pauseBUTT - NOW PAUSE' '\n')
        except Exception as e:
            lg.exception(f'Error in pauseBUTT: {e}')

    def playAlbumBUTT(self):
        try:
            mus.play()            
            lg.info(f'playAlbum - PLAY ALBUM')
            self.firstTextbox.insert("0.1", 'playAlbum - PLAY ALBUM' '\n')

        except Exception as e:
            lg.exception(f'Error in playAlbum: {e}')


    def playBUTT(self):
        try:
            mus.play()
            lg.info(f'playBUTT - '"NOW PLAYING")
            self.firstTextbox.insert("0.1", 'playBUTT - NOW PLAYING,'  '\n')

        except Exception as e:
            lg.exception(f'Error in playBUTT: {e}')

    def addMultipleSongsBUTT(self):
        try:
            lg.info(f"self.addMultipleSongsBUTT LOADED.")
            self.firstTextbox.insert("0.1", 'self.addMultipleSongsBUTT LOADED' '\n')
        except Exception as e:
            lg.exception(f'Error in addMultipleSongsBUTT: {e}')

    def openLog(self):
        try:
            if os.path.exists(lg_file):
                try:
                    subprocess.run(["notepad.exe", lg_file], check=True)
                except FileNotFoundError:
                    lg.warning("FAILED TO OPEN LOG")
            else:
                lg.warning("FAILED TO OPEN LOG")
        except Exception as e:
            lg.exception(f'Error in openLog: {e}')

    def checkMixerStatus(self):
        try:
            lg.warning(f'mus.get_init()')
            self.firstTextbox.insert("0.1", f' MIXER STATUS = {mus.get_init()}.' '\n')
        except Exception as e:
            lg.exception(f'Error in checkMixerStatus: {e}')


    def activateMixerStatus(self):
        try:
            mus.init(frequency=48000, buffer=1024) 

            self.firstTextbox.insert("0.1", f' MIXER STATUS = ACTIVATED.' '\n')
        except Exception as e:
            lg.exception(f'Error in activateMixerStatus: {e}')



    def shutDownMixerStatus(self):
        try:
            mus.quit()

            self.firstTextbox.insert("0.1", f' MIXER STATUS = SHUT OFF.' '\n')
        except Exception as e:
            lg.exception(f'Error in shutDownMixerStatus: {e}')

                        
    lg.info('END OF MAIN.PY' '\n' '------------------------------------------------------------------------------------------------------------')



    
if __name__ == "__main__":
    root = ctk.CTk()
    app = main(root)
    root.mainloop()
