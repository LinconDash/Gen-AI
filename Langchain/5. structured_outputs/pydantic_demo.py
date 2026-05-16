from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Person(BaseModel):
    name : str = "xyz"
    age : Optional[int] = None
    email : Optional[EmailStr] = None        # email validation
    cgpa : Optional[float] = Field(gt=0, lt=10, default=5, description="A decimal value which should be greater than 0 and less than 10")

new_person_a = {"name": "Lincon", "age": 25}
lincon = Person(**new_person_a)

print(lincon)
print(type(lincon))

new_person_b = {"name": "Linx", "age": "25"}  # Pydantic will actually convert str to int (type coercing)
linx = Person(**new_person_b)

print(linx)


new_person_c = {"name": "Linx", "age": "25", "email": "linx@email.com"} 
linx = Person(**new_person_c)
print(linx)
print(linx.model_dump_json())