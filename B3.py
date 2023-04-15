NumeroACL = int(input("Cual es el número IPV4 ACL? "))
if NumeroACL >= 1 and NumeroACL <= 99:
    print("Este es un ACL IPv4 estándar.")
elif NumeroACL >=100 and NumeroACL <= 199:
    print("Este es una ACL IPv4 extendida")
else:
    print("Esta ACL IPv4 no es extendida o estandar .")

print("Mi ip es 10.155.40.102.")
