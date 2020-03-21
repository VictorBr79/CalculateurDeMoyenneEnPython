def main():
    note1 = int(input("Entrer la première note : "))
    note2 = int(input("Entrer la deuxième note : "))
    note3 = int(input("Entrer la troisième note : "))
    result = (note1 + note2 + note3) / 3
    if result < 5:
        print("Tu peux faire mieux!")
    elif result > 5:
        print("Bravo, continue comme ça!")
    else:
        print("Pille la moitié!")
    print("Votre moyenne est de : " + str(result) + "!")
    avis = input("Etes vous satisfait de mon programme? : ")


if __name__ == '__main__':
    main()
