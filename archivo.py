with open("/Users/normando/3A-IAM-2026/mi_texto.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
print(contenido)

with open("/Users/normando/3A-IAM-2026/mi_texto.txt", "w", encoding="utf-8") as f:
    f.write("Los tacos estaban ricos\nLa fila es muy larga")

with open("/Users/normando/3A-IAM-2026/mi_texto.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
print(contenido)