# SublimeForRPG
Sublime for RPG coding written by Peter Smith.

Verion one install instructions for windows.

Install sublime text 3.
Install package control.
Install edit command palette.
Go to Preferences > Browsepackages and create a folder called IceBreak.
Add the icebreak.tmlanguage file to this location.
Create the directory c:\jhc\src\rpg\
Create the directory c:\jhc\src\rpg\cr
Extract the sublimeUtilities to c:\jhc\src\rpg\cr (creating the folding structure Create the directory c:\jhc\src\rpg\sublimeutilities)

Replace the following file with everything between the braces [].
preferences > commands - user
[
    {
        "caption": "checkout",
        "command":"exec",
        "args": {"cmd": "C:\\jhc\\src\\RPG\\SublimeUtilities\\keybindingcheckoutRPG.bat"}
    },
    {
        "caption": "checkin",
        "command":"exec",
        "args": {"cmd": "C:\\jhc\\src\\RPG\\SublimeUtilities\\keybindingcommitRPG.bat"}
    }
]

Replace the following file with everything between the braces [].
preferences > keybindings - user
[
    {"keys": ["ctrl+shift+1"],
        "command":"exec",
        "args": {"cmd": "C:\\jhc\\src\\RPG\\SublimeUtilities\\keybindingcheckoutRPG.bat"}
    },

    {"keys": ["ctrl+shift+9"],
        "command":"exec",
        "args": {"cmd": "C:\\jhc\\src\\RPG\\SublimeUtilities\\keybindingcommitRPG.bat"}
    }
]


