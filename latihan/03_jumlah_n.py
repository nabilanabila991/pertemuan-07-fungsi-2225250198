def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Menguji nilai n = 1, 5, 10, dan 100
test_values = [1, 5, 10, 100]

print("n | Hasil Fungsi | Hasil Rumus n(n+1)/2")
print("-" * 38)
for n in test_values:
    hasil_fungsi = jumlah_n(n)
    hasil_rumus = n * (n + 1) // 2
    print(f"{n:<2} | {hasil_fungsi:<12} | {hasil_rumus}")