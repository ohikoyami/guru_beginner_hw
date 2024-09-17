import dataclasses


@dataclasses.dataclass
class Student:
    name: str
    lastname: str
    email: str
    phone: str
    subject1: str
    addr: str
    city: str
    state: str
    gender: str
    bday_day: int
    bday_month: int
    bday_year: int
    hobbies1: str
    hobbies2: str
    img: str
