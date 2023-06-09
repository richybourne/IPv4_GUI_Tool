#Libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
# Helper files
import ipvalidator as ipchecker
import aggregate as ipv4_aggregater
import bestmatch as ipv4_best_matcher

class IPv4_APP(tk.Tk):
    def __init__(self):
        super().__init__()
        self.mainFrame = tk.Frame(self, bg="#ADD8E6")
        self.mainFrame.pack(fill="both", expand=True)
        self.ip_fields = []  # List to store the IP address fields
        self.des_field = []

    def login_screen(self):
        self.headerFrame = tk.Frame(self.mainFrame, bg="#ADD8E6")
        self.headerFrame.pack(fill="both", expand=True)

        title_label = tk.Label(self.headerFrame, text="IPv4 Route And Matching GUI Tool", font="Ubuntu 35 bold", bg="#ADD8E6", fg="black")
        title_label.pack(fill="x", expand=True, anchor="center")

        button_frame = tk.Frame(self.headerFrame, bg="#ADD8E6")
        button_frame.pack(anchor="center", expand=True)

        buttons_label = tk.Label(button_frame, text="Please choose one:", font="Ubuntu 15", bg="#ADD8E6", fg="black")
        buttons_label.pack(fill="x", pady=6, expand=True, anchor="center")

        button1 = tk.Button(button_frame, text="Route Aggregation", font="Ubuntu 12 bold", command=self.show_route_aggregation)
        button1.pack(side="left", padx=40, ipadx=10, ipady=6)

        button2 = tk.Button(button_frame, text="Longest Prefix Match", font="Ubuntu 12 bold", command=self.show_best_match)
        button2.pack(side="left", padx=40, ipadx=10, ipady=6)

        made_by_label = tk.Label(self.headerFrame, text="Made By: Ricardo Esquivel\nFor the CSE151 Class Project", font="Ubuntu 16", bg="#ADD8E6", fg="black")
        made_by_label.pack(padx=10, pady=1, expand=True, anchor="center", side="bottom")
        
        description_frame = tk.Frame(self.headerFrame, bg="#ADD8E6")
        description_frame.pack(fill="both", pady=70, padx=70, anchor="center", side="bottom", expand=True)
        description_label = tk.Label(description_frame, 
                                     text="Usage: This is a GUI application to assist with automatic and rapid IPv4 manipulation. \nPlease select a choice to perform either Route Aggregation or Longest Prefix Match and follow subsequent instructions!", 
                                     font="Ubuntu 14", bg="#ADD8E6", fg="black")
        description_label.pack(padx=10, ipadx=10, anchor="center", side="bottom", expand=True, fill="both")

    def show_route_aggregation(self):
        # Clear the mainFrame
        for widget in self.mainFrame.winfo_children():
            widget.destroy()
        self.ip_fields = []
        # Create and display the route aggregation screen
        self.aggregation_frame = tk.Frame(self.mainFrame, bg="#57A0D3")
        self.aggregation_frame.pack(fill="both", expand=True)

        route_aggregation_label = tk.Label(self.aggregation_frame, text="Route Aggregation Tool", font="Ubuntu 32 bold", background="#57A0D3", fg="black")
        route_aggregation_label.pack(side="top", fill="both", expand=True)

        route_aggregation_sublabel = tk.Label(self.aggregation_frame, text="Please enter IP addresses (must be valid)\nin the form (e.g: 192.168.0.0/28) you would like to aggregate", font="Ubuntu 12", background="#57A0D3", fg="black")
        route_aggregation_sublabel.pack(side="top", fill="both", expand=True)

        button_frame = tk.Frame(self.aggregation_frame, bg="#57A0D3")
        button_frame.pack(side="bottom", pady=10)

        back_button = tk.Button(button_frame, text="Back", font="Ubuntu 12 bold", fg="black", command=self.clear_and_go_back)
        back_button.pack(side="left", ipadx=4, padx=5, ipady=2)

        add_field_button = tk.Button(button_frame, text="Add IP Address Field", font="Ubuntu 12 bold", command=lambda: self.add_ip_field(self.aggregation_frame))
        add_field_button.pack(side="left", ipadx=4, padx=5, ipady=2)

        aggregate_button = tk.Button(button_frame, text="Aggregate!", font="Ubuntu 12 bold", fg="black", command=self.aggregate_output)
        aggregate_button.pack(side="left", ipadx=4, padx=5, ipady=2)

    def show_best_match(self):
        # Clear the mainFrame
        for widget in self.mainFrame.winfo_children():
            widget.destroy()
        self.ip_fields = []
        self.des_field = []
        # Create and display the table summary screen
        self.summary_frame = tk.Frame(self.mainFrame, bg="#57A0D3")
        self.summary_frame.pack(fill="both", expand=True)

        table_summary_label = tk.Label(self.summary_frame, text="Longest Prefix Match Tool", font="Ubuntu 32 bold", fg="black", background="#57A0D3")
        table_summary_label.pack(side="top", fill="both", expand=True)

        table_summary_sublabel = tk.Label(self.summary_frame, text="Please enter a Destination IPv4 address with no subnet mask(e.g: 192.168.0.0)\nThen please enter subsequent IPv4 addresses to match against\nAll of which in the valid form(e.g: 192.168.0.0/28)", font="Ubuntu 12", background="#57A0D3", fg="black")
        table_summary_sublabel.pack(side="top", fill="both", expand=True)

        # Destination IP Address
        field_frame = tk.Frame(self.summary_frame, bg="#57A0D3")
        field_frame.pack(side="top", pady=5, fill="x", anchor="center")
        label = tk.Label(field_frame, text="Enter IPv4 Address to Match:", font="Ubuntu 12 bold", bg="#57A0D3", fg="black")
        label.pack(side="left", padx=5)
        des_ip_field = tk.Entry(field_frame, font="Ubuntu 12")
        des_ip_field.pack(side="left", fill="x", anchor="center", expand=True, padx=(29,80))
        self.des_field.append(des_ip_field)

        button_frame = tk.Frame(self.summary_frame, bg="#57A0D3")
        button_frame.pack(side="bottom", pady=10)

        back_button = tk.Button(button_frame, text="Back", font="Ubuntu 12 bold", fg="black", command=self.clear_and_go_back)
        back_button.pack(side="left", ipadx=4, padx=5, ipady=2)

        add_field_button = tk.Button(button_frame, text="Add IP Address Field", font="Ubuntu 12 bold", fg="black", command=lambda: self.add_ip_field_bm(self.summary_frame))
        add_field_button.pack(side="left", ipadx=4, padx=5, ipady=2)

        summarize_button = tk.Button(button_frame, text="Find Best Match!", font="Ubuntu 12 bold", fg="black", command=self.bmatch_output)
        summarize_button.pack(side="left", ipadx=4, padx=5, ipady=2)


    def clear_and_go_back(self):
        # Clear the mainFrame
        for widget in self.mainFrame.winfo_children():
            widget.destroy()
        self.ip_fields = []
        self.des_fields = []
        # Display the login screen
        self.login_screen()

    def add_ip_field(self, frame):
        # Add an IP address field to the screen, but only if there are less than 14 fields
        if len(self.ip_fields) < 14:
            field_frame = tk.Frame(frame, bg="#57A0D3")
            field_frame.pack(side="top", pady=5, fill="x", anchor="center")

            label = tk.Label(field_frame, text="Enter an IPv4 Address:", font="Ubuntu 12 bold", bg="#57A0D3", fg="black")
            label.pack(side="left", padx=5)

            ip_field = tk.Entry(field_frame, font="Ubuntu 12")
            ip_field.pack(side="left", fill="x", anchor="center", expand=True, padx=80)

            self.ip_fields.append(ip_field)
        else:
            mb.showinfo("Maximum Fields Reached", "You have reached the maximum number of IP address fields (14).")

    def add_ip_field_bm(self, frame):
        # Add an IP address field to the screen, but only if there are less than 13 fields
        if len(self.ip_fields) < 13:
            field_frame = tk.Frame(frame, bg="#57A0D3")
            field_frame.pack(side="top", pady=5, fill="x", anchor="center")

            label = tk.Label(field_frame, text="Enter an IPv4 Address:", font="Ubuntu 12 bold", bg="#57A0D3", fg="black")
            label.pack(side="left", padx=5)

            ip_field = tk.Entry(field_frame, font="Ubuntu 12")
            ip_field.pack(side="left", fill="x", anchor="center", expand=True, padx=80)

            self.ip_fields.append(ip_field)
        else:
            mb.showinfo("Maximum Fields Reached", "You have reached the maximum number of IP address fields (13).")

    def aggregate_output(self):
        ip_addresses = []
        for ip_field in self.ip_fields:
            ip = ip_field.get().strip()
            if ip:
                ip_addresses.append(ip)

        # Validate the IP addresses
        if (ipchecker.validate_ips(ip_addresses)) == False:
            mb.showerror("Invalid IP Addresses", "One or more of your IPv4 addresses are invalid. Please enter valid IP addresses.")
            return
        
        # Valid number of IP addresses greater than 2
        if len(ip_addresses) < 2:
            mb.showerror("Insufficient IP Addresses", "Please enter at least 2 IP addresses.")
            return

        # Perform route aggregation
        aggregated_ip_address = ipv4_aggregater.perform_ipv4_route_aggregation(ip_addresses)
        
        # Clear the mainFrame
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

        # Display the aggregated IP addresses
        ip_label = tk.Label(self.mainFrame, text="Your Aggregated IP Address:", font="Ubuntu 30 bold", bg="#ADD8E6", fg="black")
        ip_label.pack(pady=10)
        
        ip_entry = tk.Label(self.mainFrame, text=aggregated_ip_address, font="Ubuntu 20", bg="#ADD8E6", fg="black", border=6, relief="groove")
        ip_entry.pack(pady=80)

        des_label = tk.Label(self.mainFrame, text="What does this mean?\nAfter inputting your addresses, we summarized each route to produce ONE summary static route.\nWith this, your routes can now be reachable through one summarized IPv4 address.", font="Ubuntu 16 bold", bg="#ADD8E6", fg="black")
        des_label.pack(pady=10)

        des2_label = tk.Label(self.mainFrame, text="Overall, route aggregation plays a vital role in:\n optimizing routing efficiency, reducing routing table size, enhancing scalability, and improving network performance.\nIt is an essential technique for efficient network design and management in modern computer networks.", font="Ubuntu 16 bold", bg="#ADD8E6", fg="black")
        des2_label.pack(pady=10)

        button_frame = tk.Frame(self.mainFrame, bg="#ADD8E6")
        button_frame.pack(side="bottom", pady=50)

        try_again_button = tk.Button(button_frame, text="Try Again!", font="Ubuntu 12 bold",command=self.clear_and_go_back)
        try_again_button.pack(side="left", ipadx=4, padx=10, ipady=2)

        exit_button = tk.Button(button_frame, text="Exit GUI", font="Ubuntu 12 bold", command=self.end_application)
        exit_button.pack(side="left", ipadx=4, padx=10, ipady=2)

        button_frame.pack(anchor="center")


    def bmatch_output(self):
        # Get a copy of the IP address
        ip_addresses = []
        for ip_field in self.ip_fields:
            ip = ip_field.get().strip()
            if ip:
                ip_addresses.append(ip)

        # Get a copy of the des IP address
        des_addresses = []
        for ip_field in self.des_field:
            ip = ip_field.get().strip()
            if ip:
                des_addresses.append(ip)

        # Validate the Des addresses
        if (ipchecker.validate_ips_no_subnet(des_addresses)) == False:
            mb.showerror("Invalid IP Addresses", "One or more of your IPv4 addresses are invalid. Please enter valid IP addresses.")
            return

        # Valid number of IP addresses greater than 2
        if len(des_addresses) < 1:
            mb.showerror("Insufficient IP Addresses", "Please enter a Destination IP addresses.")
            return

        # Validate the IP addresses
        if (ipchecker.validate_ips(ip_addresses)) == False:
            mb.showerror("Invalid IP Addresses", "One or more of your IPv4 addresses are invalid. Please enter valid IP addresses.")
            return
        
        # Valid number of IP addresses greater than 2
        if len(ip_addresses) < 2:
            mb.showerror("Insufficient IP Addresses", "Please enter at least 2 IP addresses.")
            return

        # Clear the mainFrame
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

        # Display the Longest Matching IP
        ip_label = tk.Label(self.mainFrame, text="Your Longest Prefix Matching IP Address:", font="Ubuntu 30 bold", bg="#ADD8E6", fg="black")
        ip_label.pack(pady=10)

        # Perform best match lookup
        best_match_network_address = ipv4_best_matcher.perform_ipv4_best_match_lookup(des_addresses[0], ip_addresses)

        ip_entry = tk.Label(self.mainFrame, text=best_match_network_address, font="Ubuntu 20", bg="#ADD8E6", fg="black", border=6, relief="groove")
        ip_entry.pack(pady=80)

        des_label = tk.Label(self.mainFrame, text="What does this mean?\nAfter inputting the address to match on(destination address) and subsequent addresses, this IP is the longest matching.\nWith this, you now know which IP address would be used to forward a packet from your destination.", font="Ubuntu 16 bold", bg="#ADD8E6", fg="black")
        des_label.pack(pady=10)

        des2_label = tk.Label(self.mainFrame, text="Overall, longest prefix match is a critical concept in routing and forwarding packets within IP networks.\nIt enables key details such as:\n efficient packet forwarding, network segmentation, flexible route advertisement, load balancing, and traffic engineering.\nBy matching the most specific prefix, routers can accurately route packets and optimize network performance.", font="Ubuntu 16 bold", bg="#ADD8E6", fg="black")
        des2_label.pack(pady=10)

        button_frame = tk.Frame(self.mainFrame, bg="#ADD8E6")
        button_frame.pack(side="bottom", pady=50)

        try_again_button = tk.Button(button_frame, text="Try Again!", font="Ubuntu 12 bold", command=self.clear_and_go_back)
        try_again_button.pack(side="left", ipadx=4, padx=10, ipady=2)

        exit_button = tk.Button(button_frame, text="Exit GUI", font="Ubuntu 12 bold", command=self.end_application)
        exit_button.pack(side="left", ipadx=4, padx=10, ipady=2)

        button_frame.pack(anchor="center")
        
    def end_application(self):
        self.destroy()
