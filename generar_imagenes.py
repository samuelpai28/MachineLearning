"""
Generación de imágenes sintéticas y procesamiento por píxeles.
Solo se usa NumPy y operaciones con arreglos.
PIL se usa únicamente para cargar y guardar imágenes.
"""

import numpy as np
from PIL import Image


# ===================== SECCIÓN 1: Imágenes sintéticas =====================

def generar_gradiente_horizontal(alto, ancho):
    """
    Genera un gradiente horizontal en escala de grises.
    Negro (0) en la izquierda, blanco (255) en la derecha.
    """
    # Crear array 2D: valores incrementan linealmente por columna
    gradiente = np.zeros((alto, ancho), dtype=np.uint8)
    for col in range(ancho):
        valor = int(255 * col / (ancho - 1)) if ancho > 1 else 0
        gradiente[:, col] = valor
    return gradiente


def generar_rayas_diagonales(tamano, ancho_raya=8):
    """
    Genera patrón de rayas diagonales alternando blanco y negro.
    Orientación diagonal (~45°), basado en (fila + columna) con módulo.
    """
    rayas = np.zeros((tamano, tamano), dtype=np.uint8)
    for fila in range(tamano):
        for col in range(tamano):
            suma = fila + col
            if (suma // ancho_raya) % 2 == 0:
                rayas[fila, col] = 0
            else:
                rayas[fila, col] = 255
    return rayas


# ===================== SECCIÓN 2: Recorridos por píxeles =====================

def generar_tablero_rgb(lena, tamano_bloque=64):
    """
    Genera i4: Lena con tablero de ajedrez que selecciona canales R, G o B.
    Rojo: solo canal R de Lena; Verde: solo G; Azul: solo B.
    Patrón cíclico: fila 0: R,G,B,R,G,B...; fila 1: G,B,R,G,B,R...; fila 2: B,R,G,B,R,G...
    """
    alto, ancho = lena.shape[:2]
    if len(lena.shape) == 2:
        lena = np.stack([lena, lena, lena], axis=-1)
    
    resultado = np.zeros_like(lena)
    
    for fila in range(alto):
        for col in range(ancho):
            bloque_fila = fila // tamano_bloque
            bloque_col = col // tamano_bloque
            r_orig, g_orig, b_orig = lena[fila, col, 0], lena[fila, col, 1], lena[fila, col, 2]
            
            # Patrón cíclico: (bloque_fila + bloque_col) % 3 -> 0=R, 1=G, 2=B
            canal = (bloque_fila + bloque_col) % 3
            if canal == 0:
                resultado[fila, col] = [r_orig, 0, 0]
            elif canal == 1:
                resultado[fila, col] = [0, g_orig, 0]
            else:
                resultado[fila, col] = [0, 0, b_orig]
    
    return resultado.astype(np.uint8)


def generar_kaleidoscopio(lena):
    """
    Genera i5: Lena con rotación 90° CW y espejado vertical (simetría).
    Efecto caleidoscopio: mitad derecha = reflejo de mitad izquierda.
    """
    alto, ancho = lena.shape[:2]
    if len(lena.shape) == 2:
        lena = np.stack([lena, lena, lena], axis=-1)
    
    # Rotación 90° en sentido horario: (fila, col) -> (col, alto-1-fila)
    rotada = np.zeros((ancho, alto, 3), dtype=np.uint8)
    for fila in range(alto):
        for col in range(ancho):
            nueva_fila = col
            nueva_col = alto - 1 - fila
            rotada[nueva_fila, nueva_col] = lena[fila, col]
    
    # Espejado vertical: mitad derecha = reflejo de mitad izquierda
    ancho_rot = rotada.shape[1]
    mitad = ancho_rot // 2
    espejada = np.zeros_like(rotada)
    
    for fila in range(rotada.shape[0]):
        for col in range(ancho_rot):
            if col < mitad:
                espejada[fila, col] = rotada[fila, col]
            else:
                espejada[fila, col] = rotada[fila, ancho_rot - 1 - col]
    
    return espejada.astype(np.uint8)


# ===================== Main =====================

def main():
    base_path = r"c:\Users\Windows\Desktop\mcl"
    
    # --- SECCIÓN 1 ---
    print("Sección 1: Generando imágenes sintéticas...")
    
    # i1: Gradiente horizontal (usar dimensiones similares a la referencia)
    i1 = generar_gradiente_horizontal(256, 512)
    Image.fromarray(i1).save(f"{base_path}\\s1_i1_gradiente.jpeg")
    print("  - s1_i1_gradiente.jpeg")
    
    # i2: Rayas diagonales
    i2 = generar_rayas_diagonales(512, ancho_raya=16)
    Image.fromarray(i2).save(f"{base_path}\\s1_i2_rayas.jpeg")
    print("  - s1_i2_rayas.jpeg")
    
    # i3: Lena (cargar i3.jpeg - para esta imagen se usa lo necesario)
    i3 = np.array(Image.open(f"{base_path}\\i3.jpeg").convert("RGB"))
    Image.fromarray(i3).save(f"{base_path}\\s1_i3_lena.jpeg")
    print("  - s1_i3_lena.jpeg")
    
    # --- SECCIÓN 2 ---
    print("\nSección 2: Generando desde Lena con recorridos por píxeles...")
    
    # Usar Lena (i3) de la sección 1
    lena = i3
    
    # i4: Tablero RGB
    i4 = generar_tablero_rgb(lena, tamano_bloque=64)
    Image.fromarray(i4).save(f"{base_path}\\s2_i4_tablero_rgb.jpeg")
    print("  - s2_i4_tablero_rgb.jpeg")
    
    # i5: Caleidoscopio (rotación + espejado)
    i5 = generar_kaleidoscopio(lena)
    Image.fromarray(i5).save(f"{base_path}\\s2_i5_kaleidoscopio.jpeg")
    print("  - s2_i5_kaleidoscopio.jpeg")
    
    print("\nListo.")


if __name__ == "__main__":
    main()
