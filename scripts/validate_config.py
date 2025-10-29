# scripts/validate_config.py
import yaml, sys, os
path = 'config/pipeline_config.yaml'
if not os.path.exists(path):
    print('Config no encontrada', file=sys.stderr); sys.exit(2)
try:
    with open(path, 'r', encoding='utf-8') as f:
        cfg = yaml.safe_load(f)
    assert 'validation' in cfg and 'processing' in cfg and 'enrichment' in cfg
    print('Validación de config OK')
except Exception as e:
    print(f'Fallo validación de config: {e}', file=sys.stderr)
    sys.exit(1)