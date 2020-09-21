#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    passed = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
        except (ValueError, TypeError):
            passed += 1
            pass
        except IndexError:
            return
        count += 1
    print()
    return (count - passed)
