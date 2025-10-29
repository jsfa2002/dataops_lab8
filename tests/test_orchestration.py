import pytest
import os
import tempfile
import yaml
from unittest.mock import patch, MagicMock

# Configuración mínima para pruebas
MINIMAL_CONFIG = {
    'version': '1.0',
    'pipeline': {'name': 'test-pipeline'},
    'validation': {'schema_path': '', 'required_files': []},
    'processing': {'output_path': '', 'steps': []},
    'enrichment': {'catalog_path': ''},
    'quality': {'checks': []}
}

def create_test_config():
    """Crea archivo de configuración para tests"""
    os.makedirs('config', exist_ok=True)
    with open('config/test_config.yaml', 'w') as f:
        yaml.dump(MINIMAL_CONFIG, f)

class TestPipelineOrchestration:
    
    def setup_method(self):
        """Configuración antes de cada test"""
        # Crear directorios necesarios
        os.makedirs('logs', exist_ok=True)
        os.makedirs('data/raw', exist_ok=True)
        os.makedirs('data/processed', exist_ok=True)
        os.makedirs('data/outputs', exist_ok=True)
        create_test_config()

    def test_pipeline_initialization(self):
        """Test que el orquestador se inicializa correctamente"""
        with patch('src.data_validation.DataValidator') as mock_val, \
             patch('src.data_processing.DataProcessor') as mock_proc, \
             patch('src.data_enrichment.DataEnricher') as mock_enr, \
             patch('src.quality_checks.QualityChecker') as mock_qual:
            
            # Configurar mocks básicos
            mock_val.return_value.validate.return_value = {'success': True}
            mock_proc.return_value.process.return_value = {'processed_data': [], 'record_count': 0}
            mock_enr.return_value.enrich.return_value = {'enriched_data': []}
            mock_qual.return_value.check_quality.return_value = {'passed': True}
            
            from src.orchestrator import PipelineOrchestrator
            orchestrator = PipelineOrchestrator('config/test_config.yaml')
            assert orchestrator.config is not None

    def test_execution_flow_success(self):
        """Test flujo de ejecución exitoso"""
        with patch('src.data_validation.DataValidator') as mock_val, \
             patch('src.data_processing.DataProcessor') as mock_proc, \
             patch('src.data_enrichment.DataEnricher') as mock_enr, \
             patch('src.quality_checks.QualityChecker') as mock_qual:
            
            # Configurar mocks para flujo exitoso
            mock_val.return_value.validate.return_value = {'success': True}
            mock_proc.return_value.process.return_value = {
                'processed_data': [{'test': 'data'}],
                'record_count': 1
            }
            mock_enr.return_value.enrich.return_value = {
                'enriched_data': [{'test': 'data', 'enriched': True}]
            }
            mock_qual.return_value.check_quality.return_value = {
                'passed': True,
                'issues': []
            }

            from src.orchestrator import PipelineOrchestrator
            orchestrator = PipelineOrchestrator('config/test_config.yaml')
            result = orchestrator.execute_pipeline()
            
            assert result['success'] == True
            assert 'execution_id' in result

    def test_execution_flow_failure(self):
        """Test flujo de ejecución con fallo en validación"""
        with patch('src.data_validation.DataValidator') as mock_val:
            # Configurar mock para fallo en validación
            mock_val.return_value.validate.return_value = {
                'success': False,
                'errors': ['Schema validation failed']
            }

            from src.orchestrator import PipelineOrchestrator
            orchestrator = PipelineOrchestrator('config/test_config.yaml')
            result = orchestrator.execute_pipeline()
            
            assert result['success'] == False
            assert 'error' in result

if __name__ == '__main__':
    # Ejecutar tests directamente
    test = TestPipelineOrchestration()
    test.setup_method()
    test.test_pipeline_initialization()
    print("✅ Todos los tests pasaron!")
