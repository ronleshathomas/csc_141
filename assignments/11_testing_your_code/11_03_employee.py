class Employee:
    
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount


from employee import Employee

def test_give_default_raise():
    emp = Employee('John', 'Doe', 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000 

def test_give_custom_raise():
    emp = Employee('Jane', 'Smith', 60000)
    emp.give_raise(10000)
    assert emp.annual_salary == 70000 


import pytest
from employee import Employee

def default_employee():
    return Employee('John', 'Doe', 50000)


def custom_employee():
    return Employee('Jane', 'Smith', 60000)

def test_give_default_raise(default_employee):
    default_employee.give_raise()
    assert default_employee.annual_salary == 55000

def test_give_custom_raise(custom_employee):
    custom_employee.give_raise(10000)
    assert custom_employee.annual_salary == 70000
