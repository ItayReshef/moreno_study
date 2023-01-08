



def thousand_pythagoras()->int:
    first_num_index = 1
    second_num_index = 1
    counter_index = 1
    multiplier_tester = 10000
    while True:
        while second_num_index < multiplier_tester:
            while first_num_index < multiplier_tester:
                tester = (first_num_index + second_num_index ) * 2
                if (first_num_index + second_num_index ) * 2 == 1000:
                    return (first_num_index + second_num_index) * 2
                first_num_index += 1
            first_num_index -= multiplier_tester - counter_index
            second_num_index += 1
            counter_index += 1
    return 0


print(thousand_pythagoras())
