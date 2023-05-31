import gui as gui
import sys 
from tkinter import messagebox as mb

###################################################################################################  
# Run our application, set up styles/properties, and set up intial resources for the continuous running of our application
###################################################################################################  
def main():
    # Start the application
    Launch=gui.IPv4_APP() # intiliaze the tk class
    # Set window properties
    Launch.geometry("1260x680")
    Launch.resizable(False, False)
    # Set GUI properties
    Launch.title("IPv4 Route Aggregation and Longest Prefix Match")
    # Load program
    Launch.login_screen()
    Launch.mainloop()
    exit()  

if __name__ == "__main__":
    main()