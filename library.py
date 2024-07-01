class Person:
    def _init_(self, lastname='', firstname='', middlename='', departmentnumber='', workingdays='', salary=''):
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.departmentnumber = departmentnumber
        self.workingdays = working_days
        self.salary = salary


def get_person_for_table(self):
    w = []
    w.append(self.last_name)
    w.append(self.first_name)
    w.append(self.middle_name)
    w.append(self.department_number)
    w.append(self.working_days)
    w.append(self.salary)
    return w
    
    '''return [self.last_name, self.first_name, self.middle_name, self.department_number,
            self.working_days, self.salary]'''

def equal_person(self, other):
    return self.last_name == other.last_name and \
           self.first_name == other.first_name and \
           self.middle_name == other.middle_name and \
           self.department_number == other.department_number and \
           self.working_days == other.working_days and \
           self.salary == other.salary

class Group:
    def init(self):
        self.people = {}
        self.count = 0


def append_person(self, data):
    new_person = Person(*data)
    self.people[self.count] = new_person
    self.count += 1

def edit_person(self, index, data):
    updated_person = Person(*data)
    self.people[index] = updated_person

def str_person(self, line):
    parts = line.strip().split("&")
    return Person(*parts)

def read_data_from_file(self, filename):
    self.people = {}
    with open(filename, "r", encoding="utf-8") as file:
        x = 0
        for line in file:
            self.people[x] = self.str_person(line)
            x += 1
            self.count += 1

def find_key_person(self, data):
    search_person = Person(*data)
    for key in self.people:
        if self.people[key].equal_person(search_person):
            return key
    return -1

def del_person(self, data):
    person_to_remove = Person(*data)
    for key in self.people:
        if self.people[key].equal_person(person_to_remove):
            del self.people[key]
            self.count -= 1
            break

def write_data_to_file(self, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for key in self.people:
            person_data = self.people[key].get_person_for_table()
            file.write('&'.join(person_data) + '\\n') 

def get_department_data(self, department_number, output_filename):
    with open(output_filename, 'a', encoding='utf-8') as file:
        for key in self.people:
            if self.people[key].department_number == department_number:
                person_data = self.people[key].get_person_for_table()
                file.write('&'.join(person_data) + '\\n')

def filter_and_sort_by_salary(self, department_number, minimum_salary):
    filtered_list = [self.people[key] for key in self.people if self.people[key].department_number == department_number and int(self.people[key].salary) > minimum_salary]
    sorted_list = sorted(filtered_list, key=lambda x: int(x.salary))
    return sorted_list

def find_average_salary_in_department(self, department_number):
    salaries = [int(self.people[key].salary) for key in self.people if self.people[key].department_number == department_number]
    if salaries:
        return sum(salaries) / len(salaries)
    return 0

def find_min_working_days_employees(self):
    min_working_days = min([int(self.people[key].working_days) for key in self.people])
    employees = [key for key in self.people if int(self.people[key].working_days) == min_working_days]
    return [self.people[key].get_person_for_table() for key in employees]

def find_employee_by_name(self, last_name, first_name, middle_name):
    for key in self.people:
        if self.people[key].last_name == last_name and self.people[key].first_name == first_name and self.people[key].middle_name == middle_name:
            return self.people[key].get_person_for_table()
    return None

def set_salary_for_employee(self, last_name, first_name, middle_name, new_salary):
    for key in self.people:
        if self.people[key].last_name == last_name and self.people[key].first_name == first_name and self.people[key].middle_name == middle_name:
            self.people[key].salary = new_salary
            break

def get_number_of_employees(self):
    return len(self.people)
