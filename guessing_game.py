a = int(input("Choose a natural number:"))
print("Enter any", a - 1, "natural numbers that are less than", a)
print("I will guess the number you missed.")
b = a * (a + 1) / 2
c = 0
for i in range(a - 1):
    c += int(input())
print("The number you missed is", b - c)
