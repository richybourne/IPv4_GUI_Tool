import gui as gui
import sys 
from tkinter import messagebox as mb

###################################################################################################  
# Run our application, set up styles/properties, and set up intial resources for the continuous running of our application
###################################################################################################  
def main():
    # Start the application
    Launch=gui.IPv6_APP() # intiliaze the tk class
    # Set window properties
    Launch.geometry("1260x680")
    Launch.resizable(False, False)
    # Set GUI properties
    Launch.title("IPv6 Route Aggregation and Table Summary")
    # Load program
    Launch.login_screen()
    Launch.mainloop() 

if __name__ == "__main__":
    main()