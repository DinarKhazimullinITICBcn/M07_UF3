contactes = {'Roger':678232311, 'Oriol':566879326}
def elimina(contactes, user):
    if user in contactes :
        del contactes[user]
    return contactes
print(elimina(contactes, 'Pablo'))
#Errors:
  #del no funciona si el user no existeix en el diccionari, per lo qual hauriem de comprovar si existeix
  #No podem retornar el contacte user si ja hem eliminar el contacte user. Eliminar Oriol per despres retornar Oriol donara error