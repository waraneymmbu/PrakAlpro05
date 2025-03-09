def cek_digit_belakang(a, b, c):
    digit_a = a % 10
    digit_b = b % 10
    digit_c = c % 10

    if (digit_a == digit_b) or (digit_a == digit_c) or (digit_b == digit_c):
        return True
    else:
        return False

hasil1 = cek_digit_belakang(145, 5, 100)
hasil2 = cek_digit_belakang(71, 187, 18)
hasil3 = cek_digit_belakang(1024, 14, 94)
print("Output:", hasil1)
print("Output:", hasil2)
print("Output:", hasil3)
