# src/data_validation.py
import os
import json
import logging

class DataValidator:
    def __init__(self, config):
        self.schema_path = config.get('schema_path', '')
        self.required_files = config.get('required_files', [])
        self.logger = logging.getLogger(__name__)

    def validate(self):
        errors = []
        
        # Verificar archivos requeridos
        for file_path in self.required_files:
            if not os.path.exists(file_path):
                errors.append(f"Archivo requerido no encontrado: {file_path}")
        
        # Verificar esquema (si existe)
        if self.schema_path and os.path.exists(self.schema_path):
            try:
                with open(self.schema_path, 'r') as f:
                    json.load(f)
                self.logger.info("Esquema validado correctamente")
            except Exception as e:
                errors.append(f"Error en esquema: {e}")
        
        success = len(errors) == 0
        return {'success': success, 'errors': errors}
