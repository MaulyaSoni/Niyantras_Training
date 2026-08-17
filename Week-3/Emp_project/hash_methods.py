# import bcrypt
from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()

def generate_hash_password(password:str):   
    # password_bytes = password.encode("utf-8")
    # hashed_password = bcrypt.hashpw(password_bytes , bcrypt.gensalt())
    # decoded_hash_password = hashed_password.decode("utf-8")
    # return decoded_hash_password
    return password_hash.hash(password)

def verify_hash_password(plain_password : str , hashed_password : str):
    
    # return bcrypt.checkpw(hashed_password.decode("utf-8") , plain_password.decode("utf-8"))
    
    return password_hash.verify(plain_password , hashed_password)
