import random
from app.db.connection import get_connection


def gen_short_code() -> str:
  try:
      
    length = 8
    code = []
    
    chars = ["qwertyuiopasdfghjklzxcvbnm","123456789"]
    
    for i in range(2):
      idx = 0
      code.append(chars[idx][random.randint(0,len(chars[idx])-1)])
      

    for i in range(length-2):
      idx = random.randint(0,len(chars)-1)
      code.append(chars[idx][random.randint(0,len(chars[idx])-1)])
    
    return "".join(code)
  except Exception as err:
    print(err)



def get_short_code() -> str:
  
  with get_connection() as conn:
    with conn.cursor() as cur:
      
      while True:
        code = gen_short_code()
          
        cur.execute("SELECT 1 FROM urls WHERE short_code = %s", (code,))
        res = cur.fetchone()
        
        if not res:
          return code

  