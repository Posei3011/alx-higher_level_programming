#!/usr/bin/python3
def safe_print_list(my_list=None, x=0):
    if my_list is None:
        my_list = []

    printed_elements = 0

    for i in range(x):
        try:
            print(my_list[i], end=' ')
            printed_elements += 1
        except IndexError:
            break  # Exit the loop if an IndexError occurs

    print()  # Print a new line to separate the output
    return printed_elements
