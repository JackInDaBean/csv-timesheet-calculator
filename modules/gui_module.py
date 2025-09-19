import tkinter as tk
from tkinter import filedialog 
import pandas as pd
import sys

class programGUI:
    """ GUI for the main program """
    def __init__(self, title = "CSV TimeSheet Calculator", width = 200, height = 75):
        self.root = tk.Tk()
        self.root.title = ("CSV TimeSheet Calculator")
        self.root.geometry(f"{width}x{height}")

        self.root.maxsize(width = 200, height = 150)
        self.root.minsize(width = 200, height = 150)

        open_csv_button = tk.Button(self.root, text = "Open CSV", command = self.open_csv_button_click)
        open_csv_button.pack(pady = 20)

        exit_button = tk.Button(self.root, text = "EXIT", command = self.exit_button_click)
        exit_button.pack(pady = 20)

    def exit_button_click(self):
        """ Closes the whole program once exit is clicked. """
        self.root.destroy()

    def run(self):
        """" Runs window and keeps it open throughout the program """
        self.root.mainloop()

    def open_csv_button_click(self):
        """ User clicks, opens the file dialog to open the CSV file and returns its path name to main. """ 
        global csv_file_path  
        csv_file_path = filedialog.askopenfilename(
            initialdir = "/",
            title = "Select a file",
         
           filetypes = [("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        self.root.destroy()

def save_text_file(finalData):
        """ Opens the file dialog to choose a location to save the finished file to. """
        file_path = filedialog.asksaveasfilename(
            defaultextension = ".txt",
            filetypes = [("Text files", "*.txt"), ("All files", "*.*")]
        )

        if file_path:
            try:
                finalData
                with open(file_path, 'w') as file:
                    file.write(finalData)
            except Exception as e:
                print("ERROR")
