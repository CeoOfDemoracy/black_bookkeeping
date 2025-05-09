from person.hr_manager.i_hr_manager import IHRManager
from person.model.interview_result import HiringResult, FiringResult
from typing import List, Optional
from person.model.person import Person

class HRManager(IHRManager):
    def __init__(self, is_illegal: bool = False):
        self.is_illegal = is_illegal
        self.employees: List[Person] = []
        self.median_salary: Optional[float] = None

    def hire_employee(self, person: Person) -> HiringResult:
        if person.age < 18 and not self.is_illegal: return HiringResult.NOT_HIRED
        self.employees.append(person)
        return HiringResult.HIRED

    def fire_employee(self, index: int) -> FiringResult:
        if index < 0 or index >= len(self.employees): return FiringResult.NOT_FIRED
        del self.employees[index]
        return FiringResult.FIRED

    def list_employees(self) -> List[Person]: return self.employees
