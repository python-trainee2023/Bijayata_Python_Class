class FileNotFountError:
    pass


try:
    source_file = open('teacher.txt', 'r');
    content = source_file.read()

except NameError:
    print("the name hasnt been defined")

    
except FileNotFountError:
    print("the file not present")

finally:


    source_file.close()