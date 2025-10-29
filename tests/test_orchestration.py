# tests/test_orchestration.py
import pytest
from unittest.mock import patch
from src.orchestrator import PipelineOrchestrator

def test_pipeline_initialization():
    orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
    assert orchestrator.config is not None
    assert 'pipeline' in orchestrator.config

def test_execution_flow_success():
    with patch('src.data_validation.DataValidator') as mock_validator,          patch('src.data_processing.DataProcessor') as mock_processor,          patch('src.data_enrichment.DataEnricher') as mock_enricher,          patch('src.quality_checks.QualityChecker') as mock_quality:
        mock_validator.return_value.validate.return_value = {'success': True}
        mock_processor.return_value.process.return_value = {'processed_data': [], 'record_count': 100}
        mock_enricher.return_value.enrich.return_value = {'enriched_data': []}
        mock_quality.return_value.check_quality.return_value = {'passed': True}

        orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
        result = orchestrator.execute_pipeline()
        assert result['success'] == True
        assert 'execution_id' in result

def test_execution_flow_failure():
    with patch('src.data_validation.DataValidator') as mock_validator:
        mock_validator.return_value.validate.return_value = {'success': False, 'errors': ['Schema validation failed']}
        orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
        result = orchestrator.execute_pipeline()
        assert result['success'] == False
        assert 'error' in result
