my_file = open('nearby.txt', 'r')
content = my_file.read()
my_file.close()

content = content.split('\n')
total_score = len(content)

score = 0
for cont in content:
    cont = cont.split('=')
    print(cont[0])
    user_input = input("Please enter the Answer here -")
    if user_input == cont[1]:
        score = score + 1

string = f'Your score is {score}/{total_score}'
result = open('result.txt', 'w')
result.write(string)
result.close()