# Goal
Create remote keylogger in Python, disguise as a photo, remote transmit, and create a safety key to stop the program.
This is inspired by Blake White's project at: https://github.com/blwhit/Remote-Keylogger

# Code
## Imports
Begin importing Python libraries.
`tkinter` for GUI.
`pynput.keyboard` for capturing keystrokes.
`logging` for creating logfiles.
`os` for interacting with host OS (Windows).
`getpass, uuid, socket` to get host information.
`threading` to execute processes in unique threads.
`subproces` for running system commands.
## Setup
Some code uses the SMTP email service to use, along with temporary files to receive text output. The temporary file is disguised to blend in with Windows files as "license_win64_details.txt".
Using Gmail's SMTP service, this will send emails to remotely extract information.
## Host Info, WiFi Profiles
These functions will run once at the beginning of execution to collect host information: hostname, IP, username, saved WiFi profiles, MAC address, and username.
## Main Loop
These main functions in the main loop of the code will listen to keystrokes and write to the temp file. It will send data once it hits an increment of 500 bytes, and on program termination.
By default, there is a safety key which terminates the program: the right control button. Hitting the key will stop the program, delete the temp files, and show an easter egg.

# Executable Compile
This program can be compiled into a standalone using PyInstaller. If we save the file as a ".pyw" extension, the program will run in a mode "without console." This is to help stay undetected.
## WinRAR Packaging
Using WinRAR, we can package the files to be an SFX archive. The program will be embedded within a photo, and when it's opened, it will exectue the keylogger under the radar. We can disguise the icon and opening of the file, but can't change the file type to change from "Application".
# Demonstration
After opening the photo, the executable will run and begin sending emails of the host information and keystrokes. This loop will happen until the user presses the right control key, which terminates the program.
