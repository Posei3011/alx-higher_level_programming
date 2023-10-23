#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        for item in my_list:
            if printed_integers == x:
                break  # Stop when 'x' integers have been printed

            try:
                formatted_item = "{:d}".format(int(item))
                print(formatted_item, end=' ')
                printed_integers += 1
            except (ValueError, TypeError):
                continue  # Skip non-integer values
        print()  # Print a new line to separate the output
    except IndexError:
        pass  # Handle the case when 'x' is greater than the list length

    return printed_integers

if __name__ == "__main__":
