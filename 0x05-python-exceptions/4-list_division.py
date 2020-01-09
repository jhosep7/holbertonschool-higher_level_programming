#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    Arr = []
    while i < list_length:
        ans = 0
        try:
            ans = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            Arr.append(ans)
            i += 1
    return Arr
