#Este codigo esconde el numero de cuenta con expresiones regulares y pide la contraseña
import re
text="Este es tu numero de cuenta: 1234-5678-9012-3456"
pattern=r"\d{4}-\d{4}-\d{4}-\d{4}"
text_remplazo="Numero Oculto"
remplazo=re.sub(pattern, text_remplazo, text)
print(remplazo)
print("Para verlo debes ingresar la contraseña")
password="Tu$ ti0ss"
for i in range(3):
    passs=input("Ingrese la contraseña: ")
    if passs==password:
        print(text)
        break
    else:
        print("Intentalo otra vez")
if passs!=password:
    print("Maximos de intentos!!!")
