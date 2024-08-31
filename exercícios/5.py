def inverte_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

# Exemplo de uso
string = "Exemplo"
print(f"String original: {string}")
print(f"String invertida: {inverte_string(string)}")