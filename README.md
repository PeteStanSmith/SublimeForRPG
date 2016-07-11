# SublimeForRPG
Sublime for RPG coding written by Peter Smith 

Icebreak existing plugin extended.

## Installation Instructions

- Install Python
- Install Sublime Text 3.
- Install Package Control (like 'apt-get install' for Sublime).
- Install Edit Command Palette (optional - allows shortcut keys to be bound to sublime commands).
- Go to Preferences > Browse packages and create a folder called IceBreak.
- Add the icebreak.tmlanguage file to this location. 
- Go to Preferences > Browse packages and extract systemitools to this location.
- Open checkout.py and change the username and password of ftp.login to be your credentials. 
- Still in checkout.py change ftp.login to be the target system.
```
ftp = FTP('systemgoeshere')

ftp.login('usernamegoeshere', 'passwordgoeshere')
```

- Open commit.py and make the same changes for system, password and username.
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

## Release notes

### 2.4
Now supports anycase file extensions.
Logging has been changed to append the new messages so that the file will contain a full history of checkouts and commits.
SQL source libraries have been added to include support for the ind, proc, trigger and view file extensions.
### 2.3
Identifies removed characters, ability to report on those that could be considered problematic.
### 2.2
Minor improvements to UI, allows the user to actively see whether a commit failed and what operation is running during execution.
### 2.1
Version 2.1 is here, offering far superior error logging and error handling, as well as some code re-factoring. Stand by for 2.2 next week since we have a 4 day weekend.
### 2.0
Version 2.0 is here! - The commands are now fully Sublime integrated, and include some level of options, validation and logging. It will still blank all of the source dates and will wipe out those pesky hex code highlighting characters people use to use in SEU. It is now mostly portable, it needs one tweak to the open file command if run on linux or mac os.
