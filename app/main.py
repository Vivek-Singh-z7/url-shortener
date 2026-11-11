from fastapi import FastAPI
from app.db.initialize import initialize_db
from app.db.schema import create_urls_table


initialize_db()
create_urls_table()


app = FastAPI(
  title="URL Shortener API",
  version="1.0.0",
)

