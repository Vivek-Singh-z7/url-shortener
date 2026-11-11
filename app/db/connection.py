import psycopg
from dotenv import load_dotenv
import os
import time

load_dotenv()

def get_connection(database_name: str | None = None): 
  db_name =  database_name or os.getenv("DB_NAME")
  
  
  for i in range(5):
    try:
      conn = psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=db_name,
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
      )
      return conn
    
    except psycopg.OperationalError as err:
      print(f"connection attempt {i + 1} failed: {err}")
        
      if i == 4:
        raise RuntimeError("Could not  connect  to postgerSQL") from err
      
      time.sleep(2)