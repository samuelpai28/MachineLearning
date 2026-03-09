# Documentación: Generación de Imágenes

Este proyecto genera imágenes usando **solo NumPy y operaciones con arreglos**. PIL se utiliza únicamente para cargar y guardar archivos.

---

## Sección 1: Imágenes sintéticas

### s1_i1_gradiente.jpeg
**Gradiente horizontal en escala de grises**

- Negro (0) a la izquierda, blanco (255) a la derecha.
- Para cada columna: `valor = 255 * col / (ancho - 1)`.
- Todas las filas de una columna tienen el mismo valor.

### s1_i2_rayas.jpeg
**Rayas diagonales (alternando blanco y negro)**

- Patrón a 45° usando `suma = fila + columna`.
- Si `(suma // ancho_raya) % 2 == 0` → negro; si no → blanco.
- Parámetro `ancho_raya = 16` píxeles.

### s1_i3_lena.jpeg
**Imagen Lena**

- Se carga desde `i3.jpeg` (imagen de prueba estándar).
- Conversión a RGB para compatibilidad.

---

## Sección 2: Recorridos por píxeles

Parten de la imagen Lena (i3).

### s2_i4_tablero_rgb.jpeg
**Tablero con selección de canales RGB**

- La imagen se divide en bloques de 64×64 píxeles.
- En cada bloque se muestra solo un canal: R, G o B.
- Patrón: `canal = (bloque_fila + bloque_col) % 3` → 0=R, 1=G, 2=B.
- Resultado: efecto de separación de canales por región.

### s2_i5_kaleidoscopio.jpeg
**Rotación 90° y simetría vertical**

1. **Rotación horaria:** `(fila, col) → (col, alto - 1 - fila)`.
2. **Espejado:** la mitad derecha es reflejo de la mitad izquierda.
3. Efecto visual tipo caleidoscopio.

---

## Uso

```bash
pip install -r requirements.txt
python generar_imagenes.py
```

Las imágenes se guardan en la misma carpeta del script.
