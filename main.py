def two_dimensional_array():
    input1 = map(int, input(
        'Enter 2 numbers separated by a comma, to display a two-dimensional array: ').split(','))
    input2 = map(int, input('Enter 2 more numbers: ').split(','))
    input3 = map(int, input('More: ').split(','))
    input4 = map(int, input('Last time: ').split(','))

    received_data = [input1, input2, input3, input4]

    for input_data in received_data:
        x, y = input_data
        inter_list = [i for i in range(1, (x * y)+1)]
        output_list = []
        helper_variable = y
        for i in range(x):
            output_list.append(inter_list[helper_variable - y:helper_variable])
            helper_variable += y
        print(output_list)
    return None


if __name__ == "__main__":
    two_dimensional_array()
