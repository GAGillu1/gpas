import urllib

from cryptography.fernet import Fernet
from sqlalchemy import create_engine

def decrypt():
    key =b'OdC2CFrHbvS7LORTLG1WgxmNGl6Xr0AP6Vbme7ak0Iw='
    encrypted_password=b'gAAAAABlU64o6lYpB4NJd76-ekFplN6VicHVoMYTqPX7RyBCtdT4FAFh8H_Tp1ULY5WPi34WoYfPn8Gz3QnhTG-lHq5ozoPIiA=='
    fernet=Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password)
    return decrypted_password.decode()

dbpw=decrypt()
def get_db_connection():
    encoded_password = urllib.parse.quote(dbpw, safe='')
    connection_string = f"postgresql://postgres:{encoded_password}@localhost:5432/gpa"
    engine=create_engine(connection_string)
    conn=engine.connect()
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="GPA",
    #     user="postgres",
    #     password=dbpw
    # )

    return conn

