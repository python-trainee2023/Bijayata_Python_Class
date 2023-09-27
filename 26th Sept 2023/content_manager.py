from platform import node


class FileManager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.node = mode

    def __enter__(self):
        self.file = open(self.filename, self.node)
        return self.file

    def __exit__(self,exc_type, exc_value, exc_traceback):
        self.file.close()

with open("student.txt", "w") as f:
    f.write("This is a test file")

print(f.closed)