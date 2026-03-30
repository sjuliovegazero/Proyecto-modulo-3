README — Gestión de Contactos
====================================================

1) Objetivo
-----------
Crear un programa por consola para administrar contactos.
Permite:
- Agregar contactos
- Listar contactos
- Buscar contactos (por nombre o teléfono)
- Editar contactos
- Eliminar contactos
- Salir

2) Requisitos
-------------
- Python 3
- No se utilizan librerías externas

3) Cómo ejecutar
----------------
- Abre la terminal buscando cmd en Windows o también abriendo Powershell
- Define el directorio de trabajo usando:
   cd + ruta de la carpeta donde se encuentra el archivo
   (ejemplo: cd Desktop\MiCarpeta)

- Ejecuta en la terminal:

   python Sistema_Gestion_Contactos.py

4) Estructura de datos
----------------------
Se usa una lista llamada 'contactos' que contiene diccionarios.
Cada producto tiene estas claves:

- nombre (texto)
- teléfono (texto)
- correo (texto)
- dirección (texto)

Ejemplo:
{
  "nombre": "Sebastián Julio",
  "teléfono": "123456",
  "correo": "sjulio@gmail.com",
  "direccion": "mi casa"
}

5) Menú del sistema
-------------------
1) Agregar contactos
2) Listar contactos
3) Buscar contactos
4) Editar contactos
5) Eliminar contactos
6) Salir

6) Validaciones incluidas
-------------------------
- Si no hay contactos, listar/editar/eliminar muestra mensaje y no falla.
- El índice debe ser numérico (isdigit) y estar dentro del rango.
- Se evita duplicar un contactos por nombre exacto (ignorando mayúsculas).