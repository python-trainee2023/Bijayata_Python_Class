with open('student.txt', 'r') as source_file, open('upper_case_student.txt', 'w') as target_file:
    for line in source_file:
        uppercase_line = line.upper()
        target_file.write(uppercase_line)

print("File copied successfully.")
print(source_file.closed)