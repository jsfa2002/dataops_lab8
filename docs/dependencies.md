# Dependencias del Pipeline

- Validación: requiere esquema (`data/schemas/sales_schema_v1.json`) y archivos en `validation.required_files`
- Transformación: depende de validación exitosa
- Enriquecimiento: depende de procesado y requiere `data/raw/product_catalog.csv`
- Carga/Entregas: depende de enriquecimiento exitoso
