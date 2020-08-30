# This challenge is to convert Employee Salary calculation which was using filter, reduce, map functionality
# into program using list comprehension

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


# Developer Average Salary

developer_salaries = [emp["salary"]
                      for emp in employees if emp["job_title"] == "developer"]

average_developer_salary = sum(
    developer_salaries) / len(developer_salaries)

print(f"Average Developer Salary: {average_developer_salary}")


# Non developer Average Salary
non_developers_salaries = [emp["salary"]
                           for emp in employees if emp["job_title"] != "developer"]

average_non_developers_salary = sum(
    non_developers_salaries) / len(non_developers_salaries)

print(f"Average Non Developer Salary: {average_non_developers_salary}")
