# ------------------------------------------------------------------------#
#                        CAST - NON TRATTATO NEL LIBRO                    #
# ------------------------------------------------------------------------#

# dichiara una variabile "x" di tipo int valore 1
x: int = 1

# usa il cast per trasformare il valore di x in float, bool e str
f: float = float(x)
b: bool = bool(x)
s: str = str(x)

# stampa il tipo di x, f, b, s usando la funzione type
print(type(x))
print(type(f))
print(type(b))
print(type(s))

# ri-converti f, b, s in int

# il cast e' sempre ammesso? posso convertire "abc" in int? 
