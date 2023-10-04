# Password Generator Project
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*./;,_-"

collected = lower + upper + numbers + symbols
length = int(input("How long do you want the password to be? "))
password = "".join(random.sample(collected, length))
print(password)
