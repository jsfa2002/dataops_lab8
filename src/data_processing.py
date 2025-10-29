# src/data_processing.py
import os
import csv
import logging

class DataProcessor:
    def __init__(self, config):
        self.output_path = config.get('output_path', 'data/processed/')
        self.steps = config.get('steps', [])
        self.logger = logging.getLogger(__name__)
        os.makedirs(self.output_path, exist_ok=True)

    def process(self):
        input_file = 'data/raw/sales_data.csv'
        processed = []
        record_count = 0
        if not os.path.exists(input_file):
            self.logger.warning(f"No existe {input_file}, se devuelve conjunto vacío")
            return {'processed_data': processed, 'record_count': 0}

        with open(input_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            seen = set()
            for row in reader:
                order_id = row.get('order_id')
                # simple deduplication
                if order_id in seen:
                    continue
                seen.add(order_id)
                try:
                    quantity = int(row.get('quantity') or 0)
                except:
                    quantity = 0
                try:
                    price = float(row.get('price') or 0.0)
                except:
                    price = 0.0
                total = quantity * price
                processed.append({
                    'order_id': order_id,
                    'product_id': row.get('product_id'),
                    'quantity': quantity,
                    'price': price,
                    'total': total,
                    'region': row.get('region'),
                    'order_date': row.get('order_date')
                })
                record_count += 1

        out_file = os.path.join(self.output_path, 'sales_processed.csv')
        with open(out_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['order_id','product_id','quantity','price','total','region','order_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for r in processed:
                writer.writerow(r)

        self.logger.info(f"Procesamiento completado. {record_count} registros procesados. Output: {out_file}")
        return {'processed_data': processed, 'record_count': record_count}
