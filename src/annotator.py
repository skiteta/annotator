import os
import tkinter as tk
from tkinter import *
import argparse


class Annotator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.geometry('1060x610')
        self.master.title('Annotator')
        self.side_panel = tk.Frame(self.master, borderwidth=2, relief=tk.SUNKEN)
        self.canvas = None
        self.images = []
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.oval = None
        self.current_id = 0
        self.frame_num = None
        self.frame_data = {}
        self.scale_var = tk.DoubleVar()
        self.scale = None
        self.slider = None
        self.canvas.bind('<ButtonPress-1>', self.start_point_get)
        self.canvas.bind('<Button1-Motion>', self.oval_drawinig)
        if os.name == 'nt':
            self.canvas.bind('<Button3-Motion>', self.drag)
        else:
            self.canvas.bind('<Button2-Motion>', self.drag)
        self.canvas.bind('<ButtonRelease-1>', self.release_action)
        self.canvas.bind('<KeyPress>', self.key_event)

    def create_widgets(self):
        pass

    def load_movie(self):
        pass

    def scroll(self, event, scale_value=None):
        pass

    def start_point_get(self, event):
        pass

    def oval_drawing(self, event):
        pass

    def drag(self, event):
        pass

    def release_action(self, event):
        pass

    def detect_object(self):
        pass


if __name__ == '__main__':
    annotator = Annotator()
