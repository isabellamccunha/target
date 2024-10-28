def contar_a(string):
    return string.lower().count('a')

texto = input("Informe uma string: ")
print(f"A letra 'a' aparece {contar_a(texto)} vezes.")
