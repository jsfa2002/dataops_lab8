# Diagrama del Pipeline

Adjunta un diagrama (por ejemplo `docs/pipeline_diagram.png`) si lo creaste con draw.io o diagrams.net.

Componentes principales:
- Fuentes: CSVs en `data/raw/`
- Ingesta: `scripts/download_sample_data.py`
- Validación: `src/data_validation.py`
- Procesamiento: `src/data_processing.py`
- Enriquecimiento: `src/data_enrichment.py`
- Calidad: `src/quality_checks.py`
- Entrega: `data/outputs/`
- Observabilidad: `logs/pipeline_execution.log`
