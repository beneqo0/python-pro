import random
znaki="!@#$%^&*POIUYTREWQASDFGHJKLMNBVCXZqwertyuioplkjhgfdsazxcvbnm1234567890"
a=int(input("wybierz dlugość hasła (napisz ilość znaków np. 10):  "))
haslo=""
for i in range(a):
    c=random.choice(znaki)
    haslo=haslo+c
print(haslo)
