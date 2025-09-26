# Semaforo-Auxiliar-Portatil
PROYECTO: Sistema de Semáforo Auxiliar Portátil (PCB + Ensamble 3D)

DESCRIPCIÓN
Este repositorio contiene los archivos de diseño electrónico (OrCAD Capture CIS y OrCAD PCB Editor/Allegro),
el ensamble mecánico 3D (Onshape), y las salidas de fabricación del sistema de semáforo auxiliar portátil.
La placa principal es el núcleo del sistema: integra conversión 12 V → 5 V, interfaz USB 2.0, y drivers para
actuadores a 12 V (sirena y baliza/LED estroboscópico).

ESTADO DEL PROYECTO
- Dimensiones PCB: 85 mm × 80 mm, stack-up de 3 capas (L1 Señal / L2 Potencia  / L3 GND).
- Objetivo de impedancia USB 2.0 (D+/D–): 90 Ω ± 15 %.
- Componentes clave: LM2678S-5.0 (buck 12→5 V/5 A), L = 22 µH (LQH66SN220MD3L), MOSFET IRLML6344TRPBF,
  diodos SS14 (40 V/1 A) para protección de cargas, Relés SRD-12VDC-SL-C.

ENLACES PRINCIPALES
- Onshape : https://cad.onshape.com/documents/21fef1b3eacda39c10852529/w/79fc7292a46ee710a65da7c9/e/ed5080d8918c1aaba1ee2e94?renderMode=0&uiState=68d63b17d7190df0bb4cd378

