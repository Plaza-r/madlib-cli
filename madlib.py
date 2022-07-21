print("It is time for Madlib")

def read_template (path):
    file = open(path, "r")
    read = file.read()
    file.close()
    return read.strip()

