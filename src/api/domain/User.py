from typing import Optional, Any, Dict
from pydantic import Field, EmailStr
from .Base import MongoModel 
from .Base import UserRole  

class Usuario(MongoModel):
    username: str = Field(..., max_length=50)
    email: EmailStr
    password: str
    name: str = Field(..., max_length=100)
    role: UserRole = Field(default=UserRole.USER)
    avatar_url: Optional[str] = Field(None, alias="avatarUrl")
    instituicao: Dict[str, Any] = Field(default_factory=dict)
    terms_accepted: bool = Field(..., alias="termsAccepted")
    profile_data: Dict[str, Any] = Field(default_factory=dict, alias="profileData")