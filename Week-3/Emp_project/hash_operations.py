from fastapi import FastAPI
from schema import Token , UsersResponse , UsersSchema , UserIn
import bcrypt 
import jwt


SECRET_KEY = "My_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recommend()
DUMMY_HASH =password_hash.hash("dummypassword")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db ={
    "jacob" : {
        "username":"jacob",
        "full_name":"Jacob Don",
        "email":"jacob@xyz.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled":False,
        },
}

def verify_pass(plain_password , hashed_password):
    return password_hash.verify(plain_password , hashed_password)

def get_pass_hashed(password):
    return password_hash.hash(password)

def get_user(db , username : str):
    if username in db:
        user_dict = db[username]
        return UserIn(user_dict)

def authenticate_user(temp_db , username : str , password : str):
    user = get_user(temp_db , username)
    if not user :
        verify_pass(password , DUMMY_HASH)
        return False
    if not verify_pass(password , user.hashed_password):
        return False
    return user


def generate_hash_password(password:str)->str:
    password_byte = password.encode("utf-8")
    hashed = bcrypt.hashpw(password_byte  , bcrypt.gensalt())


def check_hash_password():
    pass


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(status_code=401,detail="Could not validate credentials")
   
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
   
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
   
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")



@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]