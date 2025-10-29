import yaml
import logging
import json
import os
from datetime import datetime

class PipelineOrchestrator:
    def __init__(self, config_path='config/pipeline_config.yaml'):
        self.config_path = config_path
        self.config = self.load_config(config_path)
        self.setup_logging()

    def load_config(self, config_path):
        """Carga configuración con manejo robusto de errores"""
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            # Configuración por defecto si falla la carga
            return {
                'version': '1.0',
                'pipeline': {'name': 'default-pipeline'},
                'validation': {'schema_path': '', 'required_files': []},
                'processing': {'output_path': 'data/processed/', 'steps': []},
                'enrichment': {'catalog_path': ''},
                'quality': {'checks': []}
            }

    def setup_logging(self):
        """Configura el logging de manera robusta"""
        try:
            os.makedirs('logs', exist_ok=True)
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.StreamHandler()  # Solo consola para tests
                ]
            )
            self.logger = logging.getLogger(__name__)
        except Exception as e:
            # Fallback básico
            import sys
            logging.basicConfig(level=logging.INFO, stream=sys.stdout)
            self.logger = logging.getLogger(__name__)

    def execute_pipeline(self):
        """Ejecuta el pipeline completo con manejo robusto de errores"""
        execution_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.logger.info(f"Iniciando ejecución del pipeline: {execution_id}")
        
        try:
            # 1. Validación de datos
            self.logger.info("Ejecutando validación de datos...")
            from src.data_validation import DataValidator
            validator = DataValidator(self.config.get('validation', {}))
            validation_result = validator.validate()
            
            if not validation_result.get('success', True):
                raise Exception(f"Validación fallida: {validation_result.get('errors', 'Error desconocido')}")

            # 2. Procesamiento de datos
            self.logger.info("Ejecutando procesamiento de datos...")
            from src.data_processing import DataProcessor
            processor = DataProcessor(self.config.get('processing', {}))
            processing_result = processor.process()

            # 3. Enriquecimiento de datos
            self.logger.info("Ejecutando enriquecimiento de datos...")
            from src.data_enrichment import DataEnricher
            enricher = DataEnricher(self.config.get('enrichment', {}))
            enrichment_result = enricher.enrich(processing_result.get('processed_data', []))

            # 4. Validación de calidad
            self.logger.info("Ejecutando validación de calidad...")
            from src.quality_checks import QualityChecker
            quality_checker = QualityChecker(self.config.get('quality', {}))
            quality_result = quality_checker.check_quality(enrichment_result.get('enriched_data', []))
            
            if not quality_result.get('passed', True):
                raise Exception(f"Validación de calidad fallida: {quality_result.get('issues', 'Problemas de calidad')}")

            # 5. Generación de reportes
            self.logger.info("Generando reportes...")
            self.generate_reports(enrichment_result.get('enriched_data', []), execution_id)

            self.logger.info(f"Pipeline completado exitosamente: {execution_id}")
            return {
                'success': True,
                'execution_id': execution_id,
                'records_processed': processing_result.get('record_count', 0)
            }

        except Exception as e:
            self.logger.error(f"Error en el pipeline: {str(e)}")
            return {'success': False, 'error': str(e)}

    def generate_reports(self, data, execution_id):
        """Genera reportes de ejecución"""
        try:
            os.makedirs('data/outputs', exist_ok=True)
            report = {
                'execution_id': execution_id,
                'timestamp': datetime.now().isoformat(),
                'records_processed': len(data),
                'pipeline_version': self.config.get('version', '1.0')
            }
            
            out_path = f'data/outputs/report_{execution_id}.json'
            with open(out_path, 'w') as f:
                json.dump(report, f, indent=2)
            self.logger.info(f"Reporte guardado en {out_path}")
        except Exception as e:
            self.logger.warning(f"No se pudo generar reporte: {e}")

if __name__ == '__main__':
    orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
    result = orchestrator.execute_pipeline()
    print("Resultado final:", result)
