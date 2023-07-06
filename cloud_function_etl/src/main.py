import psycopg2
import csv
import re

df_data = []

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # Explanation of the regex pattern:
    # ^               - Start of the string
    # [\w\.-]+        - One or more word characters, dots, or dashes (before the @ symbol)
    # @               - The @ symbol
    # [\w\.-]+        - One or more word characters, dots, or dashes (after the @ symbol)
    # \.              - A dot (before the domain)
    # \w+             - One or more word characters (the domain)
    # $               - End of the string

    if re.match(pattern, email):
        return True
    else:
        return False

def validate_ip(ip_address):

   if not re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip_address):
       print(f"The IP address {ip_address} is not valid")
       return False

   bytes = ip_address.split(".")

   for ip_byte in bytes:
       if int(ip_byte) < 0 or int(ip_byte) > 255:
           print(f"The IP address {ip_address} is not valid")
           return False
   print(f"The IP address {ip_address} is valid")
   return True

def read_excel_file():
    data = []
    with open('section1dataset.csv', 'r') as csv_file:
    #with open('test_data_5_rec.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        #df_data=[tuple(line) for line in csv_reader]

        for line in csv_reader:
          email = line[3]
          ip_address = line[5]
          print(ip_address + " is the ip_address")
          if validate_email(email):
              if validate_ip(ip_address):
                df_data.append(tuple(line))
              else:
                print(ip_address + " : IP Address is invalid.")
          else:
              print(email + " : Email is invalid.")

    return df_data

import re



def extract_data():
  print("This is extract data.")
  global df_data
  df_data = read_excel_file()
  
def transform_data():
  print("This is transform data.")
  global df_data

def load_data():
  global df_data
  try:
      connection = psycopg2.connect(user="postgres",
                                    password="password",
                                    host="localhost",
                                    database="postgres")

      cursor = connection.cursor()
      # Executing a SQL query to insert data into  table
      insert_query = """ INSERT INTO provider (id, first_name, last_name, email, gender, ip_address) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""

       # executemany() to insert multiple rows
      result = cursor.executemany(insert_query, df_data)
      connection.commit()
      print(cursor.rowcount, "Record inserted successfully into provider table")

      # Fetch result
      cursor.execute("SELECT * from provider LIMIT 5")
      record = cursor.fetchall()
      print("Result ", record)

  except (Exception, psycopg2.Error) as error:
      print("Error while connecting to PostgreSQL", error)
  finally:
      if connection:
          cursor.close()
          connection.close()
          print("PostgreSQL connection is closed")

def execute_pipeline():
  
  #Extract the data from excel file
  extract_data()  

  #Transform the data 
  transform_data()

  #Load the data into Postgresql Database
  load_data()

def main():
    execute_pipeline()

if __name__ == "__main__":
    main()
