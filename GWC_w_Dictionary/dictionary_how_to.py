# los diccionarios están definidos por {} y están formados por muchos pares clave-valor (key-val pairs)
library_dictionary = {
    'book_name' : 'Dr. Seuss',
    'book_status': 'On Shelf'

}


# ¿Cómo acceder a los diccionarios de Python? (2)
print(library_dictionary['book_name']) 
# OR
print(library_dictionary.get('book_name'))


# ¿Cómo modificar un par clave-valor en los diccionarios de Python?
library_dictionary['book_name'] = 'Junie B. Jones'
print(library_dictionary['book_name'])

# para actualizar múltiples pares clave-valor dentro un diccionario: 🤔
library_dictionary.update({'book_name': 'Cam Jansen'}) # update only holds 1 argument at a time
print(library_dictionary['book_name'])

# para agregar un nuevo par clave-valor:
library_dictionary['book_name'] = 'Becoming'
library_dictionary['book_status'] = 'Checked Out'
print(library_dictionary['book_name'])
print(library_dictionary['book_status'])

# cómo recorrer un diccionario:
for key, value in library_dictionary.items():

    print(f'\nthe key {key} has a value of {value}\n')


# Escribí un diccionario de python sobre cómo hacerlo. 