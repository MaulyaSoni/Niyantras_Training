import bcrypt

def generate_hash_password(password):   
    password_bytes = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password_bytes , bcrypt.gensalt())
    decoded_hash_password = hashed_password.decode("utf-8")
    return decoded_hash_password

def verify_hash_password(hashed_password : str , plain_password : str):
    return bcrypt.checkpw(hashed_password.decode("utf-8") , plain_password.decode("utf-8"))
    
