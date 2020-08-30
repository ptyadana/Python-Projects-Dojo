from functools import reduce

employees = [{
    'name': 'Jane',
    'salary': 90000,
    'job_title': 'developer'
}, {
    'name': 'Bill',
    'salary': 50000,
    'job_title': 'writer'
}, {
    'name': 'Kathy',
    'salary': 120000,
    'job_title': 'executive'
}, {
    'name': 'Anna',
    'salary': 100000,
    'job_title': 'developer'
}, {
    'name': 'Dennis',
    'salary': 95000,
    'job_title': 'developer'
}, {
    'name': 'Albert',
    'salary': 70000,
    'job_title': 'marketing specialist'
}]


# get the average salary of developer
def is_developer(employee):
    return employee["job_title"] == "developer"


def is_non_developer(employee):
    return employee["job_title"] != "developer"


def get_salary(employee):
    return employee["salary"]


def get_sum(acc, x):
    return acc + x


# developer Average Salary
developer_salaries = [get_salary(emp)
                      for emp in employees if is_developer(emp)]

total_developer_salary = reduce(get_sum, developer_salaries)
average_developer_salary = total_developer_salary / len(developer_salaries)

print(f"Average Developer Salary: {average_developer_salary}")


# Non developer Average Salary

non_developers_salaries = [get_salary(emp)
                           for emp in employees if is_non_developer(emp)]

total_non_developers_salary = reduce(get_sum, non_developers_salaries)
average_non_developers_salary = total_non_developers_salary / \
    len(non_developers_salaries)

print(f"Average Non Developer Salary: {average_non_developers_salary}")
