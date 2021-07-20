import os

class Contact:

	def __init__(self,App):
		self.settings = App.settings
		#self.contact_list = self.settings.load_data_contact()

	def add_contacts(self):
		os.system("cls")
		print("\n Add New Contact")
		name = input("Name\t:")
		phone = input("Phone\t:")
		confirm = input("Are you sure to save this contact ? (y/n)")
		if confirm.lower() == 'y':
			self.settings.input_new_contact(name, phone)
			print("Contact Saved")
		else:
			print("Canceled")
		input("Press ENTER to main menu")

	def view_contacts(self):
		os.system("cls")
		print("\nView All Contacts")
		contacts = self.settings.load_data_contact()
		if len(contacts) == 0:
			print("No contacts")
		else:
			for contact in contacts:
				print(contact.name , contact.phone)

		input("Press ENTER to Main Menu")

	def search_contacts(self):
		os.system("cls")
		print("\n Search Contact")
		name = input("Name\t:")
		contact = self.settings.search_data_contact_by_name(name)
		if contact:
			print("Contact found")
			print(f"Name \t:{contact.name}\tPhone \t:{contact.phone}")

		else:
			print("Not found")

		input("Press ENTER to Main Menu")

	def delete_contacts(self):
		os.system("cls")
		print("\n Delete Contact")
		name = input("Name\t:")
		contact = self.settings.search_data_contact_by_name(name)
		if contact:
			confirm = input("Are you sure? (y/n)")
			if confirm.lower() == 'y':
				self.settings.delete_data_by_name(contact.name)
			print("Contact deleted")
		else :
			print("Not Found")

		input("Press ENTER to Main Menu")

