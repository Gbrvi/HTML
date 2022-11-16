for c in range(1, 11):
    c = int(input(f"Digite o {c} valor: "))

    if c > 0:
        print("Positivo")
    if c < 0:
        print("Negativo")
    if c == 0:
        print("Nulo")