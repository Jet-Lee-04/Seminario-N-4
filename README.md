# Seminario-N-4
En este repositorio subire mi informe de seminario Nº4

# Detección de Cuerpos con OpenCV

Programa que detecta personas en tiempo real usando la cámara web.

## Descripción

Este proyecto utiliza OpenCV para identificar cuerpos completos de personas a través de la cámara. Cuando detecta a alguien, dibuja un rectángulo azul alrededor de la persona y muestra las coordenadas de posición en la consola.

## Funcionalidades

- Detección automática de personas en tiempo real
- Visualización con rectángulos de color azul
- Muestra coordenadas (x, y, ancho, alto) en la terminal
- Control simple para salir del programa

## Instalación

Instala OpenCV:
```bash
pip install opencv-python
```

## Uso

1. Ejecuta el archivo Python
2. La cámara se abrirá automáticamente
3. Párate frente a la cámara para ser detectado
4. Presiona la tecla 's' para cerrar el programa

## Cómo funciona

El programa usa un clasificador preentrenado llamado Haar Cascade que puede reconocer formas de cuerpos humanos. Captura video de la cámara frame por frame, convierte cada imagen a escala de grises para procesarla más rápido, y busca patrones que coincidan con cuerpos completos.

## Requisitos

- Python 3.x instalado
- Cámara web funcionando
- Buena iluminación en la habitación
- Mantenerse de pie y visible para mejor detección

## Notas

- Funciona mejor cuando la persona está completamente visible
- La detección mejora con buena luz
- El programa se cierra de forma segura con la tecla 's'
