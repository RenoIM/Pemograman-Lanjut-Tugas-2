n = -1
while (n < 1) or (n > 20):
    n = int(input("Masukan Nilai Non negatif (1 - 20): "))
    if (n < 1) or (n > 20):
        print("Nilai harus sekitaran dari 1 - 20")

n = n + 1
i = 0
t = 0
print()
for i in range (0, n, 1):
    t = i * i
    print(t)
    i = i + 1

    
    