def dias(kellyDiario, samDiario, diferencia):
    if kellyDiario <= samDiario:
        return print("-1")
    samResolvio = diferencia
    kellyResolvio = 0
    dias = 0

    while kellyResolvio <= samResolvio:
        samResolvio += samDiario
        kellyResolvio += kellyDiario
        dias += 1

    print(f"Kelly puede alcanzar a Sam en {dias} dias.")


sam = int(input("Ingresa los retos diarios que resuelve Sam: "))
kelly = int(input("Ingresa los retos diarios que resuelve Kelly: "))
diferencia = int(input("Ingresa la cantidad de retos que ha resuelto Sam: "))
dias(kelly, sam, diferencia)