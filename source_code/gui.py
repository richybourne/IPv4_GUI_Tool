import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image, ImageTk

class IPv6_APP(tk.Tk):
    def __init__(self):
        super().__init__()
        self.mainFrame = tk.Frame(self, bg="#ADD8E6")
        self.mainFrame.pack(fill="both", expand=True)
        self.ip_fields = []  # List to store the IP address fields

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
        self.aggregation_frame = tk.Frame(self.mainFrame, bg="#57A0D3")
        self.aggregation_frame.pack(fill="both", expand=True)

        route_aggregation_label = tk.Label(self.aggregation_frame, text="Route Aggregation Tool", font="Ubuntu 20 bold", background="#57A0D3")
        route_aggregation_label.pack(side="top", fill="both", expand=True)

        route_aggregation_sublabel = tk.Label(self.aggregation_frame, text="Please enter IP addresses (must be fully decompressed and valid)\nin the form (e.g: 2001:0db8:85a3:0000:0000:8a2e:0370:7334) you would like to aggregate", font="Ubuntu 10", background="#57A0D3")
        route_aggregation_sublabel.pack(side="top", fill="both", expand=True)

        button_frame = tk.Frame(self.aggregation_frame, bg="#57A0D3")
        button_frame.pack(side="bottom", pady=10)

        back_button = tk.Button(button_frame, text="Back", font="Ubuntu 12 bold", command=self.clear_and_go_back)
        back_button.pack(side="left", padx=10)

        add_field_button = tk.Button(button_frame, text="Add IP Address Field", font="Ubuntu 12 bold", command=lambda: self.add_ip_field(self.aggregation_frame))
        add_field_button.pack(side="left", padx=10)

        aggregate_button = tk.Button(button_frame, text="Aggregate!", font="Ubuntu 12 bold", command=self.aggregate_output)
        aggregate_button.pack(side="left", padx=10)

    def show_table_summary(self):
        # Clear the mainFrame
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

        # Create and display the table summary screen
        self.summary_frame = tk.Frame(self.mainFrame, bg="#57A0D3")
        self.summary_frame.pack(fill="both", expand=True)

        table_summary_label = tk.Label(self.summary_frame, text="Table Summary Tool", font="Ubuntu 20 bold", background="#57A0D3")
        table_summary_label.pack(side="top", fill="both", expand=True)

        table_summary_sublabel = tk.Label(self.summary_frame, text="Please enter IP addresses (must be fully decompressed and valid)\nin the form (e.g: 2001:0db8:85a3:0000:0000:8a2e:0370:7334) you would like to summarize", font="Ubuntu 10", background="#57A0D3")
        table_summary_sublabel.pack(side="top", fill="both", expand=True)

        button_frame = tk.Frame(self.summary_frame, bg="#57A0D3")
        button_frame.pack(side="bottom", pady=10)

        back_button = tk.Button(button_frame, text="Back", font="Ubuntu 12 bold", command=self.clear_and_go_back)
        back_button.pack(side="left", padx=10)

        add_field_button = tk.Button(button_frame, text="Add IP Address Field", font="Ubuntu 12 bold", command=lambda: self.add_ip_field(self.summary_frame))
        add_field_button.pack(side="left", padx=10)

        summarize_button = tk.Button(button_frame, text="Summarize!", font="Ubuntu 12 bold", command=self.summary_output)
        summarize_button.pack(side="left", padx=10)


    def clear_and_go_back(self):
        # Clear the mainFrame
        for widget in self.mainFrame.winfo_children():
            widget.destroy()
        self.ip_fields = []
        # Display the login screen
        self.login_screen()

    def add_ip_field(self, frame):
        # Add an IP address field to the screen, but only if there are less than 12 fields
        if len(self.ip_fields) < 14:
            field_frame = tk.Frame(frame, bg="#57A0D3")
            field_frame.pack(side="top", pady=5, fill="x", anchor="center")

            label = tk.Label(field_frame, text="Enter an IPv6 Address:", font="Ubuntu 12 bold", bg="#57A0D3")
            label.pack(side="left", padx=5)

            ip_field = tk.Entry(field_frame, font="Ubuntu 12")
            ip_field.pack(side="left", fill="x", anchor="center", expand=True, padx=80)

            self.ip_fields.append(ip_field)
        else:
            mb.showinfo("Maximum Fields Reached", "You have reached the maximum number of IP address fields (14).")

