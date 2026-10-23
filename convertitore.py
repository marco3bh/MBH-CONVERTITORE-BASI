"""Convertitore interattivo di numeri interi tra quattro basi."""


BASI = {
    "1": ("Decimale", 10),
    "2": ("Binario", 2),
    "3": ("Ottale", 8),
    "4": ("Esadecimale", 16),
}


def main():
    print("=== CONVERTITORE DI NUMERI INTERI ===")

    while True:
        print("\nSeleziona la base del numero da inserire:")
        for scelta, (nome, _) in BASI.items():
            print(f"{scelta}. {nome}")
        print("0. Esci")

        scelta = input("\nLa tua scelta: ").strip()
        if scelta == "0":
            print("Arrivederci!")
            return
        if scelta not in BASI:
            print("Scelta non valida. Inserisci un numero da 0 a 4.")
            continue

        nome, base = BASI[scelta]
        while True:
            testo = input(f"Inserisci il numero in {nome.lower()}: ").strip()
            try:
                numero = int(testo, base)
                risultati = (
                    ("Decimale", str(numero)),
                    ("Binario", format(numero, "b")),
                    ("Ottale", format(numero, "o")),
                    ("Esadecimale", format(numero, "X")),
                )
            except ValueError:
                print(
                    f"Numero non valido per la base {base}, oppure troppo lungo. "
                    "Riprova con un numero intero."
                )
                continue
            break

        print("\n--- RISULTATI ---")
        for etichetta, valore in risultati:
            print(f"{etichetta:<12}: {valore}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nArrivederci!")
