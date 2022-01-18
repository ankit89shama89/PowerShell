import json

### open and close file
with open('ser.csv', 'r') as file:
    content = file.read()


content = content.split('\n')
content = content[1:-1]

dict_item = []
for cont in content:
    cont = cont.removeprefix('"').removesuffix('"')
    cont = cont.split('","')
    new_dict = {'name': cont[0], 'type': cont[2], 'status': cont[1]}
    dict_item.append(new_dict)

print(dict_item)


with open('json_file.txt', 'w') as new_json:
    json.dump(dict_item, new_json)
