# Description
This is a project done for CSE 151 Advanced Computer Networking made by Ricardo Esquivel.
The programs in this repo are Python programs that build and assist a Tkinter GUI app.
With this app, the main premise of the project is to provide automatic IPv4 tools.
Such tools are Automatic IPv4 network address aggregation and Automatic IPv4 Longest
Prefix Match Finder. Both tools are of choice within the GUI, as well as descriptions
to help a user understand why these tools are important.

## Files
All source code Python programs are found within the source_code folder.
Within the folder, you will find:
- gui.py         | Builds the user interface and handles user interaction.
- ipvalidator.py | Contains helper functions to validate IPv4 networks and addresses.
- aggregate.py   | A helper function to perform the aggregation algorithm/process. 
- bestmatch.py   | A helper function to perform the longest prefix-matching algorithm/process. 
- main.py        | The main program that starts up the GUI and continues the launch.

## Details


## Usage
If you would like to run the program, please clone this repo and run main.
Before running the main, ensure that you have:
```
A Python Version greater than 3.10
```
And have run these commands in your terminal. (supporting libraries)
```
pip install tkinter
```
```
pip install ipaddress
```
```
pip install os-sys
```