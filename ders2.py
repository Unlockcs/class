import random
char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght = int(input("uzunluk girin"))
password =""
for i in range(lenght):
    password += random.choice(char)

print(password)
