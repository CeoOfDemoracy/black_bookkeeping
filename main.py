from person.model.person import Person, FamilyStatus
from person.hr_manager.hr_manager import HRManager
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def list(hr: HRManager):
    for i,employee in enumerate(hr.list_employees(),1):
        print(f'{i}. {employee.name}, {employee.age}')


def main():
    # hr = HRManager()
    # victor = Person(name="Victor", age=17, family_status=FamilyStatus.SINGLE)

    # hr.hire_employee(Person(name="Evan", age=25, family_status=FamilyStatus.MARRIED, wanted_salary=3000))
    # hr.hire_employee(victor)

    # hr2 = HRManager(is_illegal=True)
    # hr2.hire_employee(victor)

    # print("HR:", hr.list_employees())
    # print("ILLEGAL HR:", hr2.list_employees())
    hr = HRManager(is_illegal=bool(int(input('Is hr illegal?(write: 0 or 1)'))))
    

    
    while True : 
        clear()
        print('''
1.Number of employees
2.Hire the employee
3.Fire the employee
4.Exit
''')
        choice = input()
        clear()
        if choice == '1':
            list(hr)
        elif choice == '2':
            a = hr.hire_employee(Person(
                name=input('Enter your name\n'), 
                age=int(input('Enter your age\n')), 
                family_status=[status for status in FamilyStatus][int(input('print 1 if single or 2 if married\n'))-1], 
                wanted_salary=int(input('What salary do you want(optinal variant)')) if bool(int(input('Write 0 if you dont have and preferences in salary or write 1 if you have'))) else None))
            print(a.value)
        elif choice == '3':
            list(hr)
            number_of_employee = int(input('Which employee do you want to fire?(choose number)\n'))
            hr.fire_employee(number_of_employee-1)
        elif choice == '4':
            return    
        else:
            print('Choose 1, 2, 3 or 4')
        
        input('continue?')
        

if __name__ == "__main__":
    main()
