from typing import Optional, Dict
from pydantic import Field
from .Base import MongoModel

class Setting(MongoModel):
    version: str = Field(default="1.0.0")
    privacy_policy_document: Optional[str] = Field(None, alias="privacyPolicyDocument")
    about_us_document: Optional[str] = Field(None, alias="aboutUsDocument")
    contact_info: Dict[str, str] = Field(default_factory=dict, alias="contactInfo")