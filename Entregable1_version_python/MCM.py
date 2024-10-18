num1=int(input("Ingrese el primer numero"))
num2=int(input("Ingrese el segundo numero"))
i=2
while True:
    if i%num1==0 and i%num2==0:
        mcm=i
        break
    i+=1
print("El MCM es:",mcm)
"""Como generalidad, me parece mas sencillo el ejercicio aqui que en pseint,
el modelo es muy intuitivo pero no por eso menos complejo"""