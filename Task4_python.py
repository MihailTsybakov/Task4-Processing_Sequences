name_of_file = 'C:\\Users\\mihai\\Desktop\\progy\\data.txt'
len_of_sequence = 0

def Sequence(filename):
    file = open(filename, 'r')
    max_len = 0
    temp_max = 0
    for line in file:
        length = len(line)
        prev_integer = ''
        index = 0
        flag = 0
        while (flag != 1):
            if (line[index] != ' '):
                prev_integer += line[index]
            if (line[index] == ' ') or (index == (length -1)):
                flag += 1
            index += 1
        prev_integer = int(prev_integer)
        integer = ''
        for i in range(index,length):
            if (line[i] != ' '):
                integer += line[i]
            if ((line[i] == ' ') or (i == (length - 1))):
                integer = int(integer)
                if (int(integer) == int(prev_integer)):
                    temp_max += 1
                if ((int(integer) != int(prev_integer)) or ((int(integer) == int(prev_integer)) and i == length - 1)):
                    if (temp_max > max_len):
                        max_len = temp_max
                    temp_max = 0                
                prev_integer = integer
                integer = ''
    return max_len

def Autotest():
    test_file = 'C:\\Users\\mihai\\Desktop\\progy\\test.txt'
    Test_length = Sequence(test_file)
    if ((Test_length+1) == 3):
        print("Autotest passed successfully")
    else:
        print("Autotest not passed")
Autotest()
len_of_sequence = Sequence(name_of_file)

if (len_of_sequence == 0):
    print("maximum length is 1")
else:
    print("Maximum length is", len_of_sequence + 1)
            
            
            
            
        