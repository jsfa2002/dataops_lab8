# src/data_validation.py
# tests/integration_test.py
import os
import sys
import tempfile
import shutil

def run_integration():
    """Ejecuta prueba de integración en un directorio temporal"""
    print("Iniciando prueba de integración...")
    
    # Crear directorio temporal para pruebas
    test_dir = tempfile.mkdtemp()
    original_dir = os.getcwd()
    
    try:
        print(f" Directorio temporal: {test_dir}")
        os.chdir(test_dir)
        
        # Crear estructura completa de directorios
        dirs = [
            'config',
            'data/raw', 
            'data/processed',
            'data/outputs',
            'data/schemas',
            'logs',
            'src'
        ]
        
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
            print(f"Creando directorio: {dir_path}")

        # 1. Crear archivo de configuración
        config_content = """
version: "1.0"
pipeline:
  name: "test-integration-pipeline"
validation:
  schema_path: "data/schemas/sales_schema_v1.json"
  required_files:
    - "data/raw/sales_data.csv"
    - "data/raw/product_catalog.csv"
processing:
  output_path: "data/processed/"
  steps:
    - "clean_duplicates"
    - "handle_missing_values"
    - "calculate_totals"
enrichment:
  catalog_path: "data/raw/product_catalog.csv"
quality:
  checks:
    - "completeness_threshold: 0.95"
    - "freshness_max_hours: 24"
    - "row_count_variation: 0.1"
"""
        with open('config/pipeline_config.yaml', 'w') as f:
            f.write(config_content)
        print("Configuración creada")

        # 2. Crear esquema
        schema_content = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": "sales",
            "type": "object",
            "properties": {
                "order_id": {"type": "string"},
                "product_id": {"type": "string"},
                "quantity": {"type": "integer", "minimum": 0},
                "price": {"type": "number", "minimum": 0},
                "region": {"type": "string"},
                "order_date": {"type": "string", "format": "date-time"}
            },
            "required": ["order_id", "product_id", "quantity", "price", "order_date"]
        }
        
        import json
        with open('data/schemas/sales_schema_v1.json', 'w') as f:
            json.dump(schema_content, f, indent=2)
        print(" Esquema creado")

        # 3. Crear datos de ventas
        sales_data = [
            "order_id,product_id,quantity,price,region,order_date",
            "O-001,P-001,2,10.0,north,2025-10-01T10:00:00",
            "O-002,P-002,1,20.0,south,2025-10-02T11:00:00",
            "O-003,P-001,3,10.0,east,2025-10-03T12:00:00"
        ]
        with open('data/raw/sales_data.csv', 'w') as f:
            f.write("\n".join(sales_data))
        print(" Datos de ventas creados")

        # 4. Crear catálogo de productos
        catalog_data = [
            "product_id,product_name,category",
            "P-001,Producto A,Cat1",
            "P-002,Producto B,Cat2",
            "P-003,Producto C,Cat1"
        ]
        with open('data/raw/product_catalog.csv', 'w') as f:
            f.write("\n".join(catalog_data))
        print(" Catálogo de productos creado")

        # 5. Copiar código fuente
        source_files = [
            'orchestrator.py',
            'data_validation.py', 
            'data_processing.py',
            'data_enrichment.py',
            'quality_checks.py'
        ]
        
        # Agregar directorio original al path para imports
        sys.path.insert(0, original_dir)
        
        for file in source_files:
            src_path = os.path.join(original_dir, 'src', file)
            dst_path = os.path.join('src', file)
            
            if os.path.exists(src_path):
                with open(src_path, 'r') as src, open(dst_path, 'w') as dst:
                    dst.write(src.read())
                print(f"✅ Copiado: {file}")
            else:
                print(f"⚠️  Archivo no encontrado: {src_path}")

        # 6. Ejecutar el pipeline
        print("🚀 Ejecutando pipeline...")
        from src.orchestrator import PipelineOrchestrator
        
        orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
        result = orchestrator.execute_pipeline()
        
        print(f" Resultado: {result}")
        
        # 7. Verificar resultados
        if result.get('success'):
            print(" PRUEBA DE INTEGRACIÓN EXITOSA!")
            
            # Verificar archivos generados
            outputs = os.listdir('data/outputs')
            processed = os.listdir('data/processed')
            
            print(f" Archivos de salida: {outputs}")
            print(f" Archivos procesados: {processed}")
            
            return 0
        else:
            print(f" Pipeline falló: {result.get('error')}")
            return 1
            
    except Exception as e:
        print(f" ERROR en prueba de integración: {e}")
        import traceback
        traceback.print_exc()
        return 1
    finally:
        # Volver al directorio original
        os.chdir(original_dir)
        
        # Limpiar directorio temporal (opcional para debugging)
        # shutil.rmtree(test_dir, ignore_errors=True)
        print(f"Directorio temporal mantenido para debugging: {test_dir}")

if __name__ == '__main__':
    exit_code = run_integration()
    sys.exit(exit_code)
