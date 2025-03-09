def cek_angka(a, b, c):
    if a == b or a == c or b == c:
        return False

    if (a + b == c) or (a + c == b) or (b + c == a):
        return True
    else:
        return False

print(cek_angka(3, 5, 8))
print(cek_angka(4, 6, 10))
print(cek_angka(2, 2, 4))
print(cek_angka(1, 2, 4))
