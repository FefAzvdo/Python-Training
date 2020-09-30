from time import sleep

print("Contagem regressiva de 10 segundos: ")

for c in range(10, 0, -1):
    print(c)
    sleep(1.0)

print("FIM !")
