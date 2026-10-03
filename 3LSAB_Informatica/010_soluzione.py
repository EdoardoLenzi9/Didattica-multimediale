# 1) dichiara 4 variabili e assegna loro i seguenti valori (True, 3.14, 123, "hi")
v1: bool = True
v2: float = 3.14 
v3: int = 314
v4: str = "hi"

# 2) stampa il risultato di: 1+1, 10:3 intero, resto 5:4, due alla terza
print(1 + 1)
print(10 // 3)
print(5 % 4)
print(2 ** 3)

# 3) w = (((2 + 1) // 3 + (2 - 1) * 1) ** 2) % 10
w = (((3) // 3 + (2 - 1) * 1) ** 2) % 10
w = (((3) // 3 + (1) * 1) ** 2) % 10
w = ((1 + 1 * 1) ** 2) % 10
w = ((1 + 1) ** 2) % 10
w = (2 ** 2) % 10
w = 4 % 10
w = 4

# 4) scrivi la tabella di verita' di not(a and b)
# not(True  and True ) = False
# not(True  and False) = True
# not(False and True ) = True
# not(False and False) = True

# 5) dichiara due variabili con i valori "hello" e " world!" ; concatenale e stampa
v5 = "hello"
v6 = " world!"
v5 = v5 + v6
print(v5[-1])   # stampa l'utlimo carattere
print(v5[-6: ])   # gli ultimi 6 caratteri
print(v5[1:4])   # il secondo, terzo e quarto carattere
print(v5[ :6])   # i primi 5 caratteri

# 6) dichiara una variabile con valore "123", trasformala in un numero intero e
#    salva questo valore in una nuova variabile val. Stampa il tipo di val e il valore di val

v7: str = "123"
val: int = int(v7)
print(type(val))
print(val)


# 7) scrivi un cast che manda python in errore

# x: int = int("ciao")

# 8) dichiara una variabile di tipo lista di bool con i seguenti valori: True, False, True

v8: list[bool] = [True, False, True]

# 9) dichiara una funzione "foo" che prende in input due numeri interi: anno_di_nascita e
#    anno_corrente. La funzione deve calcolare l'eta di una persona sottraendo le due variabili 
#    in input e ritorna in output "maggiorenne", "teenager", "minorenne", "over-50" a seconda 
#    dei casi

def foo(anno_di_nascita: int, anno_corrente: int) -> str:
    eta = anno_corrente - anno_di_nascita
    if 0 <= eta < 10:
        return "minorenne"
    if 10 <= eta < 19:
        return "teenager"
    if 19 <= eta < 50:
        return "maggiorenne"
    return "over-50"

print(foo(2000, 2005))
print(foo(2000, 2015))
print(foo(2000, 2025))
print(foo(2000, 2055))

# 10) scrivi una funzione "fibonacci" che prende in input un numero massimo e stampa la
#     serie di fibonacci fino al numero massimo. La serie di Fibonacci parte da 0, 1 e 
#     il numero successivo e' la somma dei due precedenti

def fibonacci(max: int):
    penultimo: int = 0
    ultimo: int = 1
    output: str = f"{penultimo}, {ultimo}"
    while ultimo < max:
        successivo = penultimo + ultimo
        output = output + f", {successivo}"
        penultimo = ultimo
        ultimo = successivo
    print(output)

fibonacci(100)

# 11) scrivi una funzione "numeri_primi" che prende in input un numero massimo e calcola
#     la serie dei numeri primi fino al numero massimo. Ritorna in output la lista dei numeri primi.
#     Per esempio: 2, 3, 5, 7, 11, 13, ..

def numeri_primi(max: int) -> list[int]:
    if max < 2:
        return []
    output: list[int] = []
    for i in range(2, max + 1):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                # break
        if primo:
            output.append(i)
    return output

print(numeri_primi(1))
print(numeri_primi(2))
print(numeri_primi(100))