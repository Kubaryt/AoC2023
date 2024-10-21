def find_first_number(string):
    for char in string:
        try:
            int(char)
        except ValueError:
            continue
        return char


current_line_code = ''

code_sum = 0

with open('input') as file:
    for line in file:
        current_line_code = ""
        current_line_code += find_first_number(line)
        current_line_code += find_first_number(reversed(line))

        current_line_code = int(current_line_code)
        code_sum += current_line_code


print(code_sum)
