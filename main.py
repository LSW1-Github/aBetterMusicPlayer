import sys
import os
import customtkinter as ctk
import logging as lg
import numpy as np
import musicCon
from musicCon import *
import listing as lst
from listing import *


lg.getLogger(__name__)
lg.basicConfig(filename='log.log',
                    level=lg.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filemode='w',
                    )

class main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x720")
        try:
            self.boooop = 0.00
            self.sefont = musicCon.fonts()
            lg.info(f"{self.sefont} LOADED.")
            print(f"{self.sefont} LOADED.")
            


    #            self.firstFrame = ctk.CTkFrame(

            
            self.firstFrame = ctk.CTkFrame(
                master=self.root,
                bg_color=lst.clrs[2],
                fg_color= lst.clrs[6],
                width = 100,
                height = 100,
                )

            self.firstFrame.grid(
                row=0,
                column=0,
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )

    #            self.secondFrame = ctk.CTkFrame(

            self.secondFrame = ctk.CTkFrame(
                master=self.root,
                bg_color=lst.clrs[2],
                fg_color=lst.clrs[0],
                width = 100,
                height = 100,
                )
            
            self.secondFrame.grid(
                row=0,
                column=1,
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )


            self.thirdFrame = ctk.CTkFrame(
                master=self.root,
                bg_color=lst.clrs[2],
                fg_color=lst.clrs[0],
                width = 100,
                height = 100,
                )
            
            self.thirdFrame.grid(
                row=1,
                column=0,
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )

            self.fourthFrame = ctk.CTkFrame(
                master=self.root,
                bg_color=lst.clrs[2],
                fg_color=lst.clrs[0],
                width = 100,
                height = 100,
                )
            
            self.fourthFrame.grid(
                row=1,
                column=1,
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
    #            self.musicFrame = musicCon.create_musicFrame(root)
            self.button = ctk.CTkButton(
                master=self.firstFrame,
                command=self.boop,
                corner_radius=lst.crd[0],
                font=self.sefont,
                )
            
            self.button.grid(
                row=0,
                column=0,
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            


            self.switch_var = ctk.StringVar(value="on")
            self.switch = ctk.CTkSwitch(master=self.secondFrame,
                                        text="MUTED",
                                        width=120,
                                        height=100,
                                        switch_width = 90,
                                        switch_height = 60,
                                        corner_radius=lst.crd[0],
                                        border_width = 3,
                                        border_color=lst.clrs[1],
                                        fg_color = lst.clrs[6],
                                        bg_color=lst.clrs[2],
                                        progress_color= lst.clrs[0],
                                        button_color= lst.clrs[7],
                                        button_hover_color= lst.clrs[8],
                                        command=self.switch_event,
                                        variable=self.switch_var,
                                        font=self.sefont,
                                        onvalue="on",
                                        offvalue="off",
                                        state="normal",
                                        )
            self.switch.grid(
                row=0,
                column=0,
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )
            self.firstTextbox = ctk.CTkTextbox(
                master = self.fourthFrame,
                width = 300,
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
                row=0,
                column=0,
                padx=5,
                pady=5,
                ipady=5,
                ipadx=5,
                )


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
            self.firstLabel.configure(text=self.boooop)
            self.firstTextbox.insert("0.1", f' Boop ={self.boooop},' '\n')
            lg.info(f' {self.boooop}')
        except Exception as e:
            lg.exception(f"Error in boop: {e}")
            lg.info(f"Error in boop: {e}")
            print(f"Error in boop: {e}")

            
if __name__ == "__main__":
    root = ctk.CTk()
    app = main(root)
    root.mainloop()


"""
        self.musicFrame = musicCon.create_musicFrame(self )
        lg.info(f"self.musicFrame LOADED.")
        print(f"self.musicFrame LOADED.")
   


        self.loadLibraryButton = musicCon.create_loadLibraryButton(self )
        lg.info(f"self.loadLibraryButton LOADED.")
        print(f"self.loadLibraryButton LOADED.")

        self.addSongButton = musicCon.create_addSongButton(self )
        lg.info(f"self.addSongButton LOADED.")
        print(f"self.addSongButton LOADED.")

        self.addMultipleSongsButton = musicCon.create_addMultipleSongs(self )
        lg.info(f"self.addMultipleSongsButton LOADED.")
        print(f"self.addMultipleSongsButton LOADED.")


        self.playAlbumButton = musicCon.create_playAlbumButton(self )
        lg.info(f"self.playAlbumButton LOADED.")
        print(f"self.playAlbumButton LOADED.")

        self.playButton = musicCon.create_playButton(self )
        lg.info(f"self.playButton LOADED.")
        print(f"self.playButton LOADED.")

        self.pauseButton = musicCon.create_pauseButton(self )
        lg.info(f"self.pauseButton LOADED.")
        print(f"self.pauseButton LOADED.")
"""
