# src/data_validation.py
import os
import json
import logging
from jsonschema import validate, ValidationError

class DataValidator:
    """Comprueba existencia de archivos requeridos y validez del esquema JSON."""
    def __init__(self, config):
        self.schema_path = config.get('schema_path')
        self.required_files = config.get('required_files', [])
        self.logger = logging.getLogger(__name__)

    def validate(self):
        errors = []
        # 1. Comprobar archivos requeridos
        for f in self.required_files:
            if not os.path.exists(f):
                errors.append(f"Archivo requerido ausente: {f}")

        # 2. Comprobar esquema (si existe)
        if self.schema_path and os.path.exists(self.schema_path):
            try:
                with open(self.schema_path, 'r', encoding='utf-8') as sf:
                    schema = json.load(sf)
                self.logger.info("Esquema cargado correctamente.")
            except Exception as e:
                errors.append(f"Error al cargar/parcear esquema: {e}")
        else:
            errors.append(f"Esquema no encontrado en {self.schema_path}")

        success = len(errors) == 0
        return {'success': success, 'errors': errors}

if __name__ == '__main__':
    import yaml
    cfg = yaml.safe_load(open('config/pipeline_config.yaml', encoding='utf-8'))
    dv = DataValidator(cfg['validation'])
    print(dv.validate())
