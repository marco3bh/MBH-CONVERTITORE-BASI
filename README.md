# Convertitore di numeri in Python

Un programma da terminale che converte numeri interi tra **decimale, binario, ottale ed esadecimale**.

## Requisiti

- Python 3 installato.
- Nessuna libreria aggiuntiva.

## Avvio

Apri il terminale nella cartella del progetto ed esegui:

```bash
python convertitore.py
```

## Come si usa

Scegli la base del numero che vuoi inserire usando il menu:

```text
1. Decimale
2. Binario
3. Ottale
4. Esadecimale
0. Esci
```

Inserisci il numero: il programma mostrerà la conversione in tutte e quattro le basi. Al termine tornerà al menu per una nuova conversione.

Per chiudere, scegli `0` nel menu.

## Esempio

Scegliendo `1. Decimale` e inserendo `42`, ottieni:

```text
Decimale    : 42
Binario     : 101010
Ottale      : 52
Esadecimale : 2A
```

## Numeri supportati

- Numeri interi positivi, negativi e zero.
- Lettere maiuscole o minuscole per l’esadecimale.
- Prefissi `0b`, `0o` e `0x`, selezionando la base corrispondente.

I numeri con la virgola non sono supportati. Se inserisci una scelta o un numero non valido, il programma ti chiederà di riprovare.

I numeri negativi vengono visualizzati con il segno meno in tutte le basi.

## Come funziona il codice

Il programma utilizza le funzioni integrate di Python:

- `int(testo, base)` interpreta il numero nella base scelta.
- `str(numero)` produce la rappresentazione decimale.
- `format(numero, "b")` produce la rappresentazione binaria.
- `format(numero, "o")` produce la rappresentazione ottale.
- `format(numero, "X")` produce la rappresentazione esadecimale con lettere maiuscole.

Python esegue internamente i calcoli necessari alle conversioni.
