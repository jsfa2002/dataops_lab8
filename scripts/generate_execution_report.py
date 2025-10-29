# scripts/generate_execution_report.py
import os, json
from datetime import datetime
outputs_dir = 'data/outputs'
os.makedirs(outputs_dir, exist_ok=True)
report = {
    'generated_at': datetime.now().isoformat(),
    'outputs_present': os.listdir(outputs_dir)
}
out = os.path.join(outputs_dir, f'execution_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2)
print('Execution report generated:', out)