# input 
print("----------------------------------------------------------")
h = float(input("Ingrese la altura inicial de la pelota en (m): "))
print("----------------------------------------------------------")

# processing
q = h / 5
n = 0

while h > q:
    h = 0.9*h
    n = n + 1

    # output
    print(f"La pelota a dado un total de {n} rebote antes de llegar a la quinta parte de su altura inicial")
