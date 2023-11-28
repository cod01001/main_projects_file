def get_dividers(values, powers):
    x = 0
    result = 1
    for i in values:
        result *= i ** powers[x]
        x += 1

    y = []
    o = 0
    while o <= result:
        o += 1
        if result % o == 0:
            y.append(o)
        else:
            continue
    print(y)




get_dividers([2, 5, 11], [2, 1, 1])

