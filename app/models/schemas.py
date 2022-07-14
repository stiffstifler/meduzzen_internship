from pydantic import BaseModel, EmailStr

class User(BaseModel):
    f_name: str
    l_name: str
    age: int
    city: str
    email: EmailStr
    password: str


class SignIn(BaseModel):
    email: EmailStr
    password: str


class SignUp(BaseModel):
    email: EmailStr
    password: str
