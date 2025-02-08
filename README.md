# README - Mejoras Implementadas con IA

En este archivo **README**, se encuentran las principales diferencias y mejoras en funcionalidades realizadas con IA en cada una de las consignas. Cabe aclarar que estas mejoras fueron solicitadas a una IA después de haber completado la consigna de manera independiente, específicamente el día **viernes 7**. Podrán ver la fecha y hora exactas de cada actualización en **GIT**.

El objetivo de este proceso fue aprender qué más podría haber agregado al código original y cómo optimizarlo, permitiéndome aplicar estos métodos en futuros proyectos cuando sea necesario.

Sin más que agregar, espero que las consignas originales cumplan con lo solicitado y quedo a la espera de la devolución correspondiente.

Muchas gracias.

**Juan Ignacio Mora**

---

## Mejoras por Consigna

### **CONSIGNA 1 - IA**
✅ **Manejo de errores**: Si el usuario ingresa valores incorrectos (letras o símbolos), el programa mostrará un mensaje en lugar de fallar.  
✅ **Eliminación de espacios en la entrada**: Se permite ingresar "1, 2, 3" en lugar de "1,2,3" sin afectar el funcionamiento.  
✅ **Función separada para la entrada de datos**: Mejora la organización del código y facilita su reutilización.  
✅ **Tipado en la función**: Se agregaron anotaciones de tipo para mejorar la claridad del código.  

---

### **CONSIGNA 2 - IA**
✅ **Eliminación de espacios en blanco**: Ahora los elementos ingresados por el usuario se limpian con `.strip()`, evitando errores en la comparación.  
✅ **Verificación de conjunto vacío antes de eliminar**: Si el conjunto está vacío, se muestra un mensaje en lugar de intentar eliminar un elemento inexistente.  
✅ **Mensajes más descriptivos**: Se mejoraron los mensajes de salida para mayor claridad.  

---

### **CONSIGNA 3 - IA**
✅ **Función `obtener_conjunto()` para la entrada de datos**:  
✔️ Separa la lógica de entrada en una función reutilizable.  
✔️ Maneja errores de entrada (`ValueError`) para evitar fallos si el usuario ingresa caracteres no numéricos.  
✔️ Elimina espacios en blanco para evitar problemas con la conversión de enteros.  
✅ **Manejo de errores mejorado**: Si el usuario ingresa valores incorrectos, se le pedirá que vuelva a intentarlo.  

---

### **CONSIGNA 4 - IA**
✅ **Eliminación de espacios adicionales**: Cada cadena ingresada se limpia con `.strip()`, evitando errores por espacios extra.  
✅ **Mantiene el orden de aparición**: Se usa `dict.fromkeys(lista)` en lugar de `set(lista)`, para eliminar duplicados sin alterar el orden original.  
✅ **Función `obtener_lista()` para la entrada de datos**:  
✔️ Verifica que el usuario no deje la entrada vacía.  
✔️ Separa la lógica de entrada del usuario, mejorando la claridad y reutilización del código.  

---

### **CONSIGNA 5 - IA**
✅ **Validación del número en la función `factorial()`**: Se verifica que `n` sea mayor o igual a 0, lanzando un error si no lo es.  
✅ **Nueva función `obtener_numero()`**:  
✔️ Maneja errores de entrada, evitando que el programa falle si el usuario ingresa texto.  
✔️ Asegura que el usuario solo pueda ingresar números enteros positivos.  

---

### **CONSIGNA 6 - IA**
✅ **Manejo de espacios en blanco**: Ahora la lista ingresada por el usuario elimina espacios adicionales con `.strip()`, evitando errores en la comparación.  
✅ **Funciones separadas para entrada de datos**:  
✔️ `obtener_lista()`: Separa la lógica de obtención de la lista, mejorando la reutilización y limpieza del código.  
✔️ `obtener_elemento()`: Permite ingresar el elemento de forma separada, asegurando que también se eliminen espacios extra.  

---

### **CONSIGNA 7 - IA**
✅ **Validación del número en `suma_recursiva()`**: Se verifica que `n` sea positivo y se lanza un `ValueError` si no lo es.  
✅ **Nueva función `obtener_numero()`**:  
✔️ Maneja errores de entrada para evitar fallos si el usuario ingresa texto en lugar de un número.  
✔️ Asegura que el usuario solo ingrese números enteros positivos.  

---

### **CONSIGNA 8 - IA**
✅ **Nueva función `es_pdf()` en `LibroDigital`**: Permite verificar si el libro digital está en formato PDF, facilitando su identificación.  
✅ **Función `obtener_libro()`**:  
✔️ Permite al usuario ingresar datos y crea un objeto `Libro` o `LibroDigital` según corresponda.  
✔️ Maneja la decisión de si el libro es digital con una entrada `s/n`, mejorando la interacción.  
✅ **Verificación del formato PDF al final del script**: Si el libro es digital, se verifica su formato y se muestra un mensaje indicando si es PDF o no.  

---

**📌 Con estas mejoras, el código ahora es más eficiente, reutilizable y fácil de mantener. ¡Gracias por leer! 🚀**

