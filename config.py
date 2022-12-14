import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "12694006")

API_HASH = os.environ.get("API_HASH", "8719d11809492f836004a39b42599215")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5959839520:AAGZzJDyN5u4gxj4g5ma3aiFQ3nWY6H-0XA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001758428532") 

DB_NAME = os.environ.get("DB_NAME","Balmiki")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Balmiki:Balmiki@cluster0.lmden.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/343f4d2225312f099f448.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '953377581').split()]

