# scripts/download_sample_data.py
import os, json, csv
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/schemas', exist_ok=True)

sales_path = 'data/raw/sales_data.csv'
with open(sales_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['order_id','product_id','quantity','price','region','order_date'])
    writer.writeheader()
    writer.writerow({'order_id':'O-001','product_id':'P-001','quantity':2,'price':10.0,'region':'north','order_date':'2025-10-01T10:00:00'})
    writer.writerow({'order_id':'O-002','product_id':'P-002','quantity':1,'price':20.0,'region':'south','order_date':'2025-10-02T11:00:00'})
    writer.writerow({'order_id':'O-003','product_id':'P-003','quantity':3,'price':5.5,'region':'center','order_date':'2025-10-03T12:30:00'})

catalog_path = 'data/raw/product_catalog.csv'
with open(catalog_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['product_id','product_name','category'])
    writer.writeheader()
    writer.writerow({'product_id':'P-001','product_name':'Producto A','category':'Cat1'})
    writer.writerow({'product_id':'P-002','product_name':'Producto B','category':'Cat2'})
    writer.writerow({'product_id':'P-003','product_name':'Producto C','category':'Cat1'})

schema_src = 'data/schemas/sales_schema_v1.json'
if not os.path.exists(schema_src):
    schema_content = {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "title": "sales",
      "type": "object",
      "properties": {
        "order_id": {"type": "string"},
        "product_id": {"type": "string"},
        "quantity": {"type": "integer", "minimum": 0},
        "price": {"type": "number", "minimum": 0},
        "region": {"type": "string"},
        "order_date": {"type": "string", "format": "date-time"}
      },
      "required": ["order_id", "product_id", "quantity", "price", "order_date"]
    }
    with open(schema_src, 'w', encoding='utf-8') as f:
        json.dump(schema_content, f, indent=2)

print('Datos de ejemplo generados en data/raw/')