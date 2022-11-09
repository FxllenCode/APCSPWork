def test_calc(*grades):
    total = 0

    for grade in grades:
        total += grade

    final = total / (len(grades))
    print(final)
        
test_calc(1, 4, 5, 6, 1, 3, 4, 9, 3, 3, 1, 3, 4)