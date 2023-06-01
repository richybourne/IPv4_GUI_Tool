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
## Details
On launch up, the user has two choices:
![image](https://github.com/richybourne/IPv4_GUI_Tool/assets/99927081/2b4a3566-8962-4598-a49e-84db9c246444)
If Route Aggregation is selected the user is presented with:
![image](https://github.com/richybourne/IPv4_GUI_Tool/assets/99927081/49cb8bd1-0246-44d4-8c97-2b6b87cd652d)
After the user adds desired IP address fields, they insert IPv4 network addresses:
![image](https://github.com/richybourne/IPv4_GUI_Tool/assets/99927081/b037e20c-5015-4afe-afa8-1be74f05cb2a)
Upon selecting Aggregate!, the user is presented with the results:
![image](https://github.com/richybourne/IPv4_GUI_Tool/assets/99927081/d8983fdf-bfad-489b-a986-b844b4e30120)
Say the user presses Try Again!, then we are taken back to our first two choices, say the user hits Longest Prefix Match:
![image](https://github.com/richybourne/IPv4_GUI_Tool/assets/99927081/101fab84-3874-4b3c-b310-0e9556701cad)
First, the user selects the main address that will be compared, in otherwords, the destination IPv4 address:
![image](https://github.com/richybourne/IPv4_GUI_Tool/assets/99927081/0b7c58de-4964-438a-aaaf-19e38593edb2)
Now, the user adds desired amount of IP address fields to compare against:
![image](https://github.com/richybourne/IPv4_GUI_Tool/assets/99927081/0da94b33-6aec-4491-b70c-324ee0f5f676)
Upon selecting Find Best Match!, the user is presented with the results:
![image](https://github.com/richybourne/IPv4_GUI_Tool/assets/99927081/6a23771f-12bb-42f7-b735-a73ba419d8dc)
If the user hits Exit Gui, then the program ends
