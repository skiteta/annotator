import os
import tkinter as tk
from tkinter import *
import argparse
import threading


class Annotator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.geometry('1060x610')
        self.master.title('Annotator')
        self.side_panel = tk.Frame(self.master, borderwidth=2, relief=tk.SUNKEN)
        self.canvas = tk.Canvas(self.master)
        self.create_widgets()
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
        self.canvas.bind('<Button1-Motion>', self.oval_drawing)
        if os.name == 'nt':
            self.canvas.bind('<Button3-Motion>', self.drag)
        else:
            self.canvas.bind('<Button2-Motion>', self.drag)
        self.canvas.bind('<ButtonRelease-1>', self.release_action)
        self.canvas.bind('<KeyPress>', self.key_event)

    def key_event(self, event):
        key = event.keysym
        if key == 'n' or key == 'Right':
            self.next_image(event)
        elif key == 'p' or key == 'Left':
            self.before_image(event)

    def next_image(self, event):
        self.canvas.focus_set()
        if self.current_id < self.frame_num - 1:
            self.current_id += 1
        self.scale_var.set(self.scale_var.get() + 1.0)
        self.scroll(event, self.current_id)

    def before_image(self, event):
        self.canvas.focus_set()
        if self.current_id > 0:
            self.current_id -= 1
        self.scale_var.set(self.scale_var.get() - 1.0)
        self.scroll(event, self.current_id)

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
    root = tk.Tk()
    annotator = Annotator(master=root)
    annotator.mainloop()
