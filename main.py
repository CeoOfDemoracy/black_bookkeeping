from person.model.person import Person, FamilyStatus
from person.hr_manager.hr_manager import HRManager

def main():
    hr = HRManager()
    victor = Person(name="Victor", age=17, family_status=FamilyStatus.SINGLE)

    hr.hire_employee(Person(name="Evan", age=25, family_status=FamilyStatus.MARRIED, wanted_salary=3000))
    hr.hire_employee(victor)

    hr2 = HRManager(is_illegal=True)
    hr2.hire_employee(victor)

    print("HR:", hr.list_employees())
    print("ILLEGAL HR:", hr2.list_employees())

if __name__ == "__main__":
    main()
