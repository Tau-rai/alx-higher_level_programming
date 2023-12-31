#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for k in range(list_length):
        result = 0
        try:
            result = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("{}".format("wrong type"))
        except ZeroDivisionError:
            print("{}".format("division by 0"))
        except IndexError:
            print("{}".format("out of range"))
        finally:
            new_list.append(result)
    return new_list
