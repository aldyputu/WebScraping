#module that we use:
#1. webbrowser; 2. requests; 3. bs4; 4. selenium

import webbrowser
import sys
import pyperclip

#check if the command line is more than 1 index
if len(sys.argv) > 1:
    #get address from command line, it will start from index 1 because index 0 is the command 
    address = ' '.join(sys.argv[1:])
else:
    #get address from clipboard
    address = pyperclip.paste()

webbrowser.open("https://www.google.co.id/maps/place/" + address, new=0, autoraise=True)


