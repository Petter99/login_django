# Clase: Funcionamiento de autenticación

Este proyecto es una aplicación de autenticación de usuarios en Django que permite el registro e inicio de sesión. Utiliza un modelo de usuario con los campos `email`, `password` y `role`. Además, emplea un sistema básico de encriptación donde la contraseña se almacena en orden inverso.

## Funcionalidades
- Registro de usuario con email, contraseña y rol.
- Inicio de sesión verificando email y contraseña.
- Encriptación básica de contraseñas invirtiendo el string.
- Validación de credenciales mediante comparación con la contraseña encriptada.
- Utilizacion de middelwares y cookies.

Creado para la clase de Programación Web 1 de la Universidad del Valle de Guatemala Campus Altiplano
