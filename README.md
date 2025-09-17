# Semaforo-Auxiliar-Portatil
PROYECTO: Sistema de Semáforo Auxiliar Portátil (PCB + Ensamble 3D)

DESCRIPCIÓN
Este repositorio contiene los archivos de diseño electrónico (OrCAD Capture CIS y OrCAD PCB Editor/Allegro),
el ensamble mecánico 3D (Onshape), y las salidas de fabricación del sistema de semáforo auxiliar portátil.
La placa principal es el núcleo del sistema: integra conversión 12 V → 5 V, interfaz USB 2.0, y drivers para
actuadores a 12 V (sirena y baliza/LED estroboscópico).

ESTADO DEL PROYECTO
- Dimensiones PCB: 85 mm × 80 mm, stack-up de 4 capas (L1 Señal / L2 GND / L3 Potencia / L4 Señal).
- Objetivo de impedancia USB 2.0 (D+/D–): 90 Ω ± 15 %.
- Componentes clave: LM2678S-5.0 (buck 12→5 V/5 A), L = 22 µH (LQH66SN220MD3L), MOSFET IRLML6344TRPBF,
  diodos SS14 (40 V/1 A) para protección de cargas, TVS en bus de 12 V. Relés SRD-12VDC-SL-C poblables opcionalmente.

ENLACES PRINCIPALES
- Onshape : https://cad.onshape.com/documents/9514c50148bd30af94668b6e/w/10fd001a8c3af11061b3f61f/e/184a6b5370e97d5e23dc29c5?renderMode=0&uiState=68ca4ee6e96fa2d06b671376

ESTRUCTURA DEL REPOSITORIO
/pcb/
  /capture/                → Archivos de esquemático (.opj, .dsn, libs)
  /allegro/                → Archivos de PCB Editor (.brd, .dra, .psm, .pad)
  /constraints/            → Reglas (Constraint Manager .dcf/.csv, pares diferenciales USB)
/fabrication/
  /gerbers/                → RS-274X por capa (GTL, GBL, GTS, GBS, GTO, GBO, GKO, etc.)
  /nc_drill/               → Taladros (.drl) y tabla de taladros
  /ipc_2581_odbpp/         → Opcional según fabricante
  /step/                   → Export STEP 3D de la PCB
/docs/
  /images/                 → Figuras del documento (ruteo, planos, DRC, 3D)
  /budget/                 → Budget energético y anexos (PDF/CSV)
/bom/
  BOM_resumen.csv          → Resumen por componente (PN fabricante)
  BOM_detallada_refdes.csv → BOM por RefDes (R/C/D/Q/U/J/K/L)
/links/
  onshape.txt              → Enlace Onshape y versión/Workspace
  referencias.txt          → Citas ISO 690 (documentos electrónicos)
/releases/
  v1.0_fabricacion/        → Paquete listo para enviar a fábrica (zip con /fabrication)
