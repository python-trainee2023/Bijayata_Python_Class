#file handling
emp_file = open("employee.txt","r")
print(emp_file.read(3))
print(emp_file.read(3))

for emp in emp_file.readlines():
    print(emp);

emp_file.close()