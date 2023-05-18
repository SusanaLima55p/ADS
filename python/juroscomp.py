def main():
    principal = 90000
    taxa = 0.01
    meses = 120
    montante = principal * ((1 + taxa)**meses)
    print(montante)

main()