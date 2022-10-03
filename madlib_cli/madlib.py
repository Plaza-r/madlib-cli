def welcome():

    print('''
        Welcome to my first MadLib Game! 
        A Madlib is a pre-generated story for you to enter your own words into. 
        It's a fun way to pass the time.
    ''')


welcome()


def read_template(path):

    try:
        with open(path, "r") as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(template):

    stripped = ""
    parts = []
    capture = False
    current_part = ""

    for character in template:
        if character == "{":
            stripped += character
            capture = True
            current_part = ""
        elif character == "}":
            stripped += character
            capture = False
            parts.append(current_part)
        elif capture:
            current_part += character
        else:
            stripped += character

    return stripped,tuple(parts)


def merge(template, tple):

    return template.format(*tple)