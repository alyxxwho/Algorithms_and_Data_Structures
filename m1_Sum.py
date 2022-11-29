import fileinput

sum_line = ''
sum_int = 0
flag = False
for input_line in fileinput.input():
    for literal in range(len(input_line) - 1):
        if input_line[literal].isdigit():
            sum_line += input_line[literal]
        elif input_line[literal] == '-' and input_line[literal + 1].isdigit():
            flag = True
        else:
            continue
        if not input_line[literal + 1].isdigit():
            if flag:
                sum_int -= int(sum_line)
                flag = False
            else:
                sum_int += int(sum_line)
            sum_line = ''
            literal += 1

print(sum_int)
