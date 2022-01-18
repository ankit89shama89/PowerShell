csv_file = open('ser.csv', 'r')
content = csv_file.read()
content = content.removeprefix('"').split('\n')
content = content[1:]

for cont in content:
    if cont != "":
        cont = cont.removeprefix('"').removesuffix('"')
        cont = cont.split('","')
        name = cont[0]
        status = cont[1]
        type = cont[2]
        print(f'Service {name} with type {type} is at {status}')





