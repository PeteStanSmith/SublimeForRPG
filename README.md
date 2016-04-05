# SublimeForRPG
Sublime for RPG coding written by Peter Smith 

Icebreak existing plugin extended.

#Installation Instructions

- Install Python
- Install Sublime Text 3.
- Install Package Control (like 'apt-get install' for Sublime).
- Install Edit Command Palette (optional - allows shortcut keys to be bound to sublime commands).
- Go to Preferences > Browse packages and create a folder called IceBreak.
- Add the icebreak.tmlanguage file to this location. This can be found on the P drive (P:\SublimeForRPG\SublimeForRPG version 2.3)
- Go to Preferences > Browse packages and extract systemitools to this location.
- Open checkout.py and change the username and password of ftp.login to be your tracey credentials.
- Open commit.py and change the username and password of ftp.login to be your tracey credentials.
- Create the directory c:\jhc\src\rpg\
- Create the directory c:\jhc\src\rpg\cr
- Replace the following file with everything between the braces []. Preferences > Commands - User

```
[
    {
       "caption": "RPG-checkout",
       "command":"checkout_from_tracey"
   },
       {
       "caption": "RPG-commit",
       "command":"commit_to_tracey"
   }
]
```
These commands will now be available from the command palette (Ctrl+Shift+P)

- You can bind these to shortcuts with Edit Command Palette by adding the following to Preferences > Key Bindings - User
```
[
    {"keys": ["ctrl+shift+7"],
       "command":"checkout_from_tracey",
       "args": {}
   },
   {"keys": ["ctrl+shift+9"],
       "command":"commit_to_tracey",
       "args": {}
   }
]
```
