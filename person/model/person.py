from enum import Enum
from typing import Optional

class FamilyStatus(Enum):
    SINGLE = 'Single'
    MARRIED = 'Married'

class Person:
    def __init__(self, name: str, age: int, family_status: FamilyStatus, wanted_salary: Optional[int] = None):
        self.name = name
        self.age = age
        self.family_status = family_status
        self.wanted_salary = wanted_salary

    def __repr__(self) -> str:
        return f'<{self.name}, {self.age} y.o., {self.family_status.value}. {("Wanted salary: " + str(self.wanted_salary)) if self.wanted_salary else ""}>'
