# src/quality_checks.py
import logging

class QualityChecker:
    def __init__(self, config):
        self.checks = config.get('checks', [])
        self.logger = logging.getLogger(__name__)

    def check_quality(self, enriched_data):
        issues = []
        passed = True
        if not enriched_data:
            issues.append("No hay datos para evaluar calidad")
            return {'passed': False, 'issues': issues}

        total_records = len(enriched_data)
        null_count = 0
        for r in enriched_data:
            if r.get('total') is None:
                null_count += 1
            if r.get('total', 0) < 0:
                issues.append(f"Total negativo en order_id {r.get('order_id')}")
        completeness = 1 - (null_count / total_records)
        threshold = 0.9
        for c in self.checks:
            if isinstance(c, str) and 'completeness_threshold' in c:
                try:
                    threshold = float(c.split(':')[1])
                except:
                    pass
        if completeness < threshold:
            issues.append(f"Completitud baja: {completeness:.2f} < {threshold}")
            passed = False
        if issues:
            passed = False
        return {'passed': passed, 'issues': issues}
