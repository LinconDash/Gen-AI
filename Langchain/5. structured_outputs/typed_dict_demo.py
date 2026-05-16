from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

new_person_a : Person = {"name": "Lincon", "age": 25}
new_person_b : Person = {"name": "Linx", "age": "24"}
new_person_c : Person = {"name": "Linx", "age": "24", "gender": "male"}

print(new_person_a)

# No errors as it doesn't validate at runtime
print(new_person_b)
print(new_person_c)