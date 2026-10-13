def statistik(data):
    total = 0
    minimum = data[0]
    maksimum = data[0]
    
    for x in data:
        total += x
        if x < minimum:
            minimum = x
        if x > maksimum:
            maksimum = x
            
    rata = total / len(data)
    return minimum, maksimum, rata

# Memanggil fungsi dan melakukan unpacking nilai
mn, mx, rt = statistik([70, 80, 65, 90, 75])
print(f"Minimum: {mn}, Maksimum: {mx}, Rata-rata: {rt}")