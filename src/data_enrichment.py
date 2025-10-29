# src/data_enrichment.py
import csv
import os
import logging

class DataEnricher:
    def __init__(self, config):
        self.catalog_path = config.get('catalog_path', 'data/raw/product_catalog.csv')
        self.logger = logging.getLogger(__name__)
        self.catalog = self.load_catalog()

    def load_catalog(self):
        if not os.path.exists(self.catalog_path):
            self.logger.warning(f"Archivo de catálogo no encontrado: {self.catalog_path}")
            return {}
        cat = {}
        with open(self.catalog_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                pid = row.get('product_id')
                cat[pid] = row
        self.logger.info(f"Catálogo cargado con {len(cat)} entradas")
        return cat

    def enrich(self, processed_data):
        enriched = []
        for r in processed_data:
            prod = self.catalog.get(r.get('product_id'), {})
            r_enriched = r.copy()
            r_enriched['product_name'] = prod.get('product_name', 'unknown')
            r_enriched['category'] = prod.get('category', 'unknown')
            enriched.append(r_enriched)

        out_file = 'data/outputs/sales_enriched.csv'
        if enriched:
            with open(out_file, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = list(enriched[0].keys())
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for r in enriched:
                    writer.writerow(r)
            self.logger.info(f"Datos enriquecidos guardados en {out_file}")
        else:
            self.logger.info("No hay datos para enriquecer.")

        return {'enriched_data': enriched}
