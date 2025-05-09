from abc import ABC, abstractmethod
from typing import List

from person.model.interview_result import HiringResult, FiringResult
from person.model.person import Person

class IHRManager(ABC):
    @abstractmethod
    def hire_employee(self, person: Person) -> HiringResult: pass

    @abstractmethod
    def fire_employee(self, index: int) -> FiringResult: pass

    @abstractmethod
    def list_employees(self) -> List[Person]: pass