import random
import string

class joker:

    def gerar_joker():
        pattern = ''
        for i in range(0,3):
            letter = random.choice(string.ascii_letters)
            pattern += letter
        n = random.randint(10000,99999)
        joker_n = pattern.upper()
        return joker_n + ' ' + str(n)


def generate_numbers():
    numbers = []
    cont = 0
    while (cont != 5):
        n = random.randint(1,50)
        if n in numbers:
            pass
        else:
            numbers.append(n)
            cont += 1           
    return numbers

def generate_stars():
    stars = []
    cont = 0
    while (cont != 2):
        n = random.randint(1,12)
        if n in stars:
            pass
        else:
            stars.append(n)
            cont += 1           
    return stars

def user_numbers():
    numbers_user = []
    cont = 0
    while (cont != 5):
        n = int(input(f"Insert the {cont+1} number:"))
        if n in numbers_user or n < 1 or n > 50:
            pass
        else:
            numbers_user.append(n)
            cont += 1           
    return numbers_user

def user_stars():
    stars_user = []
    cont = 0
    while (cont != 2):
        n = int(input(f"Insert the {cont+1} star:"))
        if n in stars_user or n < 1 or n > 12:
            pass
        else:
            stars_user.append(n)
            cont += 1           
    return stars_user

def verify_numbers(n_key, n_user):
    scored_numbers = 0
    for i in range(0,5):
        for j in range(0,5):
            if n_user[i] == n_key[j]:
                scored_numbers += 1
    return scored_numbers

def verify_stars(s_key, s_user):
    scored_stars = 0
    for i in range(0,2):
        for j in range(0,2):
            if s_user[i] == s_key[j]:
                scored_stars += 1
    return scored_stars


if __name__ == "__main__":

    key_numbers = generate_numbers()
    print(key_numbers)
    key_stars = generate_stars()
    print(key_stars)
    numbers_input = user_numbers()
    stars_input = user_stars()    

    scored_numbers = verify_numbers(key_numbers, numbers_input)
    scored_stars = verify_stars(key_stars, stars_input)

    print(f'You scored {scored_numbers} numbers and {scored_stars} stars')





