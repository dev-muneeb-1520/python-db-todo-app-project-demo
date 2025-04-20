import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def connectToDB():
  return mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
  )
  
def testDBConnection():
  try:
      conn = connectToDB()
      if conn.is_connected():
          print("Database connection successfull")
          conn.close()
      else:
          print("Failed to connect to the database")
  except Exception as error:
      print(f"Database connection error: {error}")