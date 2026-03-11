ATM Software Made Using Python

Author: Anthony Newlin
_____________________________________________________________________________________________________________________________________________________

INSTALLATION INSTRUCTIONS:
If folder is zipped, extract folder. Then open a new terminal in the "ATM System" folder. type ls in the terminal to ensure you see the scripts available, you should see these scripts:


Graphics - Folder Containing all pngs needed for GUI
account.py
atm_gui.py
main.py
account_data.py
data.csv


After you confirm these scripts are here. Type the following command:

python main.py


when you run that script, it will initialize an ATMGUI object from the atm_gui.py script, then you will see a new window pop up with the login screen. There will be a table to the left of the window with the account data from the data.csv file. (This is for simulated purposes only, you will never see this on a real ATM machine... hopefully)
_____________________________________________________________________________________________________________________________________________________

HOW TO USE ATM SYSTEM:
You can then input the account number and pin into the two entry boxs located in the middle of the window. If the data you inputted is valid it will verify with the csv and find the account name and balance and load it into the GUI. You will then be loaded into the main menu showing you four options: Check Balance, Get Cash (withdraw), Deposit, and Logout (back to main menu).

_____________________________________________________________________________________________________________________________________________________

CONFIGURATION INSTRUCTIONS:
To edit Account data, go to the ATM System folder and open the data.csv file. Once you have the file open you can add new accounts, edit account numbers, pins, names, and balances. (IF YOU EDIT THE CSV FILE. THE TABLE LOCATED ON THE LOGIN PAGE WILL BE INACURATE SINCE THE IMAGE IS NOT CONNECTED).



KNOWN BUGS:
After repeated testing, I've identified a minor issue where button clicks may occasionally fail to register or activate as expected.

_____________________________________________________________________________________________________________________________________________________

TROUBLESHOOTING INSTRUCTIONS:
In the case your program is not working, It is most likely the PNGS causing the issue, they may have corrupted when downloading or extracting. Redownload file and extract to a trusted folder. Then open a terminal in the folder "ATM System" then execute the command:

python main.py



CHANGE LOG:

1. Added Final Project Folder

2. Created Trello Board

3. Coded all the scripts except GUI

4. Finished GUI script

5. Imported Scripts to main.py

6. Created new ATMGUI object called atm

7. Created Comments for scripts

8. Edited Readme.txt



MIT License

Copyright (c) 2025 Anthony Newlin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.





CREDITS:

YouTube. (n.d.). Python tkinter tutorial for beginners. YouTube. https://www.youtube.com/playlist?list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T 


Tkinter - Python interface to TCL/TK. Python documentation. (n.d.). https://docs.python.org/3/library/tkinter.html 


ATM UI - Wincor Nixdorf - B_runo velloso. (n.d.). https://cargocollective.com/brunovelloso/ATM-UI-Wincor-Nixdorf 

