import pytest
from employee import Employee


def test_give_default_raise():
    some_employee = Employee('John', 'Smith', 10_000)
    some_employee.give_raise()
    assert some_employee.annual_salary == 60_000


def test_give_custom_raise():
    some_employee = Employee('John', 'Smith', 10_000)
    some_employee.give_raise(annual_raise=35_000)
    assert some_employee.annual_salary == 45_000
