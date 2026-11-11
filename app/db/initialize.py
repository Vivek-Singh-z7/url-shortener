from app.db.connection import get_connection
from dotenv import load_dotenv
from psycopg import sql
import os

load_dotenv()


def check_db() -> bool:
  conn = get_connection("postgres")
  
  db_name = os.getenv("DB_NAME")
  
  if conn is None:
    raise RuntimeError("PostgreSQL connection failed")
  try:
    with conn.cursor() as cur:
      cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
      
      result = cur.fetchone()
      
      if result:
        print(f"database {db_name} already exist")
        return True
      else:
        print(f"database {db_name} does not exist")
        return False
  finally:
    conn.close()

def create_db():
  db_name = os.getenv("DB_NAME")
  conn = get_connection("postgres")
  
  
  try:
    conn.autocommit = True
    with conn.cursor() as cur:
      cur.execute(
        sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name))
      )

    print(f"database '{db_name}' created successfully.")

  finally:
    conn.close()

def initialize_db():
  exists = check_db()
  
  if not exists:
    create_db()
    