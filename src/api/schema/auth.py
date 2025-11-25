from pydantic import BaseModel, EmailStr, Field

class LoginSchema(BaseModel):
    email: EmailStr = Field(..., description="Email válido do usuário")
    password: str = Field(..., min_length=1, description="Senha do usuário")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    username: str
    role: str