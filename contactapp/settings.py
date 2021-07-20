import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class Settings:

	def __init__(self):

		# APPS CONFIG
		self.active = True

		#DB CONFIG
		self.engine = create_engine(os.getenv("DB_URL"))
		self.db = scoped_session(sessionmaker(bind=self.engine))


	def load_data_contact(self):
		QUERY = "SELECT * FROM contacts ORDER BY name ASC;"
		contacts = self.db.execute(QUERY).fetchall()

		return contacts

	def input_new_contact(self, name, phone):
		QUERY = "INSERT INTO contacts (phone, name) VALUES (:phone, :name);"
		contact = self.db.execute(QUERY,{"phone":phone, "name":name})
		self.db.commit()

	def search_data_contact_by_name(self, name):
		QUERY = "SELECT * FROM contacts WHERE name = :name;"
		contact = self.db.execute(QUERY,{"name":name}).fetchone()

		return contact

	def delete_data_by_name(self,name):
		QUERY = "DELETE FROM contacts WHERE name = :name;"
		contact = self.db.execute(QUERY,{"name":name})
		self.db.commit()

		