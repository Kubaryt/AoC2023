text_to_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def parse_text(string):
    result = ''
    remaining_text = string

    while remaining_text:
        for text, digit in text_to_digits.items():
            if remaining_text.startswith(text) or remaining_text.startswith(digit):
                result += digit
                break

        remaining_text =  remaining_text[1:]

    return result

code_sum = 0


with open('input') as file:
    for line in file:
        current_line_code = ''
        result = parse_text(line)
        current_line_code = result[0] + result[-1]
        code_sum += int(current_line_code)

print(code_sum)