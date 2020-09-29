import numpy as np


def arrGen(dim, size):
    lst = []
    for i in range(dim):
        lst.append(size)

    return lst


def arrRandom(dim, size, seed):
    np.random.seed(seed)
    array = np.random.rand(*arrGen(dim, size))
    return array


def userInput():
    while True:
        userDig = input()
        try:
            userDig = int(userDig)
            break
        except ValueError:
            print("Wprowadziłeś nieprawidłowe dane")
            continue
    return userDig


def array():
    print("Wpisz liczbę wymiarów tablicy: ")
    dim = userInput()
    print("Wpisz wielkość wszystkiech wymiarów: ")
    size = userInput()
    print("Wpisz ziarno liczby losowej: ")
    seed = userInput()
    arr = arrRandom(dim, size, seed)
    print(arr)


def main():
    array()


if __name__ == "__main__":
    main()
