

def minimum_even_one_to_twenty()->int:
    starter = 1
    evenly_dividable = True
    while(starter < 9999999999999):
        for y in range(20):
            if y < 1:
                y = 1
            if starter % y != 0:
                evenly_dividable = False
        if evenly_dividable:
            return starter
        starter += 1
        evenly_dividable = True
    return 0

print(minimum_even_one_to_twenty())