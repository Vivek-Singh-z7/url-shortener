from app.db.connection import get_connection

def create_urls_table():
  try:
    with get_connection() as conn:
      with conn.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS urls(
                      id BIGSERIAL PRIMARY KEY,
                      original_url TEXT NOT NULL,
                      short_code VARCHAR(8) UNIQUE NOT NULL,
                      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                      expires_at TIMESTAMP,
                      click_count INTEGER DEFAULT 0
                    )""")
        print("urls table created successfully ")
        conn.commit()
  except Exception:
    conn.rollback()
    raise
  finally:
    conn.close()
    
