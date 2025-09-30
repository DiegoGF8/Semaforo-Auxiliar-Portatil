#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time

def main():
    cap = cv2.VideoCapture('/dev/video1')
    if not cap.isOpened():
        print("ERROR: No se pudo abrir /dev/video1")
        return

    # Rangos HSV
    red_ranges = [
        (np.array([0, 100, 100], dtype=np.uint8),  np.array([10, 255, 255], dtype=np.uint8)),
        (np.array([170, 100, 100], dtype=np.uint8),np.array([180, 255, 255], dtype=np.uint8))
    ]
    yellow_range = (np.array([15, 100, 100], dtype=np.uint8),
                    np.array([35, 255, 255], dtype=np.uint8))
    green_range  = (np.array([40, 100, 100], dtype=np.uint8),
                    np.array([90, 255, 255], dtype=np.uint8))

    prev_color = None
    last_time = None
    min_area = 300  # umbral mínimo en píxeles

    while True:
        ret, frame = cap.read()
        if not ret:
            print("ERROR: No hay frame")
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Máscaras
        red_mask    = cv2.inRange(hsv, *red_ranges[0])   | cv2.inRange(hsv, *red_ranges[1])
        yellow_mask = cv2.inRange(hsv, *yellow_range)
        green_mask  = cv2.inRange(hsv, *green_range)

        # Conteos
        counts = {
            "Rojo":     cv2.countNonZero(red_mask),
            "Amarillo": cv2.countNonZero(yellow_mask),
            "Verde":    cv2.countNonZero(green_mask)
        }

        # Color dominante
        color, area = max(counts.items(), key=lambda x: x[1])
        if area < min_area:
            color = "Ninguno"

        # Mostrar texto en la imagen
        color_bgr = {"Rojo": (0,0,255), "Amarillo": (0,255,255), "Verde": (0,255,0)}.get(color, (255,255,255))
        cv2.putText(frame, color, (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color_bgr, 2)

        # Cronómetro de cambios
        if color != "Ninguno":
            now = time.time()
            if prev_color is None:
                prev_color = color
                last_time = now
            elif color != prev_color:
                duration = now - last_time
                # Usamos solo ASCII: “dura” en lugar de “duró” y “->” en lugar de flecha Unicode  
                print(f"{prev_color} dura {duration:.2f} s -> {color}")
                prev_color = color
                last_time = now

        cv2.imshow("Paso 4: Semaforo", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
