


def to_base_10(base, any_base_number):
    if len(any_base_number) > 1:
        latex_string = ""
        left_length = len(any_base_number[0]) - 1
        right_length = len(any_base_number[1])
        right_offset = right_length + 1

        for char in any_base_number[0]:
            latex_string += f"({char} \\times {base}^{left_length})+"
            left_length -= 1
        for char in any_base_number[1]:
            latex_string += f"({char} \\times {base}^{ {right_length - right_offset} })+"
            right_length -= 1
        print(latex_string.rstrip("+").replace("\n", ""))
    else :
        latex_string = ""
        left_length = len(any_base_number[0]) - 1


        for char in any_base_number[0]:
            latex_string += f"({char} \\times {base}^{left_length})+"
            left_length -= 1

        print(latex_string.rstrip("+").replace("\n", ""))
