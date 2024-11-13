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
`subprocess` for running system commands.

![image](https://github.com/user-attachments/assets/3b3d3634-27fb-40f8-96a4-d05dad01a894)

## Setup
Some code uses the SMTP email service to use, along with temporary files to receive text output. The temporary file is disguised to blend in with Windows files as "license_win64_details.txt".
Using Gmail's SMTP service, this will send emails to remotely extract information.

![image](https://github.com/user-attachments/assets/3610f092-c791-4809-8744-b3791f3ee0a8)

## Host Info, WiFi Profiles
These functions will run once at the beginning of execution to collect host information: hostname, IP, username, saved WiFi profiles, MAC address, and username.

![image](https://github.com/user-attachments/assets/3c4fd67b-6a8f-4844-9b8f-4497f6dc8c4a)
![image](https://github.com/user-attachments/assets/57ab46fc-45db-41de-aa61-eef3d0d4a29b)

## Main Loop
These main functions in the main loop of the code will listen to keystrokes and write to the temp file. It will send data once it hits an increment of 500 bytes, and on program termination.
By default, there is a safety key which terminates the program: the right control button. Hitting the key will stop the program, delete the temp files, and show an easter egg.

![image](https://github.com/user-attachments/assets/10ec12cb-f793-4bd2-96bd-f0e86dc9c53d)
![image](https://github.com/user-attachments/assets/62dbb39a-8b9e-436f-b42a-a21bc01554b4)

![image](https://github.com/user-attachments/assets/4122af15-992e-42c6-ade6-d11927cd4a66)

# Executable Compile
This program can be compiled into a standalone using PyInstaller. If we save the file as a ".pyw" extension, the program will run in a mode "without console." This is to help stay undetected.
