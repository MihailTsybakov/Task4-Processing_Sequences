Max_len = 0
name_of_file = 'C:\\Users\\mihai\\Desktop\\progy\\data.txt'

def Function(name_of_file):
    temp_max = 0
    answer = 0
    file = open(name_of_file, 'r')
    len_of_file = 0
    string = file.read()
    for h in string:
        if (h != ''):
            len_of_file += 1
    file.seek(0)    
    temp_integer = ''
    temp_string = ''
    integer = ''
    flag_2 = 0
    index = 0
    while (flag_2 != 1):
        file.seek(index)
        temp_string = file.read(1)
        if (temp_string == ' '):
            flag_2+=1
        if (temp_string != ' '):
            temp_integer += temp_string
        index += 1
    
    temp_integer = int(temp_integer)
    while (index < len_of_file):
        file.seek(index)
        temp_string = file.read(1)
        if ((temp_string != ' ') and (temp_string != '\n')):
            integer += temp_string
        if ((temp_string ==  ' ') or (temp_string == '\n') or (index == len_of_file - 1)):
            integer = int(integer)
            if (int(integer) == int(temp_integer)):
                temp_max += 1
            if ((int(integer) != int(temp_integer)) or ((int(integer) == int(temp_integer)) and index == len_of_file - 1)):
                if (temp_max > answer):
                    answer = temp_max
                temp_max = 0
            temp_integer = integer
            integer = ''
        index += 1
    return answer

def Autotest():
    Test_length = 0
    test_name = 'C:\\Users\\mihai\\Desktop\\progy\\test.txt'
    Test_length = Function(test_name)
    print("tlen is",Test_length + 1)
    if (Test_length + 1== 3):
        print("Autotest passed successfully")
    else:
        print("Autotest not passed")
    return 0
Autotest()

Max_len = Function(name_of_file)
if (Max_len == 0):
    print("Answer is 0")
else:
    print("Answer is ",Max_len + 1)
                
                
        
        
        
    
    
    
