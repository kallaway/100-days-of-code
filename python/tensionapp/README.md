# Aplicación para trackear la presión sanguinea

Esta es una app que permite registrar, analizar y mostrar relaciones en la toma periódica de presión sanguinea

## Notas del dominio

- Cada toma de presión está compuesta por los siguientes datos:
  - quién tomó
  - presión sitólica (la Alta)
  - presióno diastólica (la baja)
  - frecuencia cardíaca (latidos por minuto)
  - tipo de tensiometro
  - fecha y hora hora de la toma
  - Observaciones
  - Tomó medicación?
  - Qué medicación se tomo
  - fecha y hora de la toma de medicación
- Se tiene que poder cargar todos los datos. Los únicos requeridos son presión sis y dias, la fecha y horario de la toma de presión
- Cada registro de medicacón está compuesto por:
  - fecha en que nos recetaron por primera vez la medicación
  - medicación(nombre genérico)
- la app no guarda datos de referencia personal del usuario, no se guardan ni nombre, ni ningún dato personal más que lo que se carga
- De los registros de toma, se tiene que poder editar los campos:
  - observaciones
  - tomó medicación
  - qué medicación
  - fecha y hora de la toma de medicación
  - si se edita, tiene que haber algúna forma de registro de esta edición.
- El campo quién tomó es un campo en el que deben ir datos definidos por el usuario en otro lado para que haya consistencia en los datos.
- no se pueden borrar datos del registro de tomas
- no se pueden borrar datos del registro de medicamentos
- Se pueden borrar o actualizar datos del registro de quienes toman. Si se borra un dato de esta tabla, el dato asociado al registro de toma pasa a ser NULL
## Notas del desarrollo
- Debería haber una forma de captar/loggear errores en la base de datos ver:
  - https://newbedev.com/error-handling-in-sqlalchemy
  - https://docs.sqlalchemy.org/en/14/core/exceptions.html

