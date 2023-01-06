

def is_palindrome(number: int)->bool:
    int_list = list(map(int, str(number)))
    is_solved = False
    list_index = 0
    if len(int_list) % 2 != 0:
        del int_list[round(len(int_list) / 2 - 1)]

    while is_solved == False:
        if int_list[list_index] != int_list[len(int_list -list_index)]:
            return False
        if list_index > len(int_list) / 2:
            break
        list_index += 1
    return True

    # for y in int_list:
    #     if y != int_list[len(int_list)-y]:
    #         return False
    #     if y >= len(int_list/2):
    #         break
    # return True


print(is_palindrome(60001))

