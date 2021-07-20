import os

class Interface:
	def __init__(self):
		pass
	def main_menu(self):
		os.system("cls")
		print("Contact Apps")
		print("1. View Contacts")
		print("2. Add Contacts")
		print("3. Search Contact")
		print("4. Delete Contact")
		print("5. Update Contact")
		print("Q. Quit")