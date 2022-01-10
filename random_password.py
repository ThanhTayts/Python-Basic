# Project Random Password Generator

import string
import random

# print(dir(string)) # xem cac ham cua thu vien string
# print(string.digits) # so
# print(string.punctuation) # cac ki tu dac biet
# print(string.ascii_letters) # cac chu cai cua bang ma Ascii

# print(dir(random))

letters = string.ascii_letters
number = string.digits
punctuation = string.punctuation

# Password Generator Function
def password_generator(lenght):
    prinable = f"{letters}{number}{punctuation}"
    prinable = list(prinable)
    random.shuffle(prinable)
    random_password = random.choices(prinable,k=lenght)
    random_password = ''.join(random_password)

    return random_password

# Get Password Lenght
def get_password_lenght():
    lenght = input(" How lenght do you want for the password :")
    lenght = int(lenght)
    return lenght

# Main Function
def main():
    lenght = get_password_lenght()
    password = password_generator(lenght)
    print(password)

if __name__ == "__main__":
    main()