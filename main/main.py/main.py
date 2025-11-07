# 1-misol
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

son = int(input("Son kiriting: "))
print("Faktorial:", factorial(son))

# 2-misol
def palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

matn = input("Matn kiriting: ")
print("Palindrommi?", palindrome(matn))


# 3-misol
def katta_kichik(royxat):
    return max(royxat), min(royxat)

r = list(map(int, input("Raqamlarni kiriting (bo‘sh joy bilan): ").split()))
katta, kichik = katta_kichik(r)
print(f"Eng katta: {katta}, Eng kichik: {kichik}")


# 4-misol
def unli_harflar_soni(s):
    unlilar = "aeiouAEIOUаоэеиыуёюяАОЭЕИЫУЁЮЯ"
    return sum(1 for i in s if i in unlilar)

matn = input("Satr kiriting: ")
print("Unli harflar soni:", unli_harflar_soni(matn))


# 5-misol
def tubmi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

son = int(input("Son kiriting: "))
print("Tub sonmi?", tubmi(son))
