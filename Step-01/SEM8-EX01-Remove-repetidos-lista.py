#Removendo repetidos
def remove_repetidos(lista):
    s_repetidos = []
    for obj in lista:
        if obj not in s_repetidos:
            s_repetidos.append(obj)
    return sorted(s_repetidos)


'''para cada elemento da lista, se ele for igual a seu anterior, removê-lo
a = [2 3, 4, 2, 5, 4, 4, 6]
b = []
[b.append(i) for i in a if i not in b]
print(b)

--first_list = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
 
# Convert to a set first
set_list = set(first_list)
 
# Now convert the set into a List
print(list(set_list))
 
second_list = [2, 3, 3, 2, 5, 4, 4, 6]
 
# Does the same as above, in a single line
print(list(set(second_list)))'''
