# tests/integration_test.py
import os
from src.orchestrator import PipelineOrchestrator

def run_integration():
    os.system('python scripts/download_sample_data.py')
    orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
    result = orchestrator.execute_pipeline()
    print('Integration result:', result)
    if not result.get('success'):
        raise SystemExit(1)

if __name__ == '__main__':
    run_integration()
