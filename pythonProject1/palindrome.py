

def is_palindrome(number: int)->bool:
    int_list = list(map(int, str(number)))
    is_solved = False
    list_index = 0
    first_iteration = 1

    if len(int_list) % 2 != 0:
        del int_list[round(len(int_list) / 2 - 1)]
    if len(int_list) < 3:
        return 0
    while True:
        if int_list[list_index] != int_list[len(int_list) - list_index - 1]:
            return False
        if list_index > len(int_list) / 2:
            break
        list_index += 1
        first_iteration = 0
    return True

def biggest_palindrome()->int:
    multi1 = 999
    multi2 = 999
    second_count_index = 999
    increasing_trductor = 1
    biggest_so_far = 0
    while multi2 > 0:
        while multi1 > 0:
            if multi1 * multi2 > 0:
                if is_palindrome(multi1 * multi2):
                    if multi1 * multi2 > biggest_so_far:
                        biggest_so_far = multi1 * multi2
            multi1 -= 1
        multi1 = second_count_index
        second_count_index -= increasing_trductor
        increasing_trductor += 1
        multi2 -= 1
    return biggest_so_far

print(biggest_palindrome())

