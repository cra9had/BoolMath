def pretty_print(number, length):
    number = str(number)[2:]
    length_delta = len(number) - length
    # print("-"*30)
    # print(length_delta)
    if length_delta < 0:
        for _ in range(-length_delta):
            number = "0" + number
    elif length_delta > 0: 
        print(number, length_delta)
        number = number[:-length_delta]
    return number



result = 0
for i in range(8):
    # print(bin(i))
    num = pretty_print(bin(i), 3)
    print(num)
