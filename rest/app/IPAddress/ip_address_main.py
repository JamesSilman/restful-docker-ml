import json
import mysql.connector

class IPAddress:

	def __init__(self, ip_address):#, server_ip):
		self.ip_address = ip_address
		#self.server_ip = server_ip

	def db_connection(self):
		global cnx

		cnx = mysql.connector.connect(
			user='root', 
			password='root',
            host='sql',
            database='intelligence'
            )
	
	def prepare_ip_address(self):
		return self.ip_address.replace('.', '')

	
	def get_ip_details(self):
		self.db_connection()

		cursor = cnx.cursor(dictionary=True)
		query = ("SELECT * FROM ip2location_db9 WHERE ip_to >= %s ORDER BY ip_to limit 1")
		cursor.execute(query, (self.prepare_ip_address(),))
		
		for ip in cursor:
			return ip 
			
		


