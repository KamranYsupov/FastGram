from pydantic import BaseModel, EmailStr, Field


class UserSchemaMixin(BaseModel):
    username: str = Field(title='Имя пользователя', max_length=50, min_length=8)
    email: EmailStr = Field(title='E-mail')

    
    
