with open('myfile.py') as file:
    print(file.read())
    file.close()

with open('myfile.py') as file:
    exec (file.read())
    file.close()

