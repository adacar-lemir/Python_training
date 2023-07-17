from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User Model
class User(BaseModel):
    id:int
    name:str
    lastname:str
    address:Optional[str]
    phone:int
    createdDate:datetime = datetime.now()
