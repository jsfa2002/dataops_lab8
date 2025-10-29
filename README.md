# DataOps Lab 8 - Orquestación y Diagramación de Pipelines (Ventas)

Este repositorio contiene la implementación completa del Laboratorio 8 (en español), tema: **sales (ventas)**.

## Estructura principal
- `src/` : código del orquestador y módulos de pipeline.
- `config/` : configuración YAML del pipeline.
- `data/` : datos de ejemplo (raw, schemas, outputs).
- `docs/` : diagramas y documentación requeridos por la guía.
- `tests/` : pruebas unitarias e integración.
- `.github/workflows/` : workflows para CI y CD.
- `scripts/` : utilidades (generar datos, validar config, reporte de ejecución).

## Ejecución rápida (local)
1. Crear y activar un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Generar datos de ejemplo (ya incluidos) o ejecutar el script de descarga:
   ```bash
   python scripts/download_sample_data.py
   ```
3. Validar config:
   ```bash
   python scripts/validate_config.py
   ```
4. Ejecutar pipeline:
   ```bash
   python src/orchestrator.py
   ```
5. Ejecutar tests:
   ```bash
   pytest -q
   ```

