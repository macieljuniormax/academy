animais = ["Gato", "Cachorro", "Elefante"]
print(animais)

animais.append("Galinha")  # Insere no final da lista
print(animais)

animais.insert(2, "Porco")  # Insere no índice definido no primeiro parâmetro
print(animais)

animais.pop(0)  # Remove o item de acordo com a posição definida
print(animais)

animais.remove("Porco")  # Remove pelo valor do item
print(animais)
