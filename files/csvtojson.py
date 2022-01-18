import json

csv_file = open('ser.csv', 'r')
content = csv_file.read()
content = content.split('\n')
content = content[1:-1]

dict_item = []
for cont in content:
    cont = cont.removeprefix('"').removesuffix('"')
    cont = cont.split('","')
    new_dict = {'name': cont[0], 'type': cont[2], 'status': cont[1]}
    dict_item.append(new_dict)

print(dict_item)

new_json = open('json_file.txt', 'w')
json.dump(dict_item, new_json)
new_json.close()