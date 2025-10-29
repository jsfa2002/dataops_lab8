# Diagrama del Pipeline

<img width="551" height="761" alt="image" src="https://github.com/user-attachments/assets/9763b8b5-7c82-4afd-8ab2-2d3b1d5940ca" />

Componentes principales:
- Fuentes: CSVs en `data/raw/`
- Ingesta: `scripts/download_sample_data.py`
- Validación: `src/data_validation.py`
- Procesamiento: `src/data_processing.py`
- Enriquecimiento: `src/data_enrichment.py`
- Calidad: `src/quality_checks.py`
- Entrega: `data/outputs/`
- Observabilidad: `logs/pipeline_execution.log`
