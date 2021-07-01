nombre= input('¿como te llamas')
edad= input('¿Cuantos años tienes?')
direccion= input('¿Cual es tu direccion? ')
telefono= input('¿Cual es tu numero de telefono? ')
persona= {'nombre': nombre,
          'edad': edad,
          'direccion': direccion,
          'telefono': telefono}
print(persona['nombre'])