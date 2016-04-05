Install sublime text 3.
Install package control.
Install edit command palette.
Go to Preferences > Browse packages and create a folder called IceBreak.
Add the icebreak.tmlanguage file to this location.
Go to Preferences > Browse packages and extract systemitools to this location.
Open checkout.py and change the username and password of ftp.login to be your tracey credentials.
Open commit.py and change the username and password of ftp.login to be your tracey credentials.
Create the directory c:\jhc\src\rpg\
Create the directory c:\jhc\src\rpg\cr

Replace the following file with everything between the braces [].
preferences > commands - user
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

These commands will now be available from the command palette (Ctrl+Shift+P)
