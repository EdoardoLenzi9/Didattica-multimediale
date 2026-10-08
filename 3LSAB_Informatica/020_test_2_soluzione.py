# 1) Dichiara 5 variabili di tipi diversi (per esempio: numero senza virgola, numero con la virgola,
#    vero/falso, parola, lista di numeri con la virgola) e assegna loro un valore a piacere

v1: int = 42
v2: float = 3.1415
v3: bool = False
v4: str = """Nel mezzo del cammin di nostra vita..."""
v5: list[float] = [1.0, 1.2, 1.1, 42.3]

# 2) stampa il risultato di: 1 - 4, tre alla quinta, il resto di 7 : 4, 5 : 2 (come valore intero)
print(1 - 4)
print(3 ** 5)
print(7 % 4)
print(5 // 2)

# 3) predici il valore stampato
w: int = (((5 + 1) // 3 + (3 - 1) * 1) ** 2) % 10
w: int = ((6 // 3 + 2 * 1) ** 2) % 10
w: int = ((3 // 3 + 2) ** 2) % 10
w: int = ((2 + 2) ** 2) % 10
w: int = ((4) ** 2) % 10
w: int = 16 % 10
w: int = 6
print(w)

# 4) scrivi la tabella di verita' di not(b or a)
"""
not(True or True) = False
not(True or False) = False
not(False or True) = False
not(False or False) = True
"""

# 5) dichiara due variabili con i valori "hello" e " world!"; concatenale e stampa:
#       - i primi 5 caratteri
#       - gli ultimi 6 caratteri
#       - l'ultimo carattere
#       - il secondo, terzo e quarto carattere

s1: str = "hello"
s2: str = " world!"
s3: str = s1 + s2
print(s3[ :6])
print(s3[-6: ])
print(s3[-1])
print(s3[1:4])

# 6) dichiara una variabile con valore "3.1415", trasformala in un numero con la virgola 
#    e salva questo valore in una nuova variabile val. Stampa il tipo di val e il valore 
#    di val incrementato di `1.0`

str_val: str = "3.1415"
val: float = float(s) 
print(type(val))
print(val + 1.0)

# 7) scrivi un cast che non mandi python in errore

float(int(bool(str(True))))

# 8) dichiara una variabile di tipo lista di numero intero con i seguenti valori: 1, 3, 42, 99, 100
lista: list[int] = [1, 3, 42, 99, 100]

# 9) dichiara una funzione `"foo"` che prende in input un numero intero (l'eta' di una persona).
# La funzione deve ritornare in output "maggiorenne" o "minorenne" a seconda dell'eta' passata
# in input

def foo(eta: int) -> str:
    output: str = "minorenne"
    if eta >= 18:
        output = "maggiorenne"
    return output
