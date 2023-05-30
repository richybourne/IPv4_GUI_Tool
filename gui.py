import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image, ImageTk

##  @brief The class that creates an instance of our application. This is our core of user interface.
 # 
 #         
 #  
 #  @param A tkinter library to access tkinter functions
 #  
 #  @return A object that is the GUI of our application
 #         
##
class IPv6_APP(tk.Tk):
    def __init__(self):
        super().__init__()
        self.mainFrame = tk.Frame(self, bg="white")
        self.mainFrame.pack(fill="both", expand=True)

    def login_screen(self):
        self.headerFrame = tk.Frame(self.mainFrame, bg="#ADD8E6")
        self.headerFrame.pack(fill="both", expand=True)

        title_label = tk.Label(self.headerFrame, text="IPv6 Route And Table GUI Tool", font="Ubuntu 35 bold", bg="#ADD8E6")
        title_label.pack(fill="x", expand=True, anchor="center")

        button_frame = tk.Frame(self.headerFrame, bg="#ADD8E6")
        button_frame.pack(anchor="center", expand=True)

        buttons_label = tk.Label(button_frame, text="Please choose one:", font="Ubuntu 15", bg="#ADD8E6")
        buttons_label.pack(fill="x", pady=6, expand=True, anchor="center")

        button1 = tk.Button(button_frame, text="Route Aggregation", font="Ubuntu 12 bold", command=self.show_route_aggregation)
        button1.pack(side="left", padx=40)

        button2 = tk.Button(button_frame, text="Table Summary", font="Ubuntu 12 bold", command=self.show_table_summary)
        button2.pack(side="left", padx=40)

        made_by_label = tk.Label(self.headerFrame, text="Made By: Ricardo Esquivel", font="Ubuntu 16", bg="#ADD8E6")
        made_by_label.pack(padx=10, pady=1, expand=True, anchor="center", side="bottom")

    def show_route_aggregation(self):
        # Clear the mainFrame
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

        # Create and display the route aggregation screen
        route_aggregation_label = tk.Label(self.mainFrame, text="Route Aggregation Screen", font="Ubuntu 20")
        route_aggregation_label.pack(side="top", fill="both", expand=True)

        back_button = tk.Button(self.mainFrame, text="Back", font="Ubuntu 12 bold", command=self.clear_and_go_back)
        back_button.pack(side="bottom", pady=10)

    def show_table_summary(self):
        # Clear the mainFrame
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

        # Create and display the table summary screen
        table_summary_label = tk.Label(self.mainFrame, text="Table Summary Screen", font="Ubuntu 20")
        table_summary_label.pack(side="top", fill="both", expand=True)

        back_button = tk.Button(self.mainFrame, text="Back", font="Ubuntu 12 bold", command=self.clear_and_go_back)
        back_button.pack(side="bottom", pady=10)

    def clear_and_go_back(self):
        # Clear the mainFrame
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

        # Display the login screen
        self.login_screen()
