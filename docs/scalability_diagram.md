# Diagrama de escalabilidad 

<img width="440" height="798" alt="image" src="https://github.com/user-attachments/assets/756dac3a-8c1f-4bc9-b0dd-1c24b3d50dd8" />

## Detalles de Escalabilidad

### Nivel 1: Local
- **Volumen**: < 1 GB
- **Herramientas**: GitHub Actions, Pandas
- **Costo**: $0 (dentro de límites gratuitos)
- **Caso de uso**: Desarrollo, pruebas, datos pequeños

### Nivel 2: Nube
- **Volumen**: 1-10 GB  
- **Herramientas**: Azure Functions, Blob Storage
- **Costo**: ~$0.20 por millón de ejecuciones
- **Caso de uso**: Datos medianos, procesamiento periódico

### Nivel 3: Distribuido
- **Volumen**: > 10 GB
- **Herramientas**: Databricks, Spark, Data Lake
- **Costo**: ~$0.40/DBU + almacenamiento
- **Caso de uso**: Big Data, procesamiento en tiempo real
